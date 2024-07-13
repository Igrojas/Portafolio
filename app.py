import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

# st.set_page_config(layout="wide")

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_codder = load_lottieur("https://lottie.host/31483329-3d9e-47b9-9e2c-ec78b400d0b9/lNTQUwdr8s.json")

# CSS con diseño pa los botones y links
st.markdown(
    """
    <style>
    body {
        background-color: #0a0a0a;
        color: white;
    }
    .main {
        background-color: #0a0a0a;
        color: white;
    }
    .stButton button {
        background-color: #1e1e1e;
        color: white;
        border: 1px solid #1e1e1e;
        border-radius: 5px;
    }
    .stButton button:hover {
        background-color: #2e2e2e;
        color: white;
        border: 1px solid #2e2e2e;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .justified-text {
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Hola, soy Ignacio Rojas')

st.markdown(
    """
    <div class="justified-text">
    Ingeniero civil matemático con experiencia en análisis de datos y programación. Especializado en matemáticas aplicadas y estadísticas, 
    enfocado en la resolución de problemas complejos con precisión y eficiencia.
    </div>
    """,
    unsafe_allow_html=True
)

#Cols pa botones

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("LinkedIn"):
        st.write("[LinkedIn](https://www.linkedin.com/in/ignaciorojasr)")
        
with col2:
    if st.button("GitHub"):
        st.write("[GitHub](https://github.com/Igrojas)")
        
with col3:
    if st.button("Correo"):
        st.write("[Correo](mailto:igrojasro@hotmail.com)")

st.write("###")

st.header("Experiencia")
st.subheader("Práctica Profesional - Empírica Consultores")
st.markdown("""
Santiago de Chile  
Octubre 2023 - Noviembre 2023
""")

st.markdown(
    """
    <div class="justified-text">
    - 🔍 **Realización del análisis, limpieza y selección de datos para proyecto de minería.**<br>
    - 📊 **Creación de visualizaciones detalladas utilizando técnicas como PCA y K-means.**<br>
    - 🤖 **Exploración y aplicación de modelos de machine learning para optimización predictiva.**<br>
    - 📈 **Presentación efectiva de resultados respaldada por análisis riguroso de datos.**<br>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("###")

st.header("Educación")
st.subheader("Ingeniero Civil Matemático - Universidad de Concepción")
st.write("Memoria de Título: Estudio Bibliométrico de las Redes de Coautoría de la Literatura en Psicología de Chile en el Período 2015-2020")
st.write("Proyecto FONDECYT Regular 1201681")

st.markdown(
    """
    <div class="justified-text">
    - 🔍 **Recopilación y unificación de datos de múltiples fuentes, incluyendo Scopus, WOS y Scielo.**<br>
    - 🧩 **Procesamiento de datos y análisis mediante indicadores bibliométricos.**<br>
    - 🧮 **Desarrollo de algoritmos para evaluar la influencia y agrupación de autores.**<br>
    - 📊 **Creación de visualizaciones gráficas y grafos para representar la información de manera efectiva.**<br>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("###")

# Cols pa lo mismo

col4, col5, col6 = st.columns([1, 1, 1])

with col4:
    if st.button("Parte 1"):
        st.write("[Parte 1](https://ml-flotacion-jdp6tepzersnzkwhyk498a.streamlit.app/)")
        
with col5:
    if st.button("Parte 2"):
        st.write("[Parte 2](https://ml-flotacion-a83mcjofehejjrpcth4frl.streamlit.app/)")
        
with col6:
    if st.button("Memoria de Título"):
        st.write("[Memoria de Título](https://github.com/Igrojas/Memoria-Titulo/blob/main/Memoria%20de%20Titulo%202023.pdf)")
