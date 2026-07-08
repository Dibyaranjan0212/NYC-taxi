"""
==========================================================
kpi_cards.py

Executive KPI Cards

Author : Dibya Ranjan

Project :
NYC Taxi Analytics Dashboard
==========================================================
"""

import streamlit as st

from utils.queries import get_kpi_summary
from utils.formatter import (
    format_number,
    format_currency,
    format_distance,
    format_duration
)


# ==========================================================
# KPI CARD
# ==========================================================

def _kpi_card(
    icon: str,
    title: str,
    value: str
):

    st.markdown(
    f"""
<div class="kpi-card">

    <div class="kpi-icon">{icon}</div>

    <div class="kpi-title">{title}</div>

    <div class="kpi-value">{value}</div>

</div>
""",
    unsafe_allow_html=True
)


# ==========================================================
# KPI SECTION
# ==========================================================

def render_kpi_cards(kpi_df):

    """
    Render Executive KPI Cards
    """

    if kpi_df.empty:

        st.warning("No KPI data available.")

        return

    row = kpi_df.iloc[0]

    st.markdown(
        """
<div class="section-title">

📊 Executive Summary

</div>
""",
        unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:

        _kpi_card(

            "🚕",

            "Total Trips",

            format_number(

                row["TOTAL_TRIPS"]

            )

        )

    with col2:

        _kpi_card(

            "💰",

            "Total Revenue",

            format_currency(

                row["TOTAL_REVENUE"]

            )

        )

    with col3:

        _kpi_card(

            "💵",

            "Average Fare",

            format_currency(

                row["AVG_FARE"]

            )

        )

    with col4:

        _kpi_card(

            "📍",

            "Average Distance",

            format_distance(

                row["AVG_DISTANCE"]

            )

        )

    with col5:

        _kpi_card(

            "⏱",

            "Average Duration",

            format_duration(

                row["AVG_TRIP_DURATION"]

            )

        )

    with col6:

        _kpi_card(

            "💳",

            "Average Tip",

            format_currency(

                row["AVG_TIP"]

            )

        )

    st.write("")