import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="Data Pasien",
    page_icon="images/paruparu.png",
    layout="wide"
)


df = pd.read_csv(
    "dataset/paru_paru.csv",
    nrows=5000
)



col1, col2 = st.columns([1, 6])

with col1:
    st.image(
        "images/paruparu.png",
        width=80
    )

with col2:
    st.title("Data Pasien")
    st.write(
        """
        Halaman ini menampilkan data pasien
        penyakit paru-paru berdasarkan dataset.
        """
    )



total_data = len(df)

total_penyakit = len(
    df[df["Hasil"] == "Ya"]
)

total_sehat = len(
    df[df["Hasil"] == "Tidak"]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        f"Total Data Pasien: {total_data}"
    )

with col2:
    st.warning(
        f"Terindikasi Penyakit: {total_penyakit}"
    )

with col3:
    st.success(
        f"Tidak Terindikasi: {total_sehat}"
    )



st.subheader("Tabel Data Pasien")

st.dataframe(
    df,
    use_container_width=True,
    height=500
)


csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Data CSV",
    data=csv,
    file_name="data_pasien.csv",
    mime="text/csv"
)


st.caption(
    "Dashboard Analisis Penyakit Paru-Paru"
)