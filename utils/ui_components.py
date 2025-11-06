import streamlit as st
from config import THEME

def inject_style():
    st.markdown(f"""
        <style>
        body {{
            background-color: {THEME['bg_light']};
            color: {THEME['text']};
        }}
        .card {{
            background: white;
            border-radius: 16px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 16px;
            margin-bottom: 12px;
        }}
        .logo {{
            height: 60px;
            margin-right: 12px;
        }}
        .title {{
            font-size: 1.2rem;
            font-weight: bold;
            color: {THEME['primary']};
        }}
        .subtitle {{
            color: {THEME['accent']};
            font-weight: 600;
        }}
        </style>
    """, unsafe_allow_html=True)

def render_card(row):
    logo = row.get("logo") or row.get("logoUrl") or ""
    col1, col2 = st.columns([1, 3])
    with col1:
        if logo:
            st.image(logo, use_container_width=False)
        else:
            st.image("https://via.placeholder.com/100x60.png?text=Sin+Logo")
    with col2:
        st.markdown(f"**RUN:** {row.get('run','')}  ")
        st.markdown(f"<div class='title'>{row.get('razonSocial','')}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='subtitle'>{row.get('ciudad','')} — {row.get('comuna','')}</div>", unsafe_allow_html=True)
        st.write(f"📍 {row.get('calle','')} #{row.get('numero','')}")
        if row.get("email"):
            st.write(f"✉️ {row['email']}")
        if row.get("telefono"):
            st.write(f"📞 {row['telefono']}")
