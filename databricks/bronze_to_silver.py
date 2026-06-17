import yaml

from pyspark.sql import DataFrame

from common.spark_utils import (
    create_spark_session
)

from common.config import (
    BRONZE_PATH,
    SILVER_PATH,
    PROCESSING_YEAR
)
from common.cleaning import (
    cast_columns,
    fill_nulls
)

from common.validation import (
    filter_invalid_records
)

from common.enrichment import (
    add_derived_columns
)




def read_bronze(
        spark,
        bronze_path: str
) -> DataFrame:

    print(
        f"Reading Bronze: {bronze_path}"
    )

    return spark.read.parquet(
        bronze_path
    )


def select_final_columns(
        df: DataFrame
) -> DataFrame:

    return df.select(
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

        "_processed_at"
    )


def write_silver(
        df: DataFrame,
        silver_path: str
):

    print(
        f"Writing Silver: {silver_path}"
    )

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .partitionBy(
            "pickup_date"
        )
        .save(
            silver_path
        )
    )

def run():

    spark = create_spark_session(
        "BronzeToSilver"
    )

    df = read_bronze(
        spark,
        BRONZE_PATH
    )

    df = cast_columns(df)

    df = fill_nulls(df)

    df = filter_invalid_records(
        df,
        PROCESSING_YEAR
    )

    df = add_derived_columns(df)

    df = select_final_columns(df)

    write_silver(
        df,
        SILVER_PATH
    )

    spark.stop()


if __name__ == "__main__":

    run()