import streamlit as st

def calcular_liquidacion(fecha_inicio, fecha_final, salario_mensual, tiene_auxilio_transporte, porcentaje_riesgo):
    # Calcula el número de días trabajados
    dias_trabajados = (fecha_final - fecha_inicio).days
    
    # Calcula el salario proporcional a los días trabajados
    salario_proporcional = salario_mensual / 30 * dias_trabajados
    
    # Calcula el auxilio de transporte si corresponde
    auxilio_transporte = 0
    if tiene_auxilio_transporte and salario_mensual <= 1817052:  # Valor del auxilio de transporte para 2024
        auxilio_transporte = 106454
    
    # Calcula la liquidación
    liquidacion = salario_proporcional + auxilio_transporte
    
    return liquidacion

# Crea la interfaz de usuario con Streamlit
def main():
    st.title("Calculadora de Liquidación")

    # Entradas de usuario
    fecha_inicio = st.date_input("Ingrese la fecha de inicio del periodo a liquidar (YYYY-MM-DD):")
    fecha_final = st.date_input("Ingrese la fecha de final del periodo a liquidar (YYYY-MM-DD):")
    salario_mensual = st.number_input("Ingrese su salario mensual:")
    tiene_auxilio_transporte = st.checkbox("¿Tiene derecho a un auxilio de transporte?")
    porcentaje_riesgo = st.selectbox("Seleccione la clase de riesgos laborales correspondiente al sector de actividad y al cargo del trabajador:",
                                      ["Riesgo I", "Riesgo II", "Riesgo III", "Riesgo IV"])

    # Convierte porcentaje de riesgo seleccionado a valor numérico
    porcentaje_riesgo_map = {"Riesgo I": 0.005, "Riesgo II": 0.01, "Riesgo III": 0.02, "Riesgo IV": 0.04}
    porcentaje_riesgo_valor = porcentaje_riesgo_map[porcentaje_riesgo]

    # Calcula liquidación al hacer clic en el botón
    if st.button("Calcular Liquidación"):
        liquidacion = calcular_liquidacion(fecha_inicio, fecha_final, salario_mensual, tiene_auxilio_transporte, porcentaje_riesgo_valor)
        liquidacion_formateada = "$ {:,.0f}".format(liquidacion)  # Formatear el resultado con punto decimal y signo de peso
        st.write(f"La liquidación laboral es: {liquidacion_formateada}")

if __name__ == "__main__":
    main()
