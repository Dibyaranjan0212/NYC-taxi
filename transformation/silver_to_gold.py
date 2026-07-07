"""
Silver → Gold ETL Pipeline

Reads one Silver partition at a time,
creates Gold star schema,
and writes the results back to S3.
"""

import gc

import boto3
import pandas as pd

from common.config import (
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
    AWS_REGION,
    SILVER_PATH,
    GOLD_PATH,
    LOOKUP_PATH,
)

from common.gold import (
    create_fact_trip,
    create_fact_daily,
    create_dim_date,
    create_dim_payment,
    create_dim_vendor,
    create_dim_location,
)

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

def read_parquet(file_path: str) -> pd.DataFrame:
    """
    Read a single parquet file from S3.
    """

    print(f"Reading : {file_path}")

    return pd.read_parquet(
        file_path,
        storage_options={
            "key": AWS_ACCESS_KEY,
            "secret": AWS_SECRET_KEY,
            "client_kwargs": {
                "region_name": AWS_REGION
            },
        },
    )

def write_parquet(
    df: pd.DataFrame,
    path: str,
    partition_cols=None,
) -> None:
    """
    Write dataframe to S3.
    """

    df.to_parquet(
        path,
        engine="pyarrow",
        compression="snappy",
        index=False,
        partition_cols=partition_cols,
        storage_options={
            "key": AWS_ACCESS_KEY,
            "secret": AWS_SECRET_KEY,
            "client_kwargs": {
                "region_name": AWS_REGION
            },
        },
    )

def list_silver_files():
    """
    Return every parquet file in Silver.
    """

    bucket = SILVER_PATH.replace(
        "s3://",
        ""
    ).split("/")[0]

    prefix = "/".join(
        SILVER_PATH.replace(
            "s3://",
            ""
        ).split("/")[1:]
    )

    paginator = s3_client.get_paginator(
        "list_objects_v2"
    )

    parquet_files = []

    for page in paginator.paginate(
        Bucket=bucket,
        Prefix=prefix,
    ):

        for obj in page.get(
            "Contents",
            []
        ):

            key = obj["Key"]

            if key.endswith(".parquet"):

                parquet_files.append(
                    f"s3://{bucket}/{key}"
                )

    parquet_files.sort()

    return parquet_files


def run():
    """
    Run Silver -> Gold ETL Pipeline.
    """

    print("=" * 80)
    print("Starting Silver -> Gold Pipeline")
    print("=" * 80)

    # ============================================================
    # Create Static Dimensions
    # ============================================================

    print("\nCreating static dimensions...")

    dim_payment = create_dim_payment()
    dim_vendor = create_dim_vendor()
    dim_location = create_dim_location()

    write_parquet(
        dim_payment,
        f"{GOLD_PATH}/dim_payment/",
    )

    write_parquet(
        dim_vendor,
        f"{GOLD_PATH}/dim_vendor/",
    )

    write_parquet(
        dim_location,
        f"{GOLD_PATH}/dim_location/",
    )

    print("Static dimensions created.\n")

    # ============================================================
    # Lists for Dynamic Dimensions
    # ============================================================

    fact_daily_list = []

    dim_date_list = []

    # ============================================================
    # Get Silver Files
    # ============================================================

    parquet_files = list_silver_files()

    print(f"Found {len(parquet_files)} partitions.\n")

    # ============================================================
    # Process One File At A Time
    # ============================================================

    for index, file_path in enumerate(parquet_files, start=1):

        print("=" * 80)
        print(f"Processing ({index}/{len(parquet_files)})")
        print(file_path)

        # --------------------------------------------------------

        silver_df = read_parquet(file_path)

        # --------------------------------------------------------
        # FACT TRIP
        # --------------------------------------------------------

        fact_trip = create_fact_trip(silver_df)

        date_key = fact_trip["date_key"].iloc[0]

        write_parquet(
            fact_trip,
            f"{GOLD_PATH}/fact_trip/date_key={date_key}/",
        )

        # --------------------------------------------------------
        # FACT DAILY
        # --------------------------------------------------------

        fact_daily = create_fact_daily(fact_trip)

        fact_daily_list.append(fact_daily)

        # --------------------------------------------------------
        # DIM DATE
        # --------------------------------------------------------

        dim_date = create_dim_date(silver_df)

        dim_date_list.append(dim_date)

        # --------------------------------------------------------
        # Free Memory
        # --------------------------------------------------------

        del silver_df
        del fact_trip
        del fact_daily
        del dim_date

        gc.collect()

    print("\nFinished processing all partitions.")

        # ============================================================
    # Merge Dynamic Tables
    # ============================================================

    print("\nCreating dynamic dimensions...")

    fact_daily_df = (
        pd.concat(
            fact_daily_list,
            ignore_index=True,
        )
        .sort_values("date_key")
        .reset_index(drop=True)
    )

    dim_date_df = (
        pd.concat(
            dim_date_list,
            ignore_index=True,
        )
        .drop_duplicates(subset="date_key")
        .sort_values("date_key")
        .reset_index(drop=True)
    )

    # ============================================================
    # Write Fact Daily
    # ============================================================

    write_parquet(
        fact_daily_df,
        f"{GOLD_PATH}/fact_daily/",
    )

    # ============================================================
    # Write Date Dimension
    # ============================================================

    write_parquet(
        dim_date_df,
        f"{GOLD_PATH}/dim_date/",
    )

    print("\nDynamic tables created successfully.")


    print("\n" + "=" * 80)
    print("Silver -> Gold Pipeline Completed Successfully")
    print("=" * 80)

    print(f"Partitions Processed : {len(parquet_files)}")
    print(f"Fact Daily Rows      : {len(fact_daily_df)}")
    print(f"Date Dimension Rows  : {len(dim_date_df)}")

if __name__ == "__main__":

    run()