import streamlit as st
from streamlit_option_menu import option_menu
import requests
from st_social_media_links import SocialMediaIcons
import webbrowser


st.title('Hola, soy :blue[Ignacio Rojas]')

st.write("""
    Ingeniero civil matemático con experiencia en análisis de datos y programación. Especializado en matemáticas aplicadas y estadísticas, 
    enfocado en la resolución de problemas complejos con precisión y eficiencia.
""")

social_media_links = [
        "https://www.linkedin.com/in/ignaciorojasr",
        "https://github.com/Igrojas",

]

colors = [None, "White"]
social_media_icons = SocialMediaIcons(social_media_links, colors)
social_media_icons.render(justify_content="Left")    

st.write("##")

st.title(":blue[Proyectos Personales]")

def mostrar_proyecto(titulo, descripcion, imagen_url, link, referencias):
    
    st.write("###")
    st.write(f"### :green[{titulo}]")
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        
        st.write(descripcion)
    with col2:
        st.markdown(
            f'<a href="{link}" target="_blank"><img src="{imagen_url}" style="width:90%;"></a>',
            unsafe_allow_html=True
        )
    refs = " | ".join([f"[{ref['nombre']}]({ref['enlace']})" for ref in referencias])
    st.markdown(f"{refs}")


# Proyecto 
titulo = "Estudio Bibliométrico: Indicadores Bibliométricos y Análisis de Redes"
descripcion = """
            Se ha llevado a cabo una recopilación y unificación de datos de diversas fuentes como Scopus,
            WOS y Scielo, para luego someterlos a un procesamiento y análisis mediante indicadores bibliométricos. 
            Además, se han desarrollado algoritmos para evaluar la influencia y agrupación de autores,
            y se han creado visualizaciones gráficas y grafos para representar la información de manera efectiva, facilitando así su comprensión y análisis.
"""
link = "https://bibliometria-dashboard.streamlit.app/"
imagen = "https://raw.githubusercontent.com/Igrojas/An-lisis-bibliom-trico/main/imagenes/Grafo.jpeg"
referencias = [
    {"nombre": "Análisis de Redes", "enlace": "https://social-network-analysis.streamlit.app/"},
    {"nombre": "Dashboard", "enlace": "https://bibliometria-dashboard.streamlit.app/"},
    {"nombre": "Algoritmo AuthorRank", "enlace": "https://algoritmo-a-uthorrank.streamlit.app/"},
    {"nombre": "Algoritmo ABCD", "enlace": "https://algoritmo-comunidades-abcd.streamlit.app/"},
    {"nombre": "Memoria de título", "enlace": "https://github.com/Igrojas/Memoria-Titulo/blob/main/Memoria%20de%20Titulo%202023.pdf"}
]
mostrar_proyecto(titulo, descripcion, imagen, link, referencias)

# Proyecto 
titulo = "Machine Learning: Flotación Predictiva"
descripcion = """
            Realicé el análisis, limpieza y selección de datos para un proyecto de minería,
            exploré y apliqué modelos de machine learning para optimización predictiva,
            y presenté los resultados de manera efectiva respaldada por un análisis riguroso de datos.
"""
link = "https://flotacion.streamlit.app/"
imagen = "https://raw.githubusercontent.com/Igrojas/ML-Flotacion/main/imagenes/cobre.jpeg"
referencias = [
    {"nombre": "Flotación", "enlace": "https://flotacion.streamlit.app/"}
]
mostrar_proyecto(titulo, descripcion, imagen, link, referencias)

  
# Proyecto 
titulo = "Análisis de Datos del Tenis"
descripcion = """
        Este proyecto analiza estadísticas clave del tenis, como victorias,
        porcentaje de victorias, enfrentamientos directos y rendimiento en diferentes superficies.
        También incluye un grafo que muestra las conexiones entre los principales tenistas para
        ofrecer una visión clara de los mejores jugadores basándonos en datos y títulos.
"""
imagen = "https://raw.githubusercontent.com/Igrojas/Head2Head-Tennis/main/imagenes/tenis.jpeg"
link = "https://datoshistoricostenis.streamlit.app/"
referencias = [
    {"nombre": "Datos del tenis", "enlace": "https://datoshistoricostenis.streamlit.app/"}
]
mostrar_proyecto(titulo, descripcion, imagen, link, referencias)


# Proyecto 
titulo = "Top Semanal Spotify"
descripcion = """
         Análisis de Tendencias Musicales Globales: Visualización de datos de popularidad musical semanal en Chile, Colombia y a nivel mundial,
         destacando informes clave como las canciones más reproducidas, el artista más escuchado y el artista con más semanas en el top 50.
"""
link = "https://top-seman-al-chile.streamlit.app/"
imagen = "https://raw.githubusercontent.com/Igrojas/Spotify/main/imagenes/spotify.png"
referencias = [
    {"nombre": "Dashboard spotify", "enlace": "https://top-seman-al-chile.streamlit.app/"}
]
mostrar_proyecto(titulo, descripcion, imagen, link, referencias)

st.write("###")

st.header(":blue[Experiencia]")
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

st.markdown("""
            [**Flotación**](https://flotacion.streamlit.app/)""")

st.write("###")

st.header(":blue[Educación]")

st.subheader("Ingeniero Civil Matemático - Universidad de Concepción")
st.write(" Memoria de Título: Estudio Bibliométrico de las Redes de Coautoría de la Literatura en Psicología de Chile en el Período 2015-2020 ")
st.write(" Proyecto FONDECYT Regular 1201681")

st.markdown("""
- 🔍 **Recopilación y unificación de datos de múltiples fuentes, incluyendo Scopus, WOS y Scielo.**
- 🧩 **Procesamiento de datos y análisis mediante indicadores bibliométricos.**
- 🧮 **Desarrollo de algoritmos para evaluar la influencia y agrupación de autores.**
- 📊 **Creación de visualizaciones gráficas y grafos para representar la información de manera efectiva.**""")

st.markdown("""
[Memoria de título](https://github.com/Igrojas/Memoria-Titulo/blob/main/Memoria%20de%20Titulo%202023.pdf) | 
[Dashboard](https://bibliometria-dashboard.streamlit.app/) | 
[Análisis de Redes](https://social-network-analysis.streamlit.app/) |
[Algoritmo AuthorRank](https://algoritmo-a-uthorrank.streamlit.app/) |
[Algoritmo ABCD](https://algoritmo-comunidades-abcd.streamlit.app/)""")










