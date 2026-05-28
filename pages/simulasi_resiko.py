import streamlit as st

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Simulasi Risiko",
    page_icon="images/simulation.png",
    layout="wide"
)


col1, col2 = st.columns([1, 8])
with col1:
    st.image(
        "images/simulation.png",
        width=60
    )

with col2:
    st.title("Simulasi Risiko Penyakit")


st.write(
    """
    Halaman ini digunakan untuk
    mensimulasikan tingkat risiko
    penyakit paru-paru berdasarkan
    gaya hidup pasien.
    """
)



st.subheader("Input Data Pasien")

col1, col2 = st.columns(2)

with col1:

    usia = st.selectbox(
        "Usia",
        ["Muda", "Tua"]
    )

    merokok = st.selectbox(
        "Status Merokok",
        ["Aktif", "Pasif"]
    )

    olahraga = st.selectbox(
        "Aktivitas Olahraga",
        ["Sering", "Jarang"]
    )

with col2:

    begadang = st.selectbox(
        "Aktivitas Begadang",
        ["Ya", "Tidak"]
    )

    penyakit_bawaan = st.selectbox(
        "Penyakit Bawaan",
        ["Ada", "Tidak"]
    )

    bekerja = st.selectbox(
        "Bekerja",
        ["Ya", "Tidak"]
    )



if st.button("Analisis Risiko"):

    skor = 0


    if usia == "Tua":
        skor += 2

    if merokok == "Aktif":
        skor += 3

    if olahraga == "Jarang":
        skor += 2

    if begadang == "Ya":
        skor += 2

    if penyakit_bawaan == "Ada":
        skor += 3

    if bekerja == "Ya":
        skor += 1

 

    st.subheader("Hasil Analisis")

    

    if skor <= 3:

        st.success(
            """
            Risiko Rendah Terkena
            Penyakit Paru-Paru
            """
        )

    

    elif skor <= 7:

        st.warning(
            """
            Risiko Sedang Terkena
            Penyakit Paru-Paru
            """
        )

    

    else:

        st.error(
            """
            Risiko Tinggi Terkena
            Penyakit Paru-Paru
            """
        )


    st.subheader("Tingkat Risiko")

    persen = min(skor * 10, 100)

    st.progress(persen)

    st.write(f"Skor Risiko: {skor}")

    

    st.subheader("Rekomendasi")

    rekomendasi = []

    if merokok == "Aktif":
        rekomendasi.append(
            "- Kurangi kebiasaan merokok"
        )

    if olahraga == "Jarang":
        rekomendasi.append(
            "- Rutin melakukan olahraga"
        )

    if begadang == "Ya":
        rekomendasi.append(
            "- Hindari begadang berlebihan"
        )

    if penyakit_bawaan == "Ada":
        rekomendasi.append(
            "- Lakukan pemeriksaan rutin"
        )

    if len(rekomendasi) == 0:

        st.success(
            """
            Gaya hidup Anda sudah cukup baik.
            """
        )

    else:

        for item in rekomendasi:
            st.write(item)