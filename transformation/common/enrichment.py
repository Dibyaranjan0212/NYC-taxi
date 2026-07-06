import pandas as pd

from datetime import datetime, timezone


def add_derived_columns(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Add derived columns required for the Silver layer.

    Derived Columns
    ---------------
    - pickup_date
    - pickup_month
    - pickup_hour
    - pickup_day_of_week
    - _processed_at
    """

    df = df.copy()

    # Ensure pickup datetime is a datetime dtype
    df["tpep_pickup_datetime"] = pd.to_datetime(
        df["tpep_pickup_datetime"],
        errors="coerce",
    )

    # Date
    df["pickup_date"] = (
        df["tpep_pickup_datetime"]
        .dt.date
    )

    # Month (1-12)
    df["pickup_month"] = (
        df["tpep_pickup_datetime"]
        .dt.month
    )

    # Hour (0-23)
    df["pickup_hour"] = (
        df["tpep_pickup_datetime"]
        .dt.hour
    )

    # Day of Week
    # Monday = 1 ... Sunday = 7
    df["pickup_day_of_week"] = (
        df["tpep_pickup_datetime"]
        .dt.dayofweek
        + 1
    )

    # Pipeline execution timestamp (UTC)
    df["_processed_at"] = datetime.now(
        timezone.utc
    )

    return df