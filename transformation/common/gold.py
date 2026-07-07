import pandas as pd
from common.config import LOOKUP_PATH
from common.config import (
    LOOKUP_PATH,
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
    AWS_REGION,
)


def create_fact_trip(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create Fact Trip table from Silver layer.

    Parameters
    ----------
    df : pd.DataFrame Silver dataframe.
   
    Returns
    -------
    pd.DataFrame
        Fact Trip dataframe.
    """
    fact_df = df.copy()

    fact_df["date_key"] = (
        pd.to_datetime(
            fact_df["pickup_date"]
        )
        .dt.strftime("%Y%m%d")
        .astype(int)
    )

    fact_df["trip_duration_minutes"] = (
        (
            pd.to_datetime(
                fact_df["tpep_dropoff_datetime"]
            )
            -
            pd.to_datetime(
                fact_df["tpep_pickup_datetime"]
            )
        )
        .dt.total_seconds()
        .div(60)
        .round(2)
    )

    fact_df = fact_df.rename(
        columns={
            "VendorID": "vendor_key",
            "payment_type": "payment_key",
            "PULocationID": "pickup_location_key",
            "DOLocationID": "dropoff_location_key",
        }
    )

    fact_df = fact_df[
        [
            "date_key",
            "vendor_key",
            "payment_key",
            "pickup_location_key",
            "dropoff_location_key",
            "passenger_count",
            "trip_distance",
            "trip_duration_minutes",
            "fare_amount",
            "tip_amount",
            "total_amount",
        ]
    ]

    fact_df = fact_df.astype(
    {
        "date_key": "int64",
        "vendor_key": "int64",
        "payment_key": "int64",
        "pickup_location_key": "int64",
        "dropoff_location_key": "int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "trip_duration_minutes": "float64",
        "fare_amount": "float64",
        "tip_amount": "float64",
        "total_amount": "float64",
    }
)

    return fact_df

def create_fact_daily(
    fact_trip_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create daily summary fact table.

    Parameters
    ----------
    fact_trip_df : pd.DataFrame
        Fact Trip dataframe for a single day.
    Returns
    -------
    pd.DataFrame
        Daily summary dataframe.
    """

    date_key = fact_trip_df["date_key"].iloc[0]
    fact_daily = pd.DataFrame(
        {
            "date_key": [date_key],
            "trip_count": [len(fact_trip_df)],
            "total_passengers": [fact_trip_df["passenger_count"].sum()],
            "total_distance": [fact_trip_df["trip_distance"].sum()],
            "avg_distance": [round(fact_trip_df["trip_distance"].mean(),2)],
            "total_fare": [round(fact_trip_df["fare_amount"].sum(),2)],
            "avg_fare": [round(fact_trip_df["fare_amount"].mean(), 2)],
            "total_tip": [round(fact_trip_df["tip_amount"].sum(),2)],
            "avg_tip": [round( fact_trip_df["tip_amount"].mean(), 2)],
            "total_revenue": [round(fact_trip_df["total_amount"].sum(),2)],
            "avg_revenue": [round(fact_trip_df["total_amount"].mean(),2)],
            "avg_trip_duration": [round(fact_trip_df["trip_duration_minutes"].mean(),2)]})

    return fact_daily


def create_dim_payment() -> pd.DataFrame:
    """
    Create Payment Dimension.

    Returns
    -------
    pd.DataFrame
        Payment Dimension dataframe.
    """

    payment_mapping = {
        0: "Flex Fare trip",
        1: "Credit Card",
        2: "Cash",
        3: "No Charge",
        4: "Dispute",
        5: "Unknown",
        6: "Voided Trip",
    }

    dim_payment = (
        pd.DataFrame(
            payment_mapping.items(),
            columns=[
                "payment_key",
                "payment_name",
            ],
        )
        .sort_values("payment_key")
        .reset_index(drop=True)
    )

    return dim_payment

def create_dim_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create Date Dimension.
    Parameters
    ----------
    df : pd.DataFrame
        Silver dataframe for a single date partition.

    Returns
    -------
    pd.DataFrame
        Date Dimension dataframe.
    """

    date = pd.to_datetime(df["pickup_date"].iloc[0])

    dim_date = pd.DataFrame(
        {
            "date_key": [int(date.strftime("%Y%m%d"))],
            "full_date": [date.date()],
            "year": [date.year],
            "quarter": [date.quarter],
            "month": [date.month],
            "month_name": [date.strftime("%B")],
            "week": [date.isocalendar().week],
            "day": [date.day],
            "day_name": [date.strftime("%A")],
            "day_of_week": [date.dayofweek + 1],
            "is_weekend": [date.dayofweek >= 5],
        }
    )

    return dim_date

def create_dim_vendor() -> pd.DataFrame:
    """
    Create Vendor Dimension.

    Returns
    -------
    pd.DataFrame
        Vendor Dimension dataframe.
    """

    vendor_mapping = {
        1: "Creative Mobile Technologies, LLC",
        2: "Curb Mobility, LLC",
        6: "Myle Technologies Inc",
        7: "Helix",
    }

    dim_vendor = (
        pd.DataFrame(
            vendor_mapping.items(),
            columns=[
                "vendor_key",
                "vendor_name",
            ],
        )
        .sort_values("vendor_key")
        .reset_index(drop=True)
    )

    return dim_vendor


def create_dim_location() -> pd.DataFrame:
    """
    Create Location Dimension from the NYC Taxi Zone lookup file.

    Returns
    -------
    pd.DataFrame
        Location Dimension dataframe.
    """

    dim_location = pd.read_csv(
        LOOKUP_PATH,
        storage_options={
            "key": AWS_ACCESS_KEY,
            "secret": AWS_SECRET_KEY,
            "client_kwargs": {
                "region_name": AWS_REGION,
            },
        },
    )

    dim_location = (
        dim_location.rename(
            columns={
                "LocationID": "location_key",
                "Borough": "borough",
                "Zone": "zone",
                "service_zone": "service_zone",
            }
        )
        .drop_duplicates(subset="location_key")
        .sort_values("location_key")
        .reset_index(drop=True)
    )

    dim_location = dim_location[
        [
            "location_key",
            "borough",
            "zone",
            "service_zone",
        ]
    ]

    return dim_location

