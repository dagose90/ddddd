import streamlit as st

st.set_page_config(page_title="Prueba examen Esther", layout="wide")

st.title("Generador de saludos")

nombre = st.text_input("Introduce tu nombre")
idioma = st.selectbox("¿En que idioma quieres el saludo?"
                      "", ["", "Español", "Inglés", "Francés"])

if st.button("Saludar"):
    if idioma == "Español":
        st.success(f"Hola, {nombre}")
    elif idioma == "Inglés":
        st.success(f"Hello {nombre}")
    elif idioma == "Francés":
        st.success(f"Salut, {nombre}")
