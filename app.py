import streamlit as st

dashboard_page = st.Page("pages/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True)
data_pasien_page = st.Page("pages/data_pasien.py", title="Data Pasien", icon=":material/data_array:")
analisis_resiko_page = st.Page("pages/analisis_resiko.py", title="Analisis Risiko", icon=":material/analytics:")
simulasi_resiko_page = st.Page("pages/simulasi_resiko.py", title="Simulasi Resiko", icon=":material/accessibility:")
visual_statistik_page = st.Page("pages/visualisasi_statistik.py", title="Visualisasi Statistik", icon=":material/visibility:")
about_page = st.Page("pages/about.py", title="About Page", icon=":material/info:")

pg = st.navigation([dashboard_page, data_pasien_page, analisis_resiko_page, simulasi_resiko_page, visual_statistik_page, about_page])

pg.run()
