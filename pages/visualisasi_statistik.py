import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(
    page_title="Visualisasi Statistik",
    page_icon="images/visual.png",
    layout="wide"
)



df = pd.read_csv(
    "dataset/paru_paru.csv",
    nrows=5000
)



st.title("📊 Visualisasi & Statistik")

st.write(
    """
    Halaman ini menampilkan berbagai
    visualisasi statistik dari dataset
    penyakit paru-paru.
    """
)



tab1, tab2, tab3 = st.tabs([
    "Grafik",
    "Statistik",
    "Insight"
])



with tab1:

    st.subheader(
        "Distribusi Aktivitas Olahraga"
    )

    fig1 = px.pie(
        df,
        names="Aktivitas_Olahraga",
        hole=0.4
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.subheader(
        "Aktivitas Begadang"
    )

    fig2 = px.histogram(
        df,
        x="Aktivitas_Begadang",
        color="Aktivitas_Begadang"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )



with tab2:

    st.subheader("Statistik Dataset")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            f"""
            Total Dataset:
            {len(df)}
            """
        )

        st.info(
            f"""
            Total Perokok Aktif:
            {
                len(
                    df[
                        df["Merokok"] == "Aktif"
                    ]
                )
            }
            """
        )

    with col2:

        st.info(
            f"""
            Total Penyakit:
            {
                len(
                    df[
                        df["Hasil"] == "Ya"
                    ]
                )
            }
            """
        )

        st.info(
            f"""
            Total Begadang:
            {
                len(
                    df[
                        df["Aktivitas_Begadang"] == "Ya"
                    ]
                )
            }
            """
        )

    st.subheader(
        "Ringkasan Data"
    )

    st.dataframe(
        df.describe(include="all"),
        use_container_width=True
    )



with tab3:

    st.subheader(
        "Insight Dataset"
    )

    total = len(df)

    aktif = len(
        df[df["Merokok"] == "Aktif"]
    )

    olahraga = len(
        df[
            df["Aktivitas_Olahraga"]
            == "Jarang"
        ]
    )

    penyakit = len(
        df[df["Hasil"] == "Ya"]
    )

    persen_merokok = (
        aktif / total
    ) * 100

    persen_penyakit = (
        penyakit / total
    ) * 100

    st.success(
        f"""
        Sebanyak
        {persen_merokok:.2f}%
        pasien merupakan
        perokok aktif.
        """
    )

    st.warning(
        f"""
        Sebanyak
        {persen_penyakit:.2f}%
        pasien terindikasi
        terkena penyakit
        paru-paru.
        """
    )

    if olahraga > total / 2:

        st.error(
            """
            Mayoritas pasien
            jarang melakukan olahraga.
            """
        )

    st.info(
        """
        Berdasarkan visualisasi,
        kebiasaan merokok aktif,
        kurang olahraga, dan
        begadang menjadi faktor
        dominan pada dataset ini.
        """
    )