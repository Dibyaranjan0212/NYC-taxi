import pandas as pd


def cast_columns(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Cast columns to the required data types.
    """

    df = df.copy()

    # Integer columns
    df["passenger_count"] = (
        pd.to_numeric(
            df["passenger_count"],
            errors="coerce",
        )
        .astype("Int64")
    )

    # Float columns
    float_columns = [
        "trip_distance",
        "fare_amount",
        "tip_amount",
        "total_amount",
    ]

    for column in float_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce",
        )

    # Timestamp columns
    datetime_columns = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
    ]

    for column in datetime_columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce",
        )

    return df


def fill_nulls(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Fill missing values.
    """

    df = df.copy()

    df["passenger_count"] = (
        df["passenger_count"]
        .fillna(1)
        .astype("Int64")
    )

    df["tip_amount"] = (
        df["tip_amount"]
        .fillna(0.0)
    )

    return df