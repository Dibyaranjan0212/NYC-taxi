"""
helper.py

Helper functions for Streamlit Dashboard.

Author : Dibya Ranjan
Project : NYC Taxi Analytics Dashboard
"""

import streamlit as st


# ==========================================================
# PAGE CONFIG
# ==========================================================

def set_page_config():

    st.set_page_config(

        page_title="NYC Taxi Analytics",

        page_icon="🚕",

        layout="wide",

        initial_sidebar_state="expanded"

    )


# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    st.markdown(
        """
        <style>

        .main{
            padding-top:1rem;
        }

        div[data-testid="metric-container"]{

            background-color:#FFFFFF;

            border:1px solid #E5E7EB;

            border-radius:12px;

            padding:15px;

            box-shadow:0px 2px 8px rgba(0,0,0,.08);

        }

        h1{
            color:#1F4E79;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# NUMBER FORMAT
# ==========================================================
def format_number(value):

    units = [
        (1_000_000_000, "B"),
        (1_000_000, "M"),
        (1_000, "K")
    ]

    for divisor, suffix in units:
        if value >= divisor:
            return f"{value/divisor:.1f}{suffix}"

    return f"{value:.0f}"


def format_currency(value):

    units = [
        (1_000_000_000, "B"),
        (1_000_000, "M"),
        (1_000, "K")
    ]

    for divisor, suffix in units:
        if value >= divisor:
            return f"${value/divisor:.1f}{suffix}"

    return f"${value:.2f}"

# ==========================================================
# DISTANCE FORMAT
# ==========================================================

def format_distance(value):

    return f"{value:.2f} mi"


# ==========================================================
# DURATION FORMAT
# ==========================================================

def format_duration(value):

    return f"{value:.1f} min"