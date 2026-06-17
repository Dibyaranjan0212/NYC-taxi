from pyspark.sql import DataFrame

from pyspark.sql.functions import (
    to_date,
    month,
    dayofweek,
    hour,
    col,
    current_timestamp
)


def add_derived_columns(
        df: DataFrame
) -> DataFrame:

    return (
        df
        .withColumn(
            "pickup_date",
            to_date(
                col(
                    "tpep_pickup_datetime"
                )
            )
        )
        .withColumn(
            "pickup_month",
            month(
                col(
                    "tpep_pickup_datetime"
                )
            )
        )
        .withColumn(
            "pickup_hour",
            hour(
                col(
                    "tpep_pickup_datetime"
                )
            )
        )
        .withColumn(
            "pickup_day_of_week",
            dayofweek(
                col(
                    "tpep_pickup_datetime"
                )
            )
        )
        .withColumn(
            "_processed_at",
            current_timestamp()
        )
    )