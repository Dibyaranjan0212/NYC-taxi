from pathlib import Path
import boto3
from botocore.exceptions import ClientError

from utils.config import load_config
from utils.logger import get_logger
import os
from dotenv import load_dotenv
load_dotenv()

logger = get_logger(__name__)

config = load_config()

BUCKET_NAME = config["aws"]["bucket_name"]
BRONZE_PREFIX = config["aws"]["bronze_prefix"]

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

s3_client = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key )


def upload_file_to_s3(
        local_file_path: str,
        s3_key: str
) -> None:
    """
    Upload file to S3 and verify upload.
    """

    logger.info(
        f"Uploading {local_file_path}"
    )

    try:

        s3_client.upload_file(
            local_file_path,
            BUCKET_NAME,
            s3_key
        )

        # Verify upload
        s3_client.head_object(
            Bucket=BUCKET_NAME,
            Key=s3_key
        )

        logger.info(
            f"Uploaded successfully: s3://{BUCKET_NAME}/{s3_key}"
        )

    except ClientError as e:

        logger.error(
            f"Failed to upload {local_file_path}"
        )

        raise e


def upload_bronze_file(
        local_file_path: str
) -> str:
    """
    Upload Bronze layer file to S3.

    CSV -> bronze/lookup/
    Parquet -> bronze/trip_data/
    """

    file_name = Path(
        local_file_path
    ).name

    if file_name.endswith(".csv"):

        s3_key = (
            f"{BRONZE_PREFIX}/lookup/{file_name}"
        )

    elif file_name.endswith(".parquet"):

        s3_key = (
            f"{BRONZE_PREFIX}/trip_data/{file_name}"
        )

    else:

        raise ValueError(
            f"Unsupported file type: {file_name}"
        )

    upload_file_to_s3(
        local_file_path,
        s3_key
    )

    return s3_key


def delete_local_file(
        local_file_path: str
) -> None:
    """
    Delete temporary local file after upload.
    """

    path = Path(local_file_path)

    if path.exists():
        path.unlink()
        logger.info(
            f"Deleted local file: {local_file_path}"
        )


def list_bronze_files() -> list:
    """
    Useful for testing and debugging.
    """

    response = s3_client.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix=BRONZE_PREFIX
    )

    files = []

    if "Contents" in response:

        for obj in response["Contents"]:

            files.append(
                obj["Key"]
            )

    return files