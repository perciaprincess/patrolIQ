import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------------------------------
# DIMENSIONALITY REDUCTION PAGE (PCA & t-SNE)
# ------------------------------------------------------------------

def render():
    # Header
    st.markdown(
        """
        <div style="text-align:center; padding:25px;
                    background:linear-gradient(135deg, #6a1b9a, #d81b60);
                    color:white; border-radius:10px; margin-bottom:20px;">
            <h2>🧩 Dimensionality Reduction</h2>
            <p style='font-size:17px;'>Visualize crime patterns using PCA & t-SNE for high‑dimensional embeddings.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("📄 Loading Dimensionality Reduction Files")

    # Try loading PCA & t-SNE component files
    try:
        pca_df = pd.read_csv("D:/Percia_MTech/GUVI/python/Projects/patrol_IQ/data/pca_components.csv")
        st.success("PCA Components Loaded: data/pca_components.csv")
    except:
        pca_df = pd.DataFrame()
        st.warning("PCA file not found. Please generate PCA components.")

    try:
        tsne_df = pd.read_csv("D:/Percia_MTech/GUVI/python/Projects/patrol_IQ/data/tsne_components.csv")
        st.success("t-SNE Components Loaded: data/tsne_components.csv")
    except:
        tsne_df = pd.DataFrame()
        st.warning("t-SNE file not found. Please generate t-SNE components.")

    # ------------------------------------------------------------------
    # PCA Visualization
    # ------------------------------------------------------------------
    st.markdown("### 📉 PCA — Principal Component Analysis")

    if not pca_df.empty:
        # 2D plot
        if pca_df.shape[1] >= 2:
            fig2d = px.scatter(
                pca_df,
                x=pca_df.columns[0],
                y=pca_df.columns[1],
                opacity=0.6,
                title="PCA — 2D Projection",
                color_discrete_sequence=['#7b1fa2'],
            )
            st.plotly_chart(fig2d, use_container_width=True)

        # 3D plot
        if pca_df.shape[1] >= 3:
            st.markdown("#### 🎥 PCA — 3D View")
            fig3d = px.scatter_3d(
                pca_df,
                x=pca_df.columns[0],
                y=pca_df.columns[1],
                z=pca_df.columns[2],
                opacity=0.7,
                title="PCA — 3D Projection",
                color=pca_df.columns[2],
            )
            st.plotly_chart(fig3d, use_container_width=True)
    else:
        st.info("PCA components not available. Run PCA notebook to generate pca_components.csv.")

    # ------------------------------------------------------------------
    # t-SNE Visualization
    # ------------------------------------------------------------------
    st.markdown("### 🎨 t‑SNE — High‑Dimensional Visualization")

    if not tsne_df.empty:
        if tsne_df.shape[1] >= 2:
            fig_tsne = px.scatter(
                tsne_df,
                x=tsne_df.columns[0],
                y=tsne_df.columns[1],
                opacity=0.7,
                title="t‑SNE — 2D Projection",
                color_discrete_sequence=['#d81b60'],
            )
            st.plotly_chart(fig_tsne, use_container_width=True)
    else:
        st.info("t-SNE components not available. Run t-SNE notebook to generate tsne_components.csv.")

    # ------------------------------------------------------------------
    # Download Buttons
    # ------------------------------------------------------------------
    st.markdown("### ⬇️ Download Dimensionality Reduction Outputs")

    if not pca_df.empty:
        st.download_button(
            "Download PCA Components", pca_df.to_csv(index=False), "pca_components.csv","text/csv"
        )

    if not tsne_df.empty:
        st.download_button(
            "Download t-SNE Components", tsne_df.to_csv(index=False), "tsne_components.csv","text/csv"
        )
