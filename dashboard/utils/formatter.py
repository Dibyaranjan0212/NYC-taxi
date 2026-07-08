"""
==========================================================
formatter.py

Formatting Utility Functions

Author : Dibya Ranjan

Project :
NYC Taxi Analytics Dashboard
==========================================================
"""


# ==========================================================
# NUMBER FORMATTER
# ==========================================================

def format_number(value):

    """
    Convert large numbers into readable format.

    Examples
    --------
    1250        -> 1.3K
    1250000     -> 1.3M
    2500000000  -> 2.5B
    """

    if value is None:
        return "-"

    value = float(value)

    if abs(value) >= 1_000_000_000:
        return f"{value/1_000_000_000:.1f}B"

    if abs(value) >= 1_000_000:
        return f"{value/1_000_000:.1f}M"

    if abs(value) >= 1_000:
        return f"{value/1_000:.1f}K"

    return f"{value:,.0f}"


# ==========================================================
# CURRENCY FORMATTER
# ==========================================================

def format_currency(value):

    """
    Examples

    2500 -> $2.5K

    1500000 -> $1.5M
    """

    if value is None:
        return "-"

    value = float(value)

    if abs(value) >= 1_000_000_000:
        return f"${value/1_000_000_000:.1f}B"

    if abs(value) >= 1_000_000:
        return f"${value/1_000_000:.1f}M"

    if abs(value) >= 1_000:
        return f"${value/1_000:.1f}K"

    return f"${value:,.2f}"


# ==========================================================
# DISTANCE
# ==========================================================

def format_distance(value):

    if value is None:
        return "-"

    return f"{float(value):.2f} mi"


# ==========================================================
# DURATION
# ==========================================================

def format_duration(value):

    if value is None:
        return "-"

    return f"{float(value):.1f} min"


# ==========================================================
# PERCENTAGE
# ==========================================================

def format_percentage(value):

    if value is None:
        return "-"

    return f"{float(value):.1f}%"


# ==========================================================
# INTEGER
# ==========================================================

def format_integer(value):

    if value is None:
        return "-"

    return f"{int(value):,}"


# ==========================================================
# DECIMAL
# ==========================================================

def format_decimal(value, digits=2):

    if value is None:
        return "-"

    return f"{float(value):,.{digits}f}"


# ==========================================================
# PLOTLY HOVER CURRENCY
# ==========================================================

def hover_currency(value):

    if value is None:
        return "$0"

    return f"${float(value):,.2f}"


# ==========================================================
# PLOTLY HOVER NUMBER
# ==========================================================

def hover_number(value):

    if value is None:
        return "0"

    return f"{int(value):,}"


# ==========================================================
# PLOTLY HOVER DISTANCE
# ==========================================================

def hover_distance(value):

    if value is None:
        return "0 mi"

    return f"{float(value):.2f} mi"


# ==========================================================
# PLOTLY HOVER DURATION
# ==========================================================

def hover_duration(value):

    if value is None:
        return "0 min"

    return f"{float(value):.1f} min"