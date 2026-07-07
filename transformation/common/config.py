import os
from dotenv import load_dotenv
load_dotenv()

ENV = os.getenv("ENV", "local")

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
AWS_BUCKET = os.getenv("AWS_BUCKET")

PROCESSING_YEAR = int(
    os.getenv("PROCESSING_YEAR", "2023")
)

BRONZE_PATH = (f"s3://{AWS_BUCKET}/bronze/trip_data/")

SILVER_PATH = (f"s3://{AWS_BUCKET}/silver/trips/")

GOLD_PATH = (f"s3://{AWS_BUCKET}/gold")

LOOKUP_PATH = "s3://nyc-taxi-analytics-dibya/bronze/lookup/taxi_zone_lookup.csv"

# ------------------------------------------------------------------
# Validate Environment Variables
# ------------------------------------------------------------------

_REQUIRED_ENV_VARS = [
    "AWS_ACCESS_KEY",
    "AWS_SECRET_KEY",
    "AWS_REGION",
    "AWS_BUCKET",
]

_missing = [
    var
    for var in _REQUIRED_ENV_VARS
    if not os.getenv(var)
]

if _missing:
    raise ValueError(
        f"Missing environment variables: {', '.join(_missing)}"
    )


