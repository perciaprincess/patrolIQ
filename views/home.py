import streamlit as st
import plotly.express as px
import pandas as pd

# ------------------------------------------------------------------
# HOME PAGE — PatrolIQ Dashboard
# ------------------------------------------------------------------
def render():
    st.markdown("""
    <div style="text-align:center; padding:25px;
                background:linear-gradient(135deg, #6a1b9a, #d81b60);
                color:white; border-radius:12px; margin-bottom:20px;">
        <h1>🚓 PatrolIQ — Crime Analytics Dashboard</h1>
        <p style='font-size:18px;'>Using AI-powered Unsupervised Learning to Understand Crime Patterns.</p>
    </div>
""", unsafe_allow_html=True)

    # ------------------------
    # KPI Cards
    # ------------------------
    st.markdown("### 📊 Key Metrics Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Crimes Loaded", "500,000+", "Chicago Dataset")
    col2.metric("Crime Types", "32", "Including Assault, Theft, Burglary")
    col3.metric("Years Covered", "2001–2025")

    # ------------------------
    # Quick Description Box
    # ------------------------
    st.markdown(
        """
        <div style='padding:20px; background-color:#e3f2fd; border-radius:10px; margin-top:15px;'>
            <h3 style='color:#0d47a1;'>🔍 What You Can Do in PatrolIQ</h3>
            <ul style='font-size:16px;'>
                <li>Identify <b>geographic crime hotspots</b> using KMeans, DBSCAN & Hierarchical Clustering</li>
                <li>Analyze <b>temporal crime patterns</b> by hour, day & month</li>
                <li>Visualize data using <b>PCA & t-SNE</b> dimensionality reduction</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )