"""
app.py

NYC Taxi Analytics Dashboard

Author : Dibya Ranjan
"""

import streamlit as st

from utils.helper import (
    set_page_config,
    load_css,
    format_number,
    format_currency,
    format_distance,
    format_duration
)

from utils.queries import (
    get_kpi_summary
)

# ----------------------------------------------------------
# PAGE SETUP
# ----------------------------------------------------------

set_page_config()

load_css()

# ----------------------------------------------------------
# TITLE
# ----------------------------------------------------------

st.title("🚕 NYC Taxi Analytics Dashboard")

st.caption(
    "Built with Python • Snowflake • AWS S3 • Streamlit"
)

st.divider()

# ----------------------------------------------------------
# LOAD KPI DATA
# ----------------------------------------------------------

kpi = get_kpi_summary()

row = kpi.iloc[0]

# ----------------------------------------------------------
# KPI CARDS
# ----------------------------------------------------------

col1,col2,col3,col4,col5,col6 = st.columns(6)

with col1:

    st.metric(
        "Trips",
        format_number(row["TOTAL_TRIPS"])
    )

with col2:

    st.metric(
        "Revenue",
        format_currency(row["TOTAL_REVENUE"])
    )

with col3:

    st.metric(
        "Avg Fare",
        format_currency(row["AVG_FARE"])
    )

with col4:

    st.metric(
        "Avg Distance",
        format_distance(row["AVG_DISTANCE"])
    )

with col5:

    st.metric(
        "Avg Duration",
        format_duration(row["AVG_TRIP_DURATION"])
    )

with col6:

    st.metric(
        "Avg Tip",
        format_currency(row["AVG_TIP"])
    )