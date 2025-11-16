import streamlit as st
from streamlit_option_menu import option_menu

# -----------------------------------------------------------------------------
# 🌆 PatrolIQ Crime Analytics Dashboard — Main App
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="PatrolIQ — Urban Safety Intelligence",
    page_icon="🚓",
    layout="wide"
)

# -----------------------------------------------------------------------------
# Sidebar Navigation Menu
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        "<h3 style='margin-bottom:10px;color:#0d47a1;font-size:24px;'>🚨 PatrolIQ</h3>",
        unsafe_allow_html=True
    )

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Geo Hotspots",
            "Temporal Patterns",
            "Dimensionality Reduction"
        ],
        icons=[
            "house",
            "map",
            "clock-history",
            "diagram-2",
            "bar-chart-line"
        ],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#f5f7fa"},
            "icon": {"color": "#8e24aa", "font-size": "18px"},   # purple icon
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#f3e5f5",     # light lavender hover
                "color": "#444",
            },
            "nav-link-selected": {
                "background-color": "#8e24aa",  # purple selected
                "color": "white",
                "font-size": "15px",
                "border-radius": "6px",
            },
        }

    )

# -----------------------------------------------------------------------------
# Dynamic Page Routing
# -----------------------------------------------------------------------------
if selected == "Home":
    from views import home
    home.render()

elif selected == "Geo Hotspots":
    from views import geo_hotspots
    geo_hotspots.render()

elif selected == "Temporal Patterns":
    from views import temporal_patterns
    temporal_patterns.render()

elif selected == "Dimensionality Reduction":
    from views import dimensionality_reduction
    dimensionality_reduction.render()

elif selected == "Model Tracker":
    from views import model_tracker
    model_tracker.render()

# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------
st.markdown(
    """
    <hr style='border:1px solid #1565c0;margin-top:25px;margin-bottom:10px'>
    <p style='text-align:center;color:#444'>
        © 2025 PatrolIQ | Built with ❤️ using Streamlit & MLflow
    </p>
    """,
    unsafe_allow_html=True
)