import streamlit as st


#Texto
st.set_page_config(page_title="Repaso",page_icon=":)",layout="wide")
st.title("Repaso de comandos Streamlit")
st.header("Cabecera")
st.subheader("Subtitulo")
st.text("Texto plano")
st.markdown("**Texto plano**")
st.code("import streamlit as st",language="python")
st.success("Éxito")
st.warning("Warning")
st.error("Error")
st.info("Info")

#Inputs
st.divider()
st.text_input("Introduce texto")
st.number_input("Introduce numero",min_value=1,max_value=10,value=1,step=1)
box=st.selectbox("Opciones",["A","B","C","D","E","F"])
multi=st.multiselect("Opciones",["A","B","C","D","E","F"])
st.checkbox("Opciones",["A"])
if st.button("Pulsa aquí"):
    st.success("Botón pulsado")
fecha=st.date_input("Introduce tu fecha de nacimiento")

#Divisiones de página
st.divider()
col1,col2=st.columns(2)
with col1:
    st.subheader("Columna 1")
with col2:
    st.subheader("Columna 2")
st.divider()
with st.container():
    st.subheader("Contenedor 1")
    st.text("Contenido")
st.divider()
with st.container():
    st.subheader("Contenedor 2")
    st.text("Contenido")
st.divider()
with st.container():
    st.subheader("Contenedor 3")
    st.text("Contenido")
st.divider()
with st.expander("Caja de expansión"):
    st.text("Descripción")

#Enlaces.
st.subheader("Imagen")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKHtdckAE4t_LDmdpT72tDj6sZm8ELdHRloTk4Y0DDSW5QSwGL7jLmQqOB_DJqoaDBvmUopVIZU7bbwSheK434zv6VACIjSrrmoQkIHA78&s=10",caption="Esto es un gatito")
st.subheader("Video")
st.video("https://www.youtube.com/watch?v=f-SHGbS61SM")
#st.audio("URL GATO")
