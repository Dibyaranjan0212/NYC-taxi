"""
==========================================================
location_section.py

Location Analysis

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
    apply_horizontal_bar_style,
    apply_bar_style
)

from config.theme import (
    CHART_PRIMARY,
    CHART_PALETTE
)


# ==========================================================
# PICKUP LOCATION
# ==========================================================

def build_pickup_chart(pickup_df):

    df = pickup_df.head(10).copy()

    fig = px.bar(

        df,

        x="TOTAL_TRIPS",

        y="ZONE",

        orientation="h",

        color="TOTAL_TRIPS",

        color_continuous_scale=CHART_PALETTE

    )

    apply_horizontal_bar_style(fig)

    apply_chart_theme(

        fig,

        y_prefix="",

        y_format="~s"

    )

    fig.update_layout(

        coloraxis_showscale=False

    )

    fig.update_yaxes(

        categoryorder="total ascending"

    )

    fig.update_traces(

        hovertemplate=

        "<b>%{y}</b><br>"

        "Trips : %{x:,.0f}"

        "<extra></extra>"

    )

    return fig


# ==========================================================
# BOROUGH REVENUE
# ==========================================================

def build_borough_chart(borough_df):

    fig = px.bar(

        borough_df,

        x="BOROUGH",

        y="TOTAL_REVENUE",

        color="BOROUGH",

        color_discrete_sequence=[

            CHART_PRIMARY,

            "#1565C0",

            "#2F80ED",

            "#64B5F6",

            "#BBDEFB"

        ]

    )

    apply_bar_style(fig)

    apply_chart_theme(

        fig,

        y_prefix="$",

        y_format="~s"

    )

    fig.update_layout(

        showlegend=False

    )

    fig.update_traces(

        hovertemplate=

        "<b>%{x}</b><br>"

        "Revenue : $%{y:,.0f}"

        "<extra></extra>"

    )

    return fig


# ==========================================================
# RENDER
# ==========================================================

def render_location_section(

    pickup_df,

    borough_df

):

    pickup_chart = build_pickup_chart(

        pickup_df

    )

    borough_chart = build_borough_chart(

        borough_df

    )

    left, right = st.columns(2)

    with left:

        with ChartCard(

            "Top Pickup Locations",

            "📍"

        ) as card:

            card.plot(

                pickup_chart

            )

    with right:

        with ChartCard(

            "Revenue by Borough",

            "🏙"

        ) as card:

            card.plot(

                borough_chart

            )