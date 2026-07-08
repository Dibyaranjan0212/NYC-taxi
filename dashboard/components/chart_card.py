"""
==========================================================
chart_card.py

Reusable Chart Card Component

Author : Dibya Ranjan

Project :
NYC Taxi Analytics Dashboard
==========================================================
"""

import streamlit as st

from config.theme import PLOTLY_CONFIG


# ==========================================================
# CHART CARD
# ==========================================================

class ChartCard:
    """
    Reusable wrapper for Plotly charts.

    Example
    -------
    with ChartCard("Revenue Trend", "📈"):
        st.plotly_chart(...)
    """

    def __init__(self, title: str, icon: str):

        self.title = title
        self.icon = icon

    def __enter__(self):

        st.markdown(
            f"""
<div class="chart-card">

<div class="chart-header">

<span class="chart-title">

{self.icon} {self.title}

</span>

</div>

<div class="chart-body">
""",
            unsafe_allow_html=True,
        )

        return self

    def plot(self, fig):

        st.plotly_chart(
            fig,
            use_container_width=True,
            config=PLOTLY_CONFIG
        )

    def __exit__(self, exc_type, exc_val, exc_tb):

        st.markdown(
            """
</div>

</div>
""",
            unsafe_allow_html=True,
        )