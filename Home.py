import streamlit as st

# Set the page title and header
st.title("Calculadora de Liquidación ")
st.header("¡Bienvenido a nuestra Calculadora de Liquidación!")

# Descripción de la aplicación
st.image("https://yekoclub-partner-content.sfo3.digitaloceanspaces.com/partner/745.ba485ade-095b-435f-9fbf-16476f6cea7a.png", width=400)
st.write("**Descripción de la aplicación:** Esta aplicación te permite calcular la liquidación laboral de un trabajador. Puedes ingresar la fecha de inicio y final del periodo laboral, el salario mensual, si el trabajador tiene derecho a auxilio de transporte y el porcentaje de riesgo laboral para obtener el valor de la liquidación.")

# Resumen del Proyecto
st.subheader("¿Qué es la Liquidación Laboral?")
st.write("La liquidación laboral es el proceso mediante el cual se calcula el monto que un empleador debe pagar a un trabajador al finalizar su relación laboral. Este monto incluye el salario proporcional, auxilio de transporte si aplica, y otros conceptos según la legislación laboral.")

# Características y Beneficios
st.subheader("Características y Beneficios de la Calculadora de Liquidación")
st.write("**Cálculo Preciso:** Realiza el cálculo de la liquidación de forma rápida y precisa.")
st.write("**Información Relevante:** Proporciona detalles sobre los componentes del cálculo, como el salario proporcional y el auxilio de transporte.")
st.write("**Fácil de Usar:** Interfaz intuitiva que permite a los usuarios ingresar fácilmente los datos necesarios y obtener el resultado.")

# Llamado a la Acción
st.subheader("¡Comienza a Calcular!")
st.write("**Completa los Campos:** Ingresa la fecha de inicio y final del periodo laboral, el salario mensual, si el trabajador tiene derecho a auxilio de transporte y el porcentaje de riesgo laboral.")
st.write("**Haz Clic en 'Calcular Liquidación':** Obtén el valor de la liquidación laboral de forma instantánea.")

# Equipo y Contacto
st.subheader("¿Necesitas Ayuda?")
st.write("**Contacta con Nosotros:** Si tienes alguna pregunta o necesitas asistencia, no dudes en ponerte en contacto con nuestro equipo.")
st.write("Correo electrónico: [info@calculadoraliquidacion.com](mailto:info@calculadoraliquidacion.com)")
