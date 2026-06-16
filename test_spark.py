import boto3
from dotenv import load_dotenv
load_dotenv()
import os

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

s3=boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

s3.upload_file(
    "test.txt",
    "nyc-taxi-analytics-dibya",
    "bronze/test.txt"
)