import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="images/dashboard.png",
    layout="wide"
)



df = pd.read_csv(
    "dataset/paru_paru.csv",
    nrows=5000
)



col1, col2 = st.columns([1, 8])

with col1:
    st.image(
        "images/paruparu.png",
        width=60
    )

with col2:
   st.title("Dashboard Penyakit Paru-Paru")


st.write(
    "Dashboard analisis data pasien penyakit paru-paru."
)


total_pasien = len(df)

total_perokok = len(
    df[df["Merokok"] == "Aktif"]
)

total_penyakit = len(
    df[df["Hasil"] == "Ya"]
)

persentase = (
    total_penyakit / total_pasien
) * 100


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Pasien",
        total_pasien
    )

with col2:
    st.metric(
        "Perokok Aktif",
        total_perokok
    )

with col3:
    st.metric(
        "Terkena Penyakit",
        total_penyakit
    )

with col4:
    st.metric(
        "Persentase Penyakit",
        f"{persentase:.2f}%"
    )



col_chart1, col_chart2 = st.columns(2)



with col_chart1:

    st.subheader(
        "Status Merokok"
    )

    fig_pie = px.pie(
        df,
        names="Merokok",
        hole=0.4
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )



with col_chart2:

    st.subheader(
        "Jenis Kelamin"
    )

    gender = (
        df["Jenis_Kelamin"]
        .value_counts()
    )

    fig_bar = px.bar(
        x=gender.index,
        y=gender.values,
        labels={
            "x": "Gender",
            "y": "Jumlah"
        }
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )



col1, col2 = st.columns([1, 8])

with col1:
    st.image(
        "images/pin.png",
        width=60
    )

with col2:
    st.subheader("Insight Analisis")


if total_perokok > total_pasien / 2:

    st.warning(
        """
        Mayoritas pasien merupakan
        perokok aktif.
        """
    )

if total_penyakit > total_pasien / 2:

    st.error(
        """
        Lebih dari 50% pasien
        terindikasi terkena
        penyakit paru-paru.
        """
    )



st.subheader("Preview Dataset")

st.dataframe(
    df.head(10),
    use_container_width=True
)