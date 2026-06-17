import yaml

from pyspark.sql import DataFrame

from pyspark.sql.functions import (
    count,
    sum as _sum,
    avg,
    round as _round
)

from common.spark_utils import (
    create_spark_session
)

def load_config():

    with open(
        "config/databricks.yaml",
        "r"
    ) as file:

        return yaml.safe_load(file)
    
def read_silver(
        spark,
        silver_path
):

    return (
        spark.read
        .format("delta")
        .load(
            silver_path
        )
    )

def build_daily_location_summary(
        df: DataFrame
):

    return (
        df.groupBy(
            "pickup_date",
            "PULocationID"
        )
        .agg(
            count("*")
            .alias(
                "total_trips"
            ),

            _round(
                _sum(
                    "total_amount"
                ),
                2
            ).alias(
                "total_revenue"
            ),

            _round(
                avg(
                    "fare_amount"
                ),
                2
            ).alias(
                "avg_fare"
            )
        )
    )

def write_gold(
        df,
        output_path
):

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .save(
            output_path
        )
    )


def run():

    config = load_config()

    silver_path = (
        config["storage"]
        ["silver_path"]
    )

    gold_path = (
        config["storage"]
        ["gold_path"]
    )

    spark = create_spark_session(
        "SilverToGold"
    )

    df = read_silver(
        spark,
        silver_path
    )

    daily_summary = (
        build_daily_location_summary(
            df
        )
    )

    write_gold(
        daily_summary,
        f"{gold_path}/daily_location_summary"
    )

    spark.stop()


if __name__ == "__main__":

    run()