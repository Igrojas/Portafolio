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
        margin: 5px;
    }
    .stButton button:hover {
        background-color: #2e2e2e;
        color: white;
        border: 1px solid #2e2e2e;
    }
    .justified-text {
        text-align: justify;
    }
    .button-container {
        display: flex;
        justify-content: flex-start;
        flex-wrap: wrap;
        gap: 10px;
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

st.markdown(
    """
    <div class="button-container">
        <a href="https://www.linkedin.com/in/ignaciorojasr" target="_blank"><button>LinkedIn</button></a>
        <a href="https://github.com/Igrojas" target="_blank"><button>GitHub</button></a>
        <a href="mailto:igrojasro@hotmail.com" target="_blank"><button>Correo</button></a>
    </div>
    """,
    unsafe_allow_html=True
)

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

st.markdown(
    """
    <div class="button-container">
        <a href="https://ml-flotacion-jdp6tepzersnzkwhyk498a.streamlit.app/" target="_blank"><button>Parte 1</button></a>
        <a href="https://ml-flotacion-a83mcjofehejjrpcth4frl.streamlit.app/" target="_blank"><button>Parte 2</button></a>
        <a href="https://github.com/Igrojas/Memoria-Titulo/blob/main/Memoria%20de%20Titulo%202023.pdf" target="_blank"><button>Memoria de Título</button></a>
    </div>
    """,
    unsafe_allow_html=True
)
