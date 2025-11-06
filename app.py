import streamlit as st
import pandas as pd
from utils.api_client import get_runs
from utils.ui_components import inject_style, render_card
from config import THEME
import streamlit as st
import traceback

try:
    # (todo el contenido actual de tu app)
    st.title("🧾 Consulta de Clientes por RUN")
    ...
except Exception as e:
    st.error("❌ Error al ejecutar la aplicación:")
    st.code(traceback.format_exc())

st.set_page_config(
    page_title="Consulta de Clientes RUN",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_style()

st.title("🧾 Consulta de Clientes por RUN")
st.markdown(
    f"<h5 style='color:{THEME['primary']}'>Sistema conectado a MongoDB vía API</h5>",
    unsafe_allow_html=True
)

# --- Filtros ---
st.sidebar.header("🔍 Filtros de búsqueda")
query_run = st.sidebar.text_input("Buscar por RUN o parte del RUN:")
query_nombre = st.sidebar.text_input("Razón Social (contiene):")
query_ciudad = st.sidebar.text_input("Ciudad:")
query_comuna = st.sidebar.text_input("Comuna:")
limite = st.sidebar.slider("Límite por página", 50, 1000, 200)

buscar = st.sidebar.button("Buscar")

# --- Consulta API ---
if buscar:
    with st.spinner("Consultando API..."):
        filtro = query_run or query_nombre or query_ciudad or query_comuna
        df, next_cursor, total = get_runs(limit=limite, query=filtro)

        if df.empty:
            st.warning("No se encontraron resultados.")
        else:
            st.success(f"{len(df)} resultados (total aprox: {total:,})")

            # Mostrar tarjetas
            for _, row in df.iterrows():
                render_card(row)

            # Descarga
            st.download_button(
                label="⬇️ Descargar resultados en Excel",
                data=df.to_excel(index=False, engine="openpyxl"),
                file_name="clientes_filtrados.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

else:
    st.info("Usa los filtros de la izquierda y presiona **Buscar**.")
