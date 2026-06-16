from pathlib import Path
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from utils.config import load_config
from utils.logger import get_logger

logger = get_logger(__name__)

config = load_config()

BASE_URL = config["download"]["base_url"]
TRIP_DATA_FOLDER = config["download"]["trip_data_folder"]
ZONE_LOOKUP_URL = config["download"]["zone_lookup_url"]


def create_session() -> requests.Session:
    """
    Create HTTP session with retry mechanism.
    """

    retry_strategy = Retry(
        total=3,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)

    session = requests.Session()

    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def ensure_directory(directory: str) -> None:
    """
    Create directory if it does not exist.
    """

    Path(directory).mkdir(
        parents=True,
        exist_ok=True
    )


def download_monthly_file(
        year: int,
        month: int,
        output_dir: str
) -> str:
    """
    Download one monthly TLC parquet file.
    """

    ensure_directory(output_dir)

    filename = f"yellow_tripdata_{year}-{month:02d}.parquet"

    url = f"{BASE_URL}/{TRIP_DATA_FOLDER}/{filename}"

    local_path = Path(output_dir) / filename

    if local_path.exists():
        logger.info(
            f"{filename} already exists. Skipping."
        )
        return str(local_path)

    logger.info(
        f"Downloading {filename}"
    )

    session = create_session()

    response = session.get(
        url,
        stream=True,
        timeout=60
    )

    response.raise_for_status()

    with open(local_path, "wb") as file:
        for chunk in response.iter_content(
                chunk_size=8192
        ):
            file.write(chunk)

    logger.info(
        f"{filename} downloaded successfully."
    )

    return str(local_path)


def download_zone_lookup(
        output_dir: str
) -> str:
    """
    Download taxi zone lookup CSV.
    """

    ensure_directory(output_dir)

    local_path = Path(output_dir) / "taxi_zone_lookup.csv"

    if local_path.exists():
        logger.info(
            "taxi_zone_lookup.csv already exists. Skipping."
        )
        return str(local_path)

    logger.info(
        "Downloading taxi zone lookup file"
    )

    session = create_session()

    response = session.get(
        ZONE_LOOKUP_URL,
        timeout=60
    )

    response.raise_for_status()

    with open(
            local_path,
            "w",
            encoding="utf-8"
    ) as file:
        file.write(response.text)

    logger.info(
        "Taxi zone lookup downloaded successfully."
    )

    return str(local_path)