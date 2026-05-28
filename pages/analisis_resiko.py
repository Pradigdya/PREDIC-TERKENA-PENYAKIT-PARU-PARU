import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Analisis Risiko",
    page_icon="images/analis.png",
    layout="wide"
)

# =========================================
# LOAD DATA
# =========================================

df = pd.read_csv(
    "dataset/paru_paru.csv",
    nrows=5000
)


col1, col2 = st.columns([1, 8])

with col1:
    st.image(
        "images/analis.png",
        width=60
    )

with col2:
    st.title(
        "Analisis Faktor Risiko"
    )
st.write(
    "Analisis faktor-faktor yang mempengaruhi penyakit paru-paru."
)



merokok_aktif = len(
    df[df["Merokok"] == "Aktif"]
)

begadang = len(
    df[df["Aktivitas_Begadang"] == "Ya"]
)

jarang_olahraga = len(
    df[df["Aktivitas_Olahraga"] == "Jarang"]
)

penyakit_bawaan = len(
    df[df["Penyakit_Bawaan"] == "Ada"]
)



risk_df = pd.DataFrame({
    "Faktor": [
        "Merokok Aktif",
        "Begadang",
        "Jarang Olahraga",
        "Penyakit Bawaan"
    ],
    "Jumlah": [
        merokok_aktif,
        begadang,
        jarang_olahraga,
        penyakit_bawaan
    ]
})


st.subheader(
    "Ranking Faktor Risiko"
)

fig = px.bar(
    risk_df,
    x="Jumlah",
    y="Faktor",
    orientation="h",
    text="Jumlah"
)

st.plotly_chart(
    fig,
    use_container_width=True
)



st.subheader(
    "Insight"
)

faktor_terbesar = risk_df.loc[
    risk_df["Jumlah"].idxmax()
]["Faktor"]

st.success(
    f"""
    Faktor risiko terbesar dalam dataset ini adalah:
    {faktor_terbesar}
    """
)



st.subheader(
    "Tingkat Risiko"
)

for index, row in risk_df.iterrows():

    persen = (
        row["Jumlah"] / len(df)
    )

    st.write(row["Faktor"])

    st.progress(
        min(int(persen * 100), 100)
    )



st.subheader(
    "Rekomendasi"
)

st.info(
    """
    Berdasarkan analisis data,
    kebiasaan merokok aktif dan
    kurang olahraga menjadi
    faktor dominan penyebab
    penyakit paru-paru.

    Disarankan untuk:
    - Mengurangi rokok
    - Rutin olahraga
    - Menghindari begadang
    - Menjaga pola hidup sehat
    """
)