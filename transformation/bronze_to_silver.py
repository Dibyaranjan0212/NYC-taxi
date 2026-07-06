import pandas as pd

from common.config import (
    BRONZE_PATH,
    SILVER_PATH,
    PROCESSING_YEAR,
)

from common.io_utils import (
    read_parquet,
    write_parquet,
)

from common.cleaning import (
    cast_columns,
    fill_nulls,
)

from common.validation import (
    filter_invalid_records,
)

from common.enrichment import (
    add_derived_columns,
)


def select_final_columns(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Select the required columns for the Silver layer.
    """

    columns = [
        "VendorID",
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "pickup_date",
        "pickup_month",
        "pickup_hour",
        "pickup_day_of_week",
        "passenger_count",
        "trip_distance",
        "PULocationID",
        "DOLocationID",
        "payment_type",
        "fare_amount",
        "tip_amount",
        "total_amount",
        "_processed_at",
    ]

    return df[columns]


def run() -> None:
    """
    Execute the Bronze → Silver transformation pipeline.
    """

    try:
        print("=" * 60)
        print("Starting Bronze → Silver Pipeline")
        print("=" * 60)

        # Read Bronze layer
        bronze_df = read_parquet(BRONZE_PATH)
        print(f"Bronze records: {len(bronze_df):,}")

        # Cleaning
        silver_df = cast_columns(bronze_df)
        silver_df = fill_nulls(silver_df)

        # Validation
        silver_df = filter_invalid_records(
            silver_df,
            PROCESSING_YEAR,
        )

        # Enrichment
        silver_df = add_derived_columns(silver_df)

        # Select final columns
        silver_df = select_final_columns(silver_df)

        print(f"Silver records: {len(silver_df):,}")

        # Write Silver layer
        write_parquet(
            silver_df,
            SILVER_PATH,
            partition_cols=["pickup_date"],
        )

        print("=" * 60)
        print("Bronze → Silver Pipeline Completed Successfully")
        print("=" * 60)

    except Exception as e:
        print("=" * 60)
        print("Bronze → Silver Pipeline Failed")
        print(f"Error: {e}")
        print("=" * 60)
        raise


if __name__ == "__main__":
    run()