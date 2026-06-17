from pyspark.sql import DataFrame
from pyspark.sql.functions import col

from pyspark.sql.types import (
    IntegerType,
    DoubleType,
    TimestampType
)


def cast_columns(
        df: DataFrame
) -> DataFrame:

    return (
        df
        .withColumn(
            "passenger_count",
            col("passenger_count")
            .cast(IntegerType())
        )
        .withColumn(
            "trip_distance",
            col("trip_distance")
            .cast(DoubleType())
        )
        .withColumn(
            "fare_amount",
            col("fare_amount")
            .cast(DoubleType())
        )
        .withColumn(
            "tip_amount",
            col("tip_amount")
            .cast(DoubleType())
        )
        .withColumn(
            "total_amount",
            col("total_amount")
            .cast(DoubleType())
        )
        .withColumn(
            "tpep_pickup_datetime",
            col("tpep_pickup_datetime")
            .cast(TimestampType())
        )
        .withColumn(
            "tpep_dropoff_datetime",
            col("tpep_dropoff_datetime")
            .cast(TimestampType())
        )
    )


def fill_nulls(
        df: DataFrame
) -> DataFrame:

    return (
        df
        .fillna(
            {"passenger_count": 1}
        )
        .fillna(
            {"tip_amount": 0.0}
        )
    )