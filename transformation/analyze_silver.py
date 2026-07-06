import pandas as pd

from common.config import SILVER_PATH
from common.io_utils import read_parquet


def main():

    print("=" * 80)
    print("READING SILVER DATA")
    print("=" * 80)

    df = read_parquet(SILVER_PATH)

    print()

    print("=" * 80)
    print("DATA SHAPE")
    print("=" * 80)

    print(f"Rows    : {len(df):,}")
    print(f"Columns : {len(df.columns)}")

    print()

    print("=" * 80)
    print("COLUMN NAMES")
    print("=" * 80)

    for i, col in enumerate(df.columns, start=1):
        print(f"{i:2d}. {col}")

    print()

    print("=" * 80)
    print("DATA TYPES")
    print("=" * 80)

    print(df.dtypes)

    print()

    print("=" * 80)
    print("NULL VALUES")
    print("=" * 80)

    print(df.isnull().sum())

    print()

    print("=" * 80)
    print("UNIQUE VALUES")
    print("=" * 80)

    for col in df.columns:
        print(f"{col:<30} {df[col].nunique()}")

    print()

    print("=" * 80)
    print("NUMERIC SUMMARY")
    print("=" * 80)

    print(df.describe())

    print()

    print("=" * 80)
    print("FIRST 5 ROWS")
    print("=" * 80)

    print(df.head())

    print()

    print("=" * 80)
    print("LAST 5 ROWS")
    print("=" * 80)

    print(df.tail())

    print()

    print("=" * 80)
    print("SAMPLE RECORD")
    print("=" * 80)

    print(df.iloc[0])

    print()

    print("=" * 80)
    print("LIST OF COLUMNS")
    print("=" * 80)

    print(df.columns.tolist())


if __name__ == "__main__":
    main()