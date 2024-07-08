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

st.title('Hola, soy Ignacio Rojas')

st.write("""
    Ingeniero civil matemático con experiencia en análisis de datos y programación. Especializado en matemáticas aplicadas y estadísticas, 
    enfocado en la resolución de problemas complejos con precisión y eficiencia.
""")

st.markdown("""
    [LinkedIn](https://www.linkedin.com/in/tu_perfil_de_linkedin) | 
    [GitHub](https://github.com/tu_usuario_de_github) | 
    [Correo](mailto:tu_correo@example.com)
""")
# with st.container():
#     col1,col2 = st.columns(2)
#     with col1:
#         st.write("##")
#         st.subheader("Ignacio Rojas")
#         st.title("Ingeniero civil matemático")
#     with col2:
#         st_lottie(lottie_codder)

# st.write("---")

st.write("##")

st.header("Experiencia")
st.subheader("Práctica Profesional - Empírica Consultores")
st.markdown("""
Santiago de Chile  
Octubre 2023 - Noviembre 2023
""")

st.markdown("""
- 🔍 **Realización del análisis, limpieza y selección de datos para proyecto de minería.**
- 📊 **Creación de visualizaciones detalladas utilizando técnicas como PCA y K-means.**
- 🤖 **Exploración y aplicación de modelos de machine learning para optimización predictiva.**
- 📈 **Presentación efectiva de resultados respaldada por análisis riguroso de datos.**
""")

st.markdown("[Ver proyecto completo](https://ml-flotacion-jdp6tepzersnzkwhyk498a.streamlit.app/)")

# st.write("---")
st.write("##")

st.header("Educación")
# Detalles de la Educación
st.subheader("Ingeniero Civil Matemático - Universidad de Concepción")
st.write(" Memoria de Título: Estudio Bibliométrico de las Redes de Coautoría de la Literatura en Psicología de Chile en el Período 2015-2020 ")
st.write(" Proyecto FONDECYT Regular 1201681")

# Descripción de las tareas realizadas en la Memoria de Título
st.markdown("""
- 🔍 **Recopilación y unificación de datos de múltiples fuentes, incluyendo Scopus, WOS y Scielo.**
- 🧩 **Procesamiento de datos y análisis mediante indicadores bibliométricos.**
- 🧮 **Desarrollo de algoritmos para evaluar la influencia y agrupación de autores.**
- 📊 **Creación de visualizaciones gráficas y grafos para representar la información de manera efectiva.**""")

#st.markdown("[Ver proyecto completo](https://ml-flotacion-jdp6tepzersnzkwhyk498a.streamlit.app/)")
