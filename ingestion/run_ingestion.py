from ingestion.downloader import (
    download_monthly_file,
    download_zone_lookup
)

from utils.config import load_config
from utils.logger import get_logger

logger = get_logger(__name__)


def run():

    config = load_config()

    year = config["pipeline"]["start_year"]

    bronze_path = config["storage"]["bronze_path"]

    logger.info(
        f"Starting ingestion for {year}"
    )

    for month in range(1, 13):

        download_monthly_file(
            year=year,
            month=month,
            output_dir=bronze_path
        )

    download_zone_lookup(
        output_dir=bronze_path
    )

    logger.info(
        "Bronze ingestion completed successfully."
    )


if __name__ == "__main__":
    run()