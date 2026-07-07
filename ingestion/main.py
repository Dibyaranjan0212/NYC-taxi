from ingestion.src.downloader import (
    download_monthly_file,
    download_zone_lookup
)

from ingestion.src.s3_upload import (
    upload_bronze_file,
    delete_local_file
)

from utils.config import load_config
from utils.logger import get_logger

logger = get_logger(__name__)


def run():

    config = load_config()

    year = config["pipeline"]["start_year"]

    download_path = (
        config["local"]["download_path"]
    )

    logger.info(
        f"Starting ingestion for {year}"
    )

    for month in range(1, 13):

        local_file = download_monthly_file(
            year=year,
            month=month,
            output_dir=download_path
        )

        upload_bronze_file(
            local_file
        )

        delete_local_file(
            local_file
        )

    zone_lookup = download_zone_lookup(
        output_dir=download_path
    )

    upload_bronze_file(
        zone_lookup
    )

    delete_local_file(
        zone_lookup
    )

    logger.info(
        "Bronze ingestion completed."
    )


if __name__ == "__main__":
    run()