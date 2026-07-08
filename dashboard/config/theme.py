"""
==========================================================
theme.py

Central Theme Configuration

Author : Dibya Ranjan

Project :
NYC Taxi Analytics Dashboard
==========================================================
"""

# ==========================================================
# BRAND COLORS
# ==========================================================

PRIMARY_BLUE = "#0B3C6D"

SECONDARY_BLUE = "#1565C0"

ACCENT_BLUE = "#2F80ED"

LIGHT_BLUE = "#EAF3FF"

BACKGROUND = "#F4F7FB"

CARD_BACKGROUND = "#FFFFFF"

TEXT_PRIMARY = "#1F2937"

TEXT_SECONDARY = "#6B7280"

BORDER = "#E5EAF2"

GRID = "#EEF2F7"

SUCCESS = "#22C55E"

WARNING = "#F59E0B"

ERROR = "#EF4444"

WHITE = "#FFFFFF"


# ==========================================================
# FONT
# ==========================================================

FONT_FAMILY = "Segoe UI"

TITLE_SIZE = 28

SUBTITLE_SIZE = 15

SECTION_TITLE = 18

BODY_TEXT = 13

SMALL_TEXT = 11


# ==========================================================
# DASHBOARD DIMENSIONS
# ==========================================================

PAGE_PADDING = 1

HEADER_HEIGHT = 90

KPI_HEIGHT = 110

CHART_HEIGHT = 245

CHART_PADDING = 10

SIDEBAR_WIDTH = 280


# ==========================================================
# CARD STYLING
# ==========================================================

CARD_RADIUS = 18

KPI_RADIUS = 18

BUTTON_RADIUS = 10

CARD_BORDER = 1

CARD_SHADOW = (
    "0px 4px 12px rgba(0,0,0,.08)"
)

HOVER_SHADOW = (
    "0px 8px 18px rgba(0,0,0,.12)"
)


# ==========================================================
# CHART COLORS
# ==========================================================

CHART_PRIMARY = PRIMARY_BLUE

CHART_SECONDARY = ACCENT_BLUE

CHART_LIGHT = LIGHT_BLUE

CHART_PALETTE = [

    PRIMARY_BLUE,

    SECONDARY_BLUE,

    ACCENT_BLUE,

    "#5DADE2",

    "#89CFF0",

    "#CFE8FF"

]


# ==========================================================
# DONUT COLORS
# ==========================================================

DONUT_COLORS = [

    "#0B3C6D",

    "#1565C0",

    "#2F80ED",

    "#64B5F6",

    "#BBDEFB"

]


# ==========================================================
# PLOTLY CONFIG
# ==========================================================

PLOTLY_CONFIG = {

    "displayModeBar": False,

    "displaylogo": False,

    "responsive": True,

    "scrollZoom": False,

    "doubleClick": False,

    "modeBarButtonsToRemove": [

        "zoom",

        "pan",

        "select",

        "lasso2d",

        "zoomIn",

        "zoomOut",

        "autoScale",

        "resetScale"

    ]

}


# ==========================================================
# COMMON PLOTLY LAYOUT
# ==========================================================

COMMON_LAYOUT = {

    "paper_bgcolor": CARD_BACKGROUND,

    "plot_bgcolor": CARD_BACKGROUND,

    "font": {

        "family": FONT_FAMILY,

        "size": BODY_TEXT,

        "color": TEXT_PRIMARY

    },

    "margin": {

        "l": 15,

        "r": 15,

        "t": 40,

        "b": 15

    },

    "height": CHART_HEIGHT,

    "showlegend": True,

    "hovermode": "x unified"

}