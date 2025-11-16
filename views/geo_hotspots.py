import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ------------------------------------------------------------------
# GEO HOTSPOTS PAGE
# ------------------------------------------------------------------
def render():
    # Header
    st.markdown(
        """
        <div style="text-align:center; padding:25px;
                    background:linear-gradient(135deg, #6a1b9a, #d81b60);
                    color:white; border-radius:10px; margin-bottom:20px;">
            <h2>📍 Geographic Crime Hotspots</h2>
            <p style='font-size:17px;'>Identify high-risk locations using clustering & geospatial analysis.</p>
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
    if not set(["latitude", "longitude"]).issubset(df.columns):
        st.error("Dataset must contain 'latitude' and 'longitude' columns.")
        return

    # Drop missing coordinates
    df = df.dropna(subset=["latitude", "longitude"])[:50000]  # limit for speed

    # Map center
    center_lat = df["latitude"].mean()
    center_lon = df["longitude"].mean()

    # Heatmap
    st.markdown("### 🔥 Crime Density Heatmap")
    heat_layer = pdk.Layer(
        "HeatmapLayer",
        data=df,
        get_position='[longitude, latitude]',
        radiusPixels=40,
    )
    deck = pdk.Deck(
        initial_view_state=pdk.ViewState(latitude=center_lat, longitude=center_lon, zoom=10, pitch=40),
        layers=[heat_layer],
    )
    st.pydeck_chart(deck)

    # KMeans Clustering
    st.markdown("### 🎯 K-Means Clustering (Hotspot Detection)")
    k = st.slider("Select number of clusters", 3, 12, 6)

    coords = df[["latitude", "longitude"]]
    scaler = StandardScaler()
    coords_scaled = scaler.fit_transform(coords)

    kmeans = KMeans(n_clusters=k, random_state=42)
    df["cluster"] = kmeans.fit_predict(coords_scaled)

    # Plot
    st.markdown("### 🗺️ Cluster Map")
    fig = px.scatter_mapbox(
        df.sample(min(20000, len(df))),
        lat="latitude",
        lon="longitude",
        color="cluster",
        zoom=9,
        height=650,
        opacity=0.5,
    )
    fig.update_layout(mapbox_style="carto-positron", margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig, use_container_width=True)

    # Cluster summary
    st.markdown("### 📌 Cluster Summary")
    summary = df.groupby("cluster").agg(
        crimes=("cluster", "count"),
        avg_lat=("latitude", "mean"),
        avg_lon=("longitude", "mean"),
    )
    st.dataframe(summary)

    # Download option
    st.markdown("### ⬇️ Download Clustered Data")
    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False),
        file_name="geo_clusters_output.csv",
        mime="text/csv",
    )