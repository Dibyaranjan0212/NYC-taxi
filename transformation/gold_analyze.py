import pandas as pd

from common.config import (
    GOLD_PATH,
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
    AWS_REGION,
)

STORAGE_OPTIONS = {
    "key": AWS_ACCESS_KEY,
    "secret": AWS_SECRET_KEY,
    "client_kwargs": {
        "region_name": AWS_REGION,
    },
}


def inspect_table(name: str):
    print("\n" + "=" * 100)
    print(name.upper())
    print("=" * 100)

    path = f"{GOLD_PATH}/{name}/"

    try:
        df = pd.read_parquet(
            path,
            storage_options=STORAGE_OPTIONS,
        )

        print(f"\nPath : {path}")
        print(f"Rows : {len(df):,}")
        print(f"Columns : {len(df.columns)}")

        print("\nColumns")
        print("-" * 60)
        print(df.columns.tolist())

        print("\nData Types")
        print("-" * 60)
        print(df.dtypes)

        print("\nNull Values")
        print("-" * 60)
        print(df.isnull().sum())

        print("\nFirst 5 Rows")
        print("-" * 60)
        print(df.head())

        print("\nLast 5 Rows")
        print("-" * 60)
        print(df.tail())

        print("\nMemory Usage")
        print("-" * 60)
        print(
            round(
                df.memory_usage(deep=True).sum() / 1024,
                2,
            ),
            "KB",
        )

    except Exception as e:
        print(f"FAILED : {e}")


def inspect_fact_trip():

    print("\n" + "=" * 100)
    print("FACT_TRIP")
    print("=" * 100)

    path = f"{GOLD_PATH}/fact_trip/"

    try:

        df = pd.read_parquet(
            path,
            storage_options=STORAGE_OPTIONS,
        )

        print(f"\nRows : {len(df):,}")
        print(f"Columns : {len(df.columns)}")

        print("\nColumns")
        print(df.columns.tolist())

        print("\nDate Range")

        print(df["date_key"].min())
        print(df["date_key"].max())

        print("\nUnique Dates")

        print(df["date_key"].nunique())

        print("\nSample")

        print(df.head())

        print("\nSummary")

        print(df.describe())

    except Exception as e:

        print(e)


def main():

    inspect_fact_trip()

    inspect_table("fact_daily")

    inspect_table("dim_date")

    inspect_table("dim_payment")

    inspect_table("dim_vendor")

    inspect_table("dim_location")


if __name__ == "__main__":

    main()