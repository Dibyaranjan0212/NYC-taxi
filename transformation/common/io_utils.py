from pathlib import Path
import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

AWS_STORAGE_OPTIONS = {
    "key": os.getenv("AWS_ACCESS_KEY"),
    "secret": os.getenv("AWS_SECRET_KEY"),
    "client_kwargs": {
        "region_name": os.getenv("AWS_REGION"),
    },
}


def read_parquet(
    path: str,
) -> pd.DataFrame:
    """
    Read a parquet dataset from local storage or S3.
    """

    print(f"Reading parquet from: {path}")

    if path.startswith("s3://"):
        return pd.read_parquet(
            path,
            storage_options=AWS_STORAGE_OPTIONS,
            engine="pyarrow",
        )

    return pd.read_parquet(
        path,
        engine="pyarrow",
    )


def write_parquet(
    df: pd.DataFrame,
    path: str,
    partition_cols: list[str] | None = None,
) -> None:
    """
    Write dataframe as parquet.
    """

    print(f"Writing parquet to: {path}")

    if path.startswith("s3://"):

        df.to_parquet(
            path,
            engine="pyarrow",
            compression="snappy",
            index=False,
            partition_cols=partition_cols,
            storage_options=AWS_STORAGE_OPTIONS,
        )

    else:

        Path(path).mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_parquet(
            path,
            engine="pyarrow",
            compression="snappy",
            index=False,
            partition_cols=partition_cols,
        )

    print("Write completed successfully.")