"""
==========================================================
header.py

Dashboard Header Component

Author : Dibya Ranjan

Project :
NYC Taxi Analytics Dashboard
==========================================================
"""

from datetime import datetime

import streamlit as st


# ==========================================================
# HEADER
# ==========================================================

def render_header():

    """
    Render dashboard header.
    """

    current_time = datetime.now().strftime("%d %b %Y • %I:%M %p")

    col1, col2 = st.columns([4, 1])

    # ======================================================
    # LEFT
    # ======================================================

    with col1:

        st.markdown(
            f"""
<div class="dashboard-header">

<div class="dashboard-title">

🚕 NYC Taxi Analytics Dashboard

</div>

<div class="dashboard-subtitle">

Executive Business Intelligence Dashboard

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    # ======================================================
    # RIGHT
    # ======================================================

    with col2:

        st.markdown(
            f"""
<div class="summary-card">

<div class="summary-value">

🟢 LIVE

</div>

<div class="summary-label">

Snowflake Connected

</div>

<hr style="margin:8px 0;">

<div style="font-size:11px;color:#6B7280;">

Updated

<br>

<b>{current_time}</b>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    st.write("")