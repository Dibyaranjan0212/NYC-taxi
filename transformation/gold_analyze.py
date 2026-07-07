"""
Inspect complete Gold layer in S3
"""

import boto3
from collections import defaultdict

from common.config import (
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
    AWS_REGION,
)

BUCKET = "nyc-taxi-analytics-dibya"
PREFIX = "gold/"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

print("=" * 100)
print("READING GOLD FOLDER")
print("=" * 100)

paginator = s3.get_paginator("list_objects_v2")

objects = []

for page in paginator.paginate(
    Bucket=BUCKET,
    Prefix=PREFIX,
):
    objects.extend(page.get("Contents", []))

print(f"\nTotal Objects : {len(objects)}")

if not objects:
    print("\nNo objects found.")
    exit()

# ==============================================================================
# Folder Structure
# ==============================================================================

tree = defaultdict(list)

for obj in objects:

    key = obj["Key"]

    parts = key.split("/")

    for i in range(len(parts) - 1):

        parent = "/".join(parts[:i + 1])

        child = parts[i + 1]

        if child not in tree[parent]:
            tree[parent].append(child)


print("\n" + "=" * 100)
print("FOLDER STRUCTURE")
print("=" * 100)


def print_tree(node, indent=""):

    children = sorted(tree[node])

    for child in children:

        current = f"{node}/{child}" if node else child

        if current in tree:

            print(indent + "📁 " + child)

            print_tree(current, indent + "    ")

        else:

            print(indent + "📄 " + child)


print("📁 gold")

print_tree("gold")

# ==============================================================================
# Object Details
# ==============================================================================

print("\n" + "=" * 100)
print("OBJECT DETAILS")
print("=" * 100)

total_size = 0

for obj in objects:

    size_mb = obj["Size"] / 1024 / 1024

    total_size += obj["Size"]

    print(f"{obj['Key']}")
    print(f"    Size : {size_mb:.2f} MB")
    print(f"    Last Modified : {obj['LastModified']}")
    print()

# ==============================================================================
# Summary
# ==============================================================================

print("=" * 100)
print("SUMMARY")
print("=" * 100)

print(f"Total Objects : {len(objects)}")
print(f"Total Size    : {total_size / 1024 / 1024:.2f} MB")

# ==============================================================================
# Count by Folder
# ==============================================================================

print("\n" + "=" * 100)
print("OBJECT COUNT PER FOLDER")
print("=" * 100)

folder_counts = defaultdict(int)

for obj in objects:

    folder = "/".join(obj["Key"].split("/")[:-1])

    folder_counts[folder] += 1

for folder in sorted(folder_counts):

    print(f"{folder:<70} {folder_counts[folder]}")

# ==============================================================================
# Parquet Files
# ==============================================================================

print("\n" + "=" * 100)
print("PARQUET FILES")
print("=" * 100)

count = 0

for obj in objects:

    if obj["Key"].endswith(".parquet"):

        count += 1

        print(obj["Key"])

print(f"\nTotal Parquet Files : {count}")