import streamlit as st
from datetime import date

st.title("🎂 Calculadora de Fecha de Nacimiento")

st.write("Ingrese su edad actual:")

edad = st.number_input(
    "Edad",
    min_value=0,
    max_value=120,
    step=1
)

if st.button("Calcular fecha de nacimiento"):

    hoy = date.today()

    anio_nacimiento = hoy.year - edad

    st.success(
        f"Fecha de nacimiento estimada: "
        f"{hoy.day:02d}/{hoy.month:02d}/{anio_nacimiento}"
    )

    st.write(f"📅 Día: {hoy.day}")
    st.write(f"📅 Mes: {hoy.month}")
    st.write(f"📅 Año: {anio_nacimiento}")

    st.info(
        "Este cálculo supone que hoy es el día de su cumpleaños."
    )
