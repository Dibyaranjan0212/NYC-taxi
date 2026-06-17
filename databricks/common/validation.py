from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    year
)


def filter_invalid_records(
        df: DataFrame,
        processing_year: int
) -> DataFrame:

    return df.filter(
        (col("fare_amount") > 0)
        &
        (col("trip_distance") > 0)
        &
        (col("passenger_count") > 0)
        &
        (
            col("tpep_dropoff_datetime")
            >
            col("tpep_pickup_datetime")
        )
        &
        (
            year(
                col(
                    "tpep_pickup_datetime"
                )
            )
            ==
            processing_year
        )
    )