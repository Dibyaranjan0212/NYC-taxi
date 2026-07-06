import pandas as pd

from pathlib import Path


def create_fact_trip(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create the fact_trip table.
    """

    fact_df = df.copy()

    # Create surrogate key
    fact_df.insert(
        0,
        "trip_key",
        range(1, len(fact_df) + 1),
    )

    # Date key (YYYYMMDD)
    fact_df["date_key"] = (
        pd.to_datetime(
            fact_df["pickup_date"]
        )
        .dt.strftime("%Y%m%d")
        .astype(int)
    )

    # Trip duration
    fact_df["trip_duration_minutes"] = (
        (
            fact_df["tpep_dropoff_datetime"]
            -
            fact_df["tpep_pickup_datetime"]
        )
        .dt.total_seconds()
        / 60
    ).round(2)

    return fact_df[
        [
            "trip_key",
            "date_key",
            "VendorID",
            "PULocationID",
            "DOLocationID",
            "payment_type",
            "passenger_count",
            "trip_distance",
            "trip_duration_minutes",
            "fare_amount",
            "tip_amount",
            "total_amount",
        ]
    ]


def create_dim_date(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create the date dimension.
    """

    date_df = (
        pd.DataFrame(
            {
                "pickup_date":
                pd.to_datetime(
                    df["pickup_date"]
                )
            }
        )
        .drop_duplicates()
        .sort_values(
            "pickup_date"
        )
    )

    date_df["date_key"] = (
        date_df["pickup_date"]
        .dt.strftime("%Y%m%d")
        .astype(int)
    )

    date_df["year"] = (
        date_df["pickup_date"]
        .dt.year
    )

    date_df["quarter"] = (
        date_df["pickup_date"]
        .dt.quarter
    )

    date_df["month"] = (
        date_df["pickup_date"]
        .dt.month
    )

    date_df["month_name"] = (
        date_df["pickup_date"]
        .dt.month_name()
    )

    date_df["day"] = (
        date_df["pickup_date"]
        .dt.day
    )

    date_df["day_of_week"] = (
        date_df["pickup_date"]
        .dt.day_name()
    )

    date_df["week_of_year"] = (
        date_df["pickup_date"]
        .dt.isocalendar()
        .week
    )

    date_df["is_weekend"] = (
        date_df["pickup_date"]
        .dt.dayofweek
        >= 5
    )

    return date_df


def create_dim_payment() -> pd.DataFrame:
    """
    Create payment dimension.
    """

    return pd.DataFrame(
        {
            "payment_type": [
                1,
                2,
                3,
                4,
                5,
                6,
            ],
            "payment_name": [
                "Credit Card",
                "Cash",
                "No Charge",
                "Dispute",
                "Unknown",
                "Voided Trip",
            ],
        }
    )


def create_dim_location(
    lookup_path: str,
) -> pd.DataFrame:
    """
    Create location dimension
    from NYC Taxi Zone Lookup.
    """

    location_df = pd.read_csv(
        lookup_path
    )

    location_df.columns = [
        "LocationID",
        "Borough",
        "Zone",
        "ServiceZone",
    ]

    return location_df


def create_trip_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Monthly KPI summary.
    """

    summary = (
        df.groupby(
            [
                "pickup_month",
                "payment_type",
            ]
        )
        .agg(
            trip_count=(
                "VendorID",
                "count",
            ),
            total_revenue=(
                "total_amount",
                "sum",
            ),
            average_fare=(
                "fare_amount",
                "mean",
            ),
            average_tip=(
                "tip_amount",
                "mean",
            ),
            average_distance=(
                "trip_distance",
                "mean",
            ),
        )
        .reset_index()
    )

    summary = summary.round(2)

    return summary