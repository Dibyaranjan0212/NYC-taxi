import pandas as pd


def filter_invalid_records(
    df: pd.DataFrame,
    processing_year: int,
) -> pd.DataFrame:
    """
    Remove invalid trip records.

    Validation Rules
    ----------------
    - fare_amount > 0
    - trip_distance > 0
    - passenger_count > 0
    - dropoff time must be after pickup time
    - pickup year must equal processing year
    """

    df = df.copy()

    df = df[
        (df["fare_amount"] > 0)
        & (df["trip_distance"] > 0)
        & (df["passenger_count"] > 0)
        & (
            df["tpep_dropoff_datetime"]
            > df["tpep_pickup_datetime"]
        )
        & (
            df["tpep_pickup_datetime"].dt.year
            == processing_year
        )
    ]

    return df.reset_index(drop=True)