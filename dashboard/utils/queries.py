"""
queries.py

All Snowflake queries for the dashboard.

Author : Dibya Ranjan
Project : NYC Taxi Analytics Dashboard
"""

import pandas as pd

from utils.connection import get_connection


def execute_query(query: str) -> pd.DataFrame:
    """
    Execute a SQL query and return a Pandas DataFrame.
    """

    conn = get_connection()

    try:
        df = pd.read_sql(query, conn)

    finally:
        conn.close()

    return df


# ==========================================================
# KPI SUMMARY
# ==========================================================

def get_kpi_summary():

    query = """
    SELECT *
    FROM VW_KPI_SUMMARY;
    """

    return execute_query(query)


# ==========================================================
# MONTHLY REVENUE
# ==========================================================

def get_monthly_revenue():

    query = """
    SELECT *
    FROM VW_MONTHLY_REVENUE;
    """

    return execute_query(query)


# ==========================================================
# MONTHLY TRIPS
# ==========================================================

def get_monthly_trips():

    query = """
    SELECT *
    FROM VW_MONTHLY_TRIPS;
    """

    return execute_query(query)


# ==========================================================
# PAYMENT DISTRIBUTION
# ==========================================================

def get_payment_distribution():

    query = """
    SELECT *
    FROM VW_PAYMENT_DISTRIBUTION;
    """

    return execute_query(query)


# ==========================================================
# VENDOR PERFORMANCE
# ==========================================================

def get_vendor_performance():

    query = """
    SELECT *
    FROM VW_VENDOR_PERFORMANCE;
    """

    return execute_query(query)


# ==========================================================
# TOP PICKUP LOCATIONS
# ==========================================================

def get_top_pickup_locations():

    query = """
    SELECT *
    FROM VW_TOP_PICKUP_LOCATIONS;
    """

    return execute_query(query)


# ==========================================================
# BOROUGH REVENUE
# ==========================================================

def get_borough_revenue():

    query = """
    SELECT *
    FROM VW_BOROUGH_REVENUE;
    """

    return execute_query(query)


# ==========================================================
# DAILY TREND
# ==========================================================

def get_daily_trend():

    query = """
    SELECT *
    FROM VW_DAILY_TREND;
    """

    return execute_query(query)