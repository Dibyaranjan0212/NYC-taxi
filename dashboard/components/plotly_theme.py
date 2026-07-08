"""
==========================================================
plotly_theme.py

Reusable Plotly Theme

Author : Dibya Ranjan

Project :
NYC Taxi Analytics Dashboard
==========================================================
"""

import plotly.graph_objects as go

from config.theme import (
    COMMON_LAYOUT,
    GRID,
    TEXT_PRIMARY,
    CHART_PRIMARY
)


# ==========================================================
# APPLY COMMON DASHBOARD THEME
# ==========================================================

def apply_chart_theme(
    fig: go.Figure,
    y_prefix: str = "",
    y_format: str = "",
    show_x_grid: bool = False,
    show_y_grid: bool = True,
):
    """
    Apply common styling to every Plotly chart.
    """

    fig.update_layout(**COMMON_LAYOUT)

    fig.update_xaxes(

        showgrid=show_x_grid,

        gridcolor=GRID,

        zeroline=False,

        linecolor="#D9E2EC",

        tickfont=dict(

            color=TEXT_PRIMARY,

            size=11

        )

    )

    fig.update_yaxes(

        showgrid=show_y_grid,

        gridcolor=GRID,

        zeroline=False,

        linecolor="#D9E2EC",

        tickprefix=y_prefix,

        tickformat=y_format,

        tickfont=dict(

            color=TEXT_PRIMARY,

            size=11

        )

    )

    return fig


# ==========================================================
# LINE CHART STYLE
# ==========================================================

def apply_line_style(
    fig: go.Figure,
    color: str = CHART_PRIMARY
):

    fig.update_traces(

        line=dict(

            color=color,

            width=4

        ),

        marker=dict(

            size=8,

            color=color,

            line=dict(

                color="white",

                width=2

            )

        )

    )

    return fig


# ==========================================================
# BAR CHART STYLE
# ==========================================================

def apply_bar_style(
    fig: go.Figure,
    color: str = CHART_PRIMARY
):

    fig.update_traces(

        marker=dict(

            color=color,

            line=dict(

                color="white",

                width=1

            )

        )

    )

    return fig


# ==========================================================
# DONUT STYLE
# ==========================================================

def apply_donut_style(
    fig: go.Figure
):

    fig.update_traces(

        textposition="inside",

        textinfo="percent",

        marker=dict(

            line=dict(

                color="white",

                width=2

            )

        )

    )

    return fig


# ==========================================================
# HORIZONTAL BAR STYLE
# ==========================================================

def apply_horizontal_bar_style(
    fig: go.Figure
):

    fig.update_traces(

        marker_line_color="white",

        marker_line_width=1

    )

    return fig