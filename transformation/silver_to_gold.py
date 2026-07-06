import pandas as pd

from common.config import (
    SILVER_PATH,
    GOLD_PATH,
    LOCATION_LOOKUP_PATH,
)

from common.io_utils import (
    read_parquet,
    write_parquet,
)

from common.gold import (
    create_fact_trip,
    create_dim_date,
    create_dim_location,
    create_dim_payment,
    create_trip_summary,
)


def run() -> None:
    """
    Execute the Silver → Gold pipeline.
    """

    try:

        print("=" * 60)
        print("Starting Silver → Gold Pipeline")
        print("=" * 60)

        # Read Silver Layer
        silver_df = read_parquet(
            SILVER_PATH
        )

        print(
            f"Silver records: {len(silver_df):,}"
        )

        # Create Gold Tables
        fact_trip = create_fact_trip(
            silver_df
        )

        dim_date = create_dim_date(
            silver_df
        )

        dim_payment = create_dim_payment()

        dim_location = create_dim_location(
            LOCATION_LOOKUP_PATH
        )

        trip_summary = create_trip_summary(
            silver_df
        )

        # Write Fact Table
        write_parquet(
            fact_trip,
            f"{GOLD_PATH}/fact_trip/"
        )

        # Write Date Dimension
        write_parquet(
            dim_date,
            f"{GOLD_PATH}/dim_date/"
        )

        # Write Payment Dimension
        write_parquet(
            dim_payment,
            f"{GOLD_PATH}/dim_payment/"
        )

        # Write Location Dimension
        write_parquet(
            dim_location,
            f"{GOLD_PATH}/dim_location/"
        )

        # Write KPI Summary
        write_parquet(
            trip_summary,
            f"{GOLD_PATH}/trip_summary/"
        )

        print()

        print("Gold Layer Created Successfully")

        print(f"Fact Trips      : {len(fact_trip):,}")
        print(f"Date Dimension  : {len(dim_date):,}")
        print(f"Location Dim    : {len(dim_location):,}")
        print(f"Payment Dim     : {len(dim_payment):,}")
        print(f"Trip Summary    : {len(trip_summary):,}")

        print()

        print("=" * 60)
        print("Silver → Gold Pipeline Completed")
        print("=" * 60)

    except Exception as e:

        print("=" * 60)
        print("Silver → Gold Pipeline Failed")
        print(f"Error: {e}")
        print("=" * 60)

        raise


if __name__ == "__main__":
    run()