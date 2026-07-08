"""
==========================================================
revenue_section.py

Revenue & Trip Analysis

Author : Dibya Ranjan

Project :
NYC Taxi Analytics Dashboard
==========================================================
"""

import streamlit as st
import plotly.express as px

from components.chart_card import ChartCard

from components.plotly_theme import (
    apply_chart_theme,
    apply_line_style,
    apply_bar_style
)

from config.theme import (
    CHART_PRIMARY,
    CHART_SECONDARY
)


# ==========================================================
# REVENUE CHART
# ==========================================================

def build_revenue_chart(revenue_df):

    fig = px.line(

        revenue_df,

        x="MONTH_NAME",

        y="TOTAL_REVENUE",

        markers=True

    )

    apply_line_style(

        fig,

        color=CHART_PRIMARY

    )

    apply_chart_theme(

        fig,

        y_prefix="$",

        y_format="~s"

    )

    fig.update_traces(

        hovertemplate=

        "<b>%{x}</b><br>"

        "Revenue : $%{y:,.0f}"

        "<extra></extra>"

    )

    return fig


# ==========================================================
# MONTHLY TRIPS
# ==========================================================

def build_trip_chart(trip_df):

    fig = px.bar(

        trip_df,

        x="MONTH_NAME",

        y="TOTAL_TRIPS",

        color_discrete_sequence=[

            CHART_SECONDARY

        ]

    )

    apply_bar_style(

        fig,

        color=CHART_SECONDARY

    )

    apply_chart_theme(

        fig,

        y_format="~s"

    )

    fig.update_traces(

        hovertemplate=

        "<b>%{x}</b><br>"

        "Trips : %{y:,.0f}"

        "<extra></extra>"

    )

    return fig


# ==========================================================
# RENDER
# ==========================================================

def render_revenue_section(

    revenue_df,

    trip_df

):

    left, right = st.columns(2)

    with left:

        with ChartCard(

            "Revenue Trend",

            "📈"

        ) as card:

            card.plot(

                build_revenue_chart(

                    revenue_df

                )

            )

    with right:

        with ChartCard(

            "Monthly Trips",

            "🚕"

        ) as card:

            card.plot(

                build_trip_chart(

                    trip_df

                )

            )