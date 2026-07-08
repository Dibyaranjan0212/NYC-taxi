"""
==========================================================
app.py

NYC Taxi Analytics Dashboard

Author : Dibya Ranjan

Project :
NYC Taxi Data Engineering Pipeline

Dashboard :
Snowflake + Streamlit + Plotly
==========================================================
"""

# ==========================================================
# IMPORTS
# ==========================================================

import streamlit as st

from config.styles import load_css

from components.sidebar import render_sidebar
from components.header import render_header
from components.kpi_cards import render_kpi_cards
from components.revenue_section import render_revenue_section
from components.payment_section import render_payment_section
from components.location_section import render_location_section

from utils.dashboard_data import (
    load_dashboard_data,
    validate_dashboard_data
)

from utils.helper import set_page_config


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

set_page_config()

load_css()


# ==========================================================
# LOAD DASHBOARD DATA
# ==========================================================

dashboard_data = load_dashboard_data()

validate_dashboard_data(dashboard_data)


# ==========================================================
# SIDEBAR
# ==========================================================

filters = render_sidebar()

# (Reserved for future filtering)
# Currently filters are displayed only.
# Later we can apply them to dashboard_data.


# ==========================================================
# HEADER
# ==========================================================

render_header()


# ==========================================================
# KPI SECTION
# ==========================================================

render_kpi_cards(

    dashboard_data["kpi"]

)


# ==========================================================
# REVENUE SECTION
# ==========================================================

render_revenue_section(

    dashboard_data["monthly_revenue"],

    dashboard_data["monthly_trips"]

)


# ==========================================================
# PAYMENT SECTION
# ==========================================================

render_payment_section(

    dashboard_data["payment_distribution"],

    dashboard_data["vendor_performance"]

)


# ==========================================================
# LOCATION SECTION
# ==========================================================

render_location_section(

    dashboard_data["pickup_locations"],

    dashboard_data["borough_revenue"]

)