# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:37:08 2025

@author: jperezr
"""

import streamlit as st
import pandas as pd

# Título de la aplicación
page = st.sidebar.radio("Navegar por", ["Formulario", "Comentarios"])

# Cambiar el título dependiendo de la página seleccionada
if page == "Formulario":
    st.title("FORO COMUNITARIO DE: ¡ Ideas y Propuestas para un México Mejor !")
elif page == "Comentarios":
    st.title("Comentarios Recientes del Foro Comunitario")

# Sidebar: Foro Comunitario
st.sidebar.title("Foro Comunitario: Evaluación de Políticas Públicas del Gobierno de México")
st.sidebar.markdown("""
¡Bienvenidos al foro! Este es un espacio creado para que puedas compartir tus opiniones sobre las políticas públicas del gobierno actual de México. Tu opinión es valiosa y puede ayudar a mejorar el rumbo del país.

Preguntas sobre las políticas públicas del gobierno de México:

1. **¿Qué opinas sobre las políticas públicas implementadas por el gobierno de México en los últimos años?**
    - ¿Crees que están beneficiando a la mayoría de los ciudadanos?

2. **¿Consideras que las reformas económicas del gobierno han tenido un impacto positivo en la estabilidad financiera del país?**
    - ¿Qué cambios te gustaría ver en este ámbito?

3. **¿Cómo crees que las políticas sociales han afectado a las comunidades vulnerables?**
    - ¿Crees que se ha hecho suficiente para reducir las desigualdades sociales?

4. **¿Qué piensas sobre las iniciativas ambientales y de sustentabilidad implementadas por el gobierno?**
    - ¿Crees que están siendo efectivas en la protección del medio ambiente?

5. **¿Qué sugerencias tienes para mejorar las políticas públicas del gobierno actual?**
    - Comparte tus ideas sobre lo que podría hacerse de manera diferente.
    
### Desarrollado por: 
- Javier Horacio Pérez Ricárdez    
    
""")

# Enlace del Google Forms modificado para incrustar
google_forms_url = "https://docs.google.com/forms/d/e/1FAIpQLSeXCnKleayPwpOnqb08qGbiUCFyE5YCJXq7fyQnfoKRdT4MEQ/viewform?embedded=true"

# URL pública de Google Sheets para leer los datos como CSV
sheet_id = "1MgwGBBFuX_s-xsCH1TTK7KB_eLR94H3kZtGDrjyWlB8"
sheet_name = "Hoja1"  # Cambia esto por el nombre de la hoja que almacena las respuestas
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Leer los datos desde Google Sheets
df = pd.read_csv(csv_url)

# Si la página seleccionada es "Formulario"
if page == "Formulario":
    # Mostrar el formulario en un iframe
    st.components.v1.html(
        f"""
        <iframe src="{google_forms_url}" width="640" height="800" frameborder="0" marginheight="0" marginwidth="0">
        Cargando…
        </iframe>
        """,
        height=800,
    )

    # Agregar espacio entre los botones
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

# Si la página seleccionada es "Comentarios"
if page == "Comentarios":
    # Mostrar solo la lista de comentarios
    st.subheader("Comentarios Recientes")

    if 'Comentarios' in df.columns:
        for i, comentario in enumerate(df['Comentarios'], 1):
            st.markdown(f"**{i}.** {comentario}")
    else:
        st.write("No se encontraron comentarios en las respuestas.")