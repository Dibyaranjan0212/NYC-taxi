"""
==========================================================
payment_section.py

Payment & Vendor Analysis

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
    apply_donut_style,
    apply_horizontal_bar_style
)

from config.theme import (
    DONUT_COLORS,
    CHART_PALETTE
)


# ==========================================================
# PAYMENT DISTRIBUTION CHART
# ==========================================================

def build_payment_chart(payment_df):

    fig = px.pie(

        payment_df,

        names="PAYMENT_NAME",

        values="TOTAL_TRIPS",

        hole=0.68,

        color="PAYMENT_NAME",

        color_discrete_sequence=DONUT_COLORS

    )

    apply_donut_style(fig)

    apply_chart_theme(fig)

    fig.update_layout(

        showlegend=True,

        legend=dict(

            orientation="v",

            y=0.95,

            x=1.02,

            font=dict(size=11)

        )

    )

    fig.update_traces(

        hovertemplate=

        "<b>%{label}</b><br>"

        "Trips : %{value:,.0f}<br>"

        "Share : %{percent}"

        "<extra></extra>"

    )

    return fig


# ==========================================================
# VENDOR PERFORMANCE CHART
# ==========================================================

def build_vendor_chart(vendor_df):

    fig = px.bar(

        vendor_df,

        y="VENDOR_NAME",

        x="TOTAL_REVENUE",

        orientation="h",

        color="TOTAL_REVENUE",

        color_continuous_scale=CHART_PALETTE

    )

    apply_horizontal_bar_style(fig)

    apply_chart_theme(

        fig,

        y_prefix="$",

        y_format="~s"

    )

    fig.update_layout(

        coloraxis_showscale=False,

        showlegend=False

    )

    fig.update_traces(

        hovertemplate=

        "<b>%{y}</b><br>"

        "Revenue : $%{x:,.0f}"

        "<extra></extra>"

    )

    return fig


# ==========================================================
# RENDER SECTION
# ==========================================================

def render_payment_section(

    payment_df,

    vendor_df

):

    left, right = st.columns(2)

    with left:

        with ChartCard(

            "Payment Distribution",

            "💳"

        ) as card:

            payment_chart = build_payment_chart(

                payment_df

            )

            card.plot(

                payment_chart

            )

    with right:

        with ChartCard(

            "Vendor Performance",

            "📊"

        ) as card:

            vendor_chart = build_vendor_chart(

                vendor_df

            )

            card.plot(

                vendor_chart

            )