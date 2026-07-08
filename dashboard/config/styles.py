"""
==========================================================
styles.py

Global Dashboard Styles

Author : Dibya Ranjan

Project :
NYC Taxi Analytics Dashboard
==========================================================
"""


import streamlit as st


# ==========================================================
# LOAD GLOBAL CSS
# ==========================================================

def load_css():

    st.markdown("""

<style>

/* ==========================================================
PAGE
========================================================== */

html,
body,
[class*="css"]{

    font-family:'Segoe UI',sans-serif;

}

.stApp{

    background:#F4F7FB;

}

/* Remove extra white space */

.block-container{

    padding-top:.6rem;

    padding-left:1.3rem;

    padding-right:1.3rem;

    padding-bottom:.5rem;

    max-width:100%;

}

/* ==========================================================
SIDEBAR
========================================================== */

section[data-testid="stSidebar"]{

    background:#0B3C6D;

    border-right:none;

    width:280px;

}

section[data-testid="stSidebar"] *{

    color:white;

}

section[data-testid="stSidebar"] h1{

    color:white;

}

section[data-testid="stSidebar"] h2{

    color:white;

}

section[data-testid="stSidebar"] h3{

    color:white;

}

section[data-testid="stSidebar"] label{

    color:white;

    font-weight:600;

}

section[data-testid="stSidebar"] .stSelectbox{

    margin-bottom:12px;

}

section[data-testid="stSidebar"] div[data-baseweb="select"]{

    background:white;

    border-radius:10px;

}

section[data-testid="stSidebar"] svg{

    color:#0B3C6D;

}

/* ==========================================================
HEADER
========================================================== */

.dashboard-header{

    background:linear-gradient(
        90deg,
        #0B3C6D,
        #1565C0
    );

    border-radius:18px;

    padding:18px 28px;

    margin-bottom:14px;

    box-shadow:0px 4px 12px rgba(0,0,0,.12);

}

.dashboard-title{

    color:white;

    font-size:30px;

    font-weight:700;

    margin:0;

}

.dashboard-subtitle{

    color:#D6EAF8;

    font-size:14px;

    margin-top:4px;

}

/* ==========================================================
SECTION TITLE
========================================================== */

.section-title{

    color:#12355B;

    font-size:20px;

    font-weight:700;

    margin-bottom:8px;

}

/* ==========================================================
KPI CARD
========================================================== */

.kpi-card{

    background:white;

    border-radius:18px;

    border-left:6px solid #1565C0;

    padding:16px;

    height:108px;

    box-shadow:0px 3px 10px rgba(0,0,0,.08);

    transition:.25s;

}

.kpi-card:hover{

    transform:translateY(-3px);

    box-shadow:0px 8px 18px rgba(0,0,0,.12);

}

.kpi-icon{

    font-size:28px;

    margin-bottom:6px;

}

.kpi-value{

    font-size:30px;

    font-weight:700;

    color:#0B3C6D;

    margin-top:6px;

}

.kpi-title{

    display:block;

    font-size:14px;

    font-weight:600;

    color:#4B5563;

    margin-top:8px;

    line-height:1.2;

}
                
/* ==========================================================
CHART CARD
========================================================== */

.chart-card{

    background:white;

    border-radius:18px;

    overflow:hidden;

    border:1px solid #E5EAF2;

    box-shadow:0px 3px 10px rgba(0,0,0,.08);

    margin-bottom:12px;

}

.chart-header{

    background:linear-gradient(
        90deg,
        #0B3C6D,
        #1565C0
    );

    padding:10px 16px;

}

.chart-title{

    color:white;

    font-size:17px;

    font-weight:600;

}

.chart-body{

    padding:8px;

}

/* ==========================================================
SUMMARY CARD
========================================================== */

.summary-card{

    background:white;

    border-radius:15px;

    padding:10px;

    text-align:center;

    border:1px solid #E5EAF2;

    box-shadow:0px 2px 8px rgba(0,0,0,.08);

}

.summary-value{

    font-size:22px;

    color:#0B3C6D;

    font-weight:700;

}

.summary-label{

    font-size:12px;

    color:#6B7280;

}

/* ==========================================================
BUTTONS
========================================================== */

.stButton>button{

    background:#1565C0;

    color:white;

    border:none;

    border-radius:10px;

}

.stButton>button:hover{

    background:#0B3C6D;

}

/* ==========================================================
REMOVE STREAMLIT ELEMENTS
========================================================== */

#MainMenu{

    visibility:hidden;

}

footer{

    visibility:hidden;

}

header{

    visibility:hidden;

}

/* ==========================================================
SCROLLBAR
========================================================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#B8C7DB;

    border-radius:10px;

}

/* ==========================================================
PLOTLY
========================================================== */

.js-plotly-plot{

    border-radius:16px;

}

/* ==========================================================
SCREEN HEIGHT
========================================================== */

/* Optimized so dashboard fits on one 1920×1080 screen */

div[data-testid="stVerticalBlock"]{

    gap:.65rem;

}

</style>

""",

unsafe_allow_html=True)