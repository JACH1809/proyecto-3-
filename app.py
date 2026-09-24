import streamlit as st
import requests
from datetime import date

st.title("Registro de participante")

# Captura de fecha de nacimiento
fecha_nacimiento = st.date_input(
    "Fecha de nacimiento",
    value=date(2010, 1, 1),
    min_value=date(1950, 1, 1),
    max_value=date.today()
)

st.write("Fecha seleccionada:", fecha_nacimiento.strftime("%d/%m/%Y"))

if st.button("Guardar"):
    
    datos = {
        "fecha_nacimiento": fecha_nacimiento.strftime("%Y-%m-%d")
    }

    # Ejemplo de envío a una API
    url = "https://tu-api.com/personas"

    respuesta = requests.post(
        url,
        json=datos
    )

    if respuesta.status_code == 200:
        st.success("Información guardada correctamente")
    else:
        st.error(f"Error: {respuesta.status_code}")