PatrolIQ — Urban Safety Intelligence Platform
AI-powered Crime Hotspot Detection • Temporal Pattern Mining • City Safety Analytics
<p align="center"> <img src="https://img.shields.io/badge/ML-Unsupervised_Learning-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/Framework-Streamlit-red?style=for-the-badge"> <img src="https://img.shields.io/badge/Tracking-MLflow-%23E57373?style=for-the-badge"> <img src="https://img.shields.io/badge/Data-Chicago_Crime-yellow?style=for-the-badge"> </p>
**📘 Project Overview**

PatrolIQ is an AI-driven crime analysis platform built using unsupervised machine learning, designed to help police departments and city planners understand:

Where crimes are happening (hotspots)

When crimes occur the most (temporal patterns)

How crime behaviors cluster naturally

What patterns exist in high-dimensional crime data

The system processes 500,000+ crime records from Chicago (2001–2025) and provides a fully interactive dashboard built with Streamlit.

🎯 Project Objectives

Identify geographic crime hotspots using K-Means, DBSCAN, and Hierarchical Clustering

Analyze temporal crime patterns (hour, day-of-week, month)

Apply PCA and t-SNE to visualize high-dimensional crime features

Track all experiments using MLflow

Build a multi-page Streamlit application for real-time crime intelligence

Provide actionable insights for police patrol routing & resource planning

🗂️ Tech Stack

Languages: Python
Libraries: NumPy, Pandas, Scikit-Learn, Plotly, PyDeck
Visualization: Streamlit
Experiment Tracking: MLflow
Dimensionality Reduction: PCA, t-SNE
Clustering: K-Means, DBSCAN, Agglomerative
Deployment: Streamlit Cloud / Local Deployment

📁 Folder Structure
crime_app/
│── app.py
│── utils.py
│── data/
│   ├── Chicago_Crimes_Features.csv
│   ├── pca_components.csv
│   └── tsne_components.csv
│── views/
│   ├── home.py
│   ├── geo_hotspots.py
│   ├── temporal_patterns.py
│   ├── dimensionality_reduction.py
│   └── model_tracker.py
│── notebooks/
│   ├── Data_Preprocessing.ipynb
│   ├── EDA.ipynb
│   ├── Feature_Engineering.ipynb
│   ├── Geo_Clustering.ipynb
│   ├── Temporal_Clustering.ipynb
│   └── Dimensionality_Reduction.ipynb
│── README.md


🧠 Key Features
🔥 1. Geographic Crime Hotspots

K-Means (5–10 clusters)

DBSCAN for density-based hotspots

Hierarchical clustering with dendrogram

Interactive heatmaps and cluster boundaries

Hotspot summary tables

🕒 2. Temporal Pattern Analysis

Crime patterns by hour, day, and month

Heatmap of Day-of-Week vs Hour

Temporal clustering (3–5 crime behavior profiles)

Peak crime period and seasonal insights

🧩 3. Dimensionality Reduction

PCA: reduces 22+ features → top 2–3 components

t-SNE: reveals hidden structure in crime patterns

2D & 3D interactive visualizations

📈 4. MLflow Integration

Tracks:

Clustering model parameters

Silhouette score

Davies–Bouldin score

PCA explained variance

Dimensionality reduction outputs

🌐 5. Streamlit Web App

Multi-page dashboard:

Home

Geo Hotspots

Temporal Patterns

Dimensionality Reduction

Model Tracking

Fully interactive and visually rich.
