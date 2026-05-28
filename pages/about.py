import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="About Page",
    page_icon="images/about.png",
    layout="wide"
)

st.markdown(
    """
    # Penyakit Paru-Paru
    """
)

st.write(
    "Penyakit paru-paru adalah gangguan pada organ pernapasan yang menyebabkan fungsi paru-paru tidak bekerja dengan baik. Penyakit ini dapat disebabkan oleh infeksi, polusi udara, dan kebiasaan merokok. Gejalanya meliputi batuk, sesak napas, dan nyeri dada."
)

st.subheader(
    "Tujuan"
)

st.write(
    "Tujuan project website ini adalah untuk membantu pengguna melakukan prediksi dini terhadap risiko penyakit paru-paru berdasarkan gejala yang dialami. Website ini juga bertujuan memberikan informasi kesehatan secara cepat, mudah, dan edukatif agar pengguna lebih peduli terhadap kondisi paru-parunya."
)

st.subheader("Teknologi yang Digunakan")

st.info("""
- **Python** → bahasa pemrograman utama
- **Streamlit** → framework website interaktif
- **Pandas** → pengolahan dataset
- **Plotly** → visualisasi data
- **Machine Learning** → prediksi penyakit paru-paru
- **Dataset Kaggle** → sumber data penelitian
""")
st.info(    
    "Dataset ini diambil dari kaggle.com"

)

st.markdown(
    """
    # Profile Pengembang
    """
)

col1, col2 = st.columns(2)

with col1:

    left, center, right = st.columns([1,2,1])

    with center:
        st.write("## Pradigya Rafly")
        st.image("images/rafly.jpg", width=200)
        st.write("## 2313010631")

with col2:

    left, center, right = st.columns([1,2,1])

    with center:
        
        st.write("## Affan Pradipa")
        st.image("images/rafly.jpg", width=200)
        st.write("## 2313010638")
