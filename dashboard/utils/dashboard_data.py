"""
==========================================================
dashboard_data.py

Dashboard Data Loader

Author : Dibya Ranjan

Project :
NYC Taxi Analytics Dashboard
==========================================================
"""

import streamlit as st

from utils.queries import (

    get_kpi_summary,

    get_monthly_revenue,

    get_monthly_trips,

    get_payment_distribution,

    get_vendor_performance,

    get_top_pickup_locations,

    get_borough_revenue

)


# ==========================================================
# LOAD DASHBOARD DATA
# ==========================================================

@st.cache_data(show_spinner=False)

def load_dashboard_data():

    """
    Load all dashboard datasets.

    Returns
    -------
    dict
    """

    dashboard_data = {

        "kpi": get_kpi_summary(),

        "monthly_revenue": get_monthly_revenue(),

        "monthly_trips": get_monthly_trips(),

        "payment_distribution": get_payment_distribution(),

        "vendor_performance": get_vendor_performance(),

        "pickup_locations": get_top_pickup_locations(),

        "borough_revenue": get_borough_revenue()

    }

    return dashboard_data


# ==========================================================
# DATA VALIDATION
# ==========================================================

def validate_dashboard_data(data: dict):

    """
    Ensure every dataframe exists.
    """

    required_keys = [

        "kpi",

        "monthly_revenue",

        "monthly_trips",

        "payment_distribution",

        "vendor_performance",

        "pickup_locations",

        "borough_revenue"

    ]

    for key in required_keys:

        if key not in data:

            raise ValueError(

                f"{key} not found."

            )

        if data[key].empty:

            raise ValueError(

                f"{key} dataframe is empty."

            )

    return True