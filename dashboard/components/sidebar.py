"""
==========================================================
sidebar.py

Dashboard Sidebar

Author : Dibya Ranjan

Project :
NYC Taxi Analytics Dashboard
==========================================================
"""

import streamlit as st
from PIL import Image


# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar():

    """
    Render Dashboard Sidebar

    Returns
    -------
    dict
        Selected filters
    """

    with st.sidebar:

        # ==================================================
        # LOGO
        # ==================================================

        try:

            logo = Image.open("dashboard/assets/logo.png")

            st.image(
                logo,
                use_container_width=True
            )

        except Exception:

            st.markdown("# 🚕")


        # ==================================================
        # TITLE
        # ==================================================

        st.markdown(
            """
            <div style="text-align:center;">
                <h2 style="color:white;margin-bottom:0;">
                    NYC Taxi
                </h2>

                <p style="
                    color:#D6EAF8;
                    margin-top:0;
                    font-size:14px;
                ">
                    Analytics Dashboard
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


        st.divider()


        # ==================================================
        # FILTERS
        # ==================================================

        st.markdown("### 📅 Date")

        year = st.selectbox(

            "Year",

            [

                "2023"

            ],

            key="year_filter"

        )


        month = st.selectbox(

            "Month",

            [

                "All",

                "January",

                "February",

                "March",

                "April",

                "May",

                "June",

                "July",

                "August",

                "September",

                "October",

                "November",

                "December"

            ],

            key="month_filter"

        )


        st.markdown("### 🚕 Vendor")


        vendor = st.selectbox(

            "Vendor",

            [

                "All",

                "Vendor 1",

                "Vendor 2"

            ],

            key="vendor_filter"

        )


        st.markdown("### 💳 Payment")


        payment = st.selectbox(

            "Payment Type",

            [

                "All",

                "Credit Card",

                "Cash",

                "No Charge",

                "Dispute",

                "Unknown"

            ],

            key="payment_filter"

        )


        st.markdown("### 📍 Borough")


        borough = st.selectbox(

            "Borough",

            [

                "All",

                "Manhattan",

                "Queens",

                "Brooklyn",

                "Bronx",

                "Staten Island",

                "Unknown"

            ],

            key="borough_filter"

        )


        st.divider()


        # ==================================================
        # PROJECT INFO
        # ==================================================

        st.markdown("### ☁ Technology")

        st.markdown("""
- Snowflake
- AWS S3
- Streamlit
- Plotly
- Python
""")

        st.divider()


        # ==================================================
        # FOOTER
        # ==================================================

        st.caption(
            "NYC Taxi Analytics Dashboard"
        )

        st.caption(
            "Version 1.0"
        )


    return {

        "year": year,

        "month": month,

        "vendor": vendor,

        "payment": payment,

        "borough": borough

    }