"""
Snowflake Connection

Author : Dibya Ranjan
Project : NYC Taxi Analytics Dashboard
"""

import os

import snowflake.connector

from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """
    Create and return a Snowflake connection.
    """

    connection = snowflake.connector.connect(

        account=os.getenv("account"),

        user=os.getenv("user"),

        password=os.getenv("password"),

        warehouse=os.getenv("warehouse"),

        database=os.getenv("database"),

        schema=os.getenv("schema")

    )

    return connection
