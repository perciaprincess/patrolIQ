import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------------------------------
# TEMPORAL PATTERNS PAGE
# ------------------------------------------------------------------
def render():
    # Header
    st.markdown(
        """
        <div style="text-align:center; padding:25px;
                    background:linear-gradient(135deg, #6a1b9a, #d81b60);
                    color:white; border-radius:10px; margin-bottom:20px;">
            <h2>🕒 Temporal Crime Patterns</h2>
            <p style='font-size:17px;'>Analyze crime trends across hours, days, and months.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Load dataset directly
    st.subheader("📄 Loaded Dataset: Chicago_Crimes_Features.csv")

    try:
        df = pd.read_csv("D:\Percia_MTech\GUVI\python\Projects\patrol_IQ\data\chicago_crime_featured.csv")
        st.success("Dataset loaded successfully from: data/Chicago_Crimes_Features.csv")
    except Exception as e:
        st.error(f"Failed to load dataset. Error: {e}")
        return

    # Ensure required columns
    required = ["hour", "day_of_week", "month"]
    if not set(required).issubset(df.columns):
        st.error(f"Dataset must contain required columns: {required}")
        return

    # ---------------------------
    # Crime by Hour
    # ---------------------------
    st.markdown("### ⏱️ Crime Distribution by Hour")
    hourly = df['hour'].value_counts().sort_index()

    fig1 = px.line(
        x=hourly.index, y=hourly.values,
        labels={'x': 'Hour of Day', 'y': 'Crime Count'},
        title="Crimes by Hour of Day",
    )
    st.plotly_chart(fig1, use_container_width=True)

    # ---------------------------
    # Crime by Day of Week
    # ---------------------------
    st.markdown("### 📆 Crime Distribution by Day of Week")
    dow = df['day_of_week'].value_counts().sort_index()

    fig2 = px.bar(
        x=dow.index, y=dow.values,
        labels={'x': 'Day of Week (0=Mon)', 'y': 'Crime Count'},
        title="Crimes by Day of Week",
        text=dow.values,
    )
    st.plotly_chart(fig2, use_container_width=True)

    # ---------------------------
    # Crime by Month
    # ---------------------------
    st.markdown("### 📅 Crime Distribution by Month")
    month = df['month'].value_counts().sort_index()

    fig3 = px.bar(
        x=month.index, y=month.values,
        labels={'x': 'Month', 'y': 'Crime Count'},
        title="Crimes by Month",
        text=month.values,
        color=month.values,
        color_continuous_scale='Reds'
    )
    st.plotly_chart(fig3, use_container_width=True)

    # ---------------------------
    # Heatmap (Day of Week vs Hour)
    # ---------------------------
    st.markdown("### 🔥 Heatmap — Crime Intensity by Hour & Day")

    pivot = df.pivot_table(
        index='day_of_week',
        columns='hour',
        values='case_number' if 'case_number' in df.columns else 'hour',
        aggfunc='count'
    ).fillna(0)

    fig4 = px.imshow(
        pivot,
        aspect='auto',
        color_continuous_scale='Inferno',
        title="Heatmap: Day of Week vs Hour",
        labels={'color': 'Crime Count'}
    )
    st.plotly_chart(fig4, use_container_width=True)

    # ---------------------------
    # Temporal Clusters (If available)
    # ---------------------------
    if 'TimeCluster' in df.columns:
        st.markdown("### 🎯 Temporal Clustering Result (K-Means)")
        fig5 = px.histogram(
            df, x='TimeCluster',
            title='Crime Count per Temporal Cluster',
            color='TimeCluster',
            text_auto=True
        )
        st.plotly_chart(fig5, use_container_width=True)
    else:
        st.info("No temporal clustering found. Run clustering notebook to generate TimeCluster column.")