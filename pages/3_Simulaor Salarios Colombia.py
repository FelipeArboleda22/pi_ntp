import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# Set the page title and header
st.title("Simulador Ofertas de Empleo")

# Cargar el archivo CSV
df = pd.read_csv('static/datasets/raw1.csv')

# Convertir los nombres de las columnas a minúsculas
df.columns = [col.lower() for col in df.columns]

# Listas de valores únicos para los selectboxes
municipios_u = sorted(df['municipio'].unique())
sectores_u = sorted(df['sector_económico'].unique())
cargos_u = sorted(df['nombre_cargo'].unique())
niveles_educativos_u = sorted(df['nivel_educativo'].unique())

# -----------------------------------------------------------------------------------
def filtro_municipio_sector():    
    municipio = st.selectbox("Municipio", municipios_u)
    sector = st.selectbox("Sector Económico", sectores_u)
    
    resultado = df[(df['municipio'] == municipio) & (df['sector_económico'] == sector)]
    
    if resultado.empty:
        st.write("No se encontraron resultados para la combinación seleccionada.")
    else:
        # Gráfico de barras
        fig = go.Figure(data=[
            go.Bar(name='Vacantes', x=resultado['nombre_cargo'], y=resultado['numero_de_vacantes']),
            go.Bar(name='Salario', x=resultado['nombre_cargo'], y=resultado['salario_honorarios'])
        ])   
        fig.update_layout(barmode='group', title='Vacantes y Salarios por Cargo')
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabla
        st.table(resultado[['nombre_cargo', 'numero_de_vacantes', 'salario_honorarios']])
    
# -----------------------------------------------------------------------------------
def filtro_municipio_cargo():
    municipio = st.selectbox("Municipio", municipios_u)
    cargo = st.selectbox("Cargo", ['Todos'] + cargos_u)

    if cargo == "Todos":
        resultado = df[df['municipio'] == municipio]
    else:
        resultado = df[(df['municipio'] == municipio) & (df['nombre_cargo'] == cargo)]
    
    if resultado.empty:
        st.write("No se encontraron resultados para la combinación seleccionada.")
    else:
        # Gráfico de barras
        fig = go.Figure(data=[
            go.Bar(name='Vacantes', x=resultado['nombre_cargo'], y=resultado['numero_de_vacantes']),
            go.Bar(name='Salario', x=resultado['nombre_cargo'], y=resultado['salario_honorarios'])
        ])   
        fig.update_layout(barmode='group', title='Vacantes y Salarios por Cargo')
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabla
        st.table(resultado[['nombre_cargo', 'numero_de_vacantes', 'salario_honorarios']])
        
# -----------------------------------------------------------------------------------
def filtro_nivel_educativo():
    nivel_educativo = st.selectbox("Nivel Educativo", niveles_educativos_u)
    resultado = df[df['nivel_educativo'] == nivel_educativo]
    
    if resultado.empty:
        st.write("No se encontraron resultados para el nivel educativo seleccionado.")
    else:
        # Tabla
        st.table(resultado[['nombre_cargo', 'numero_de_vacantes', 'salario_honorarios', 'municipio', 'sector_económico']])
    
# -----------------------------------------------------------------------------------
filtros =[
    "Ofertas por Municipio y Sector",
    "Ofertas por Municipio y Cargo",
    "Ofertas por Nivel Educativo"
]

filtro = st.selectbox("Filtros", filtros)

if filtro:
    if filtro == "Ofertas por Municipio y Sector":
        filtro_municipio_sector()
    elif filtro == "Ofertas por Municipio y Cargo":
        filtro_municipio_cargo()
    elif filtro == "Ofertas por Nivel Educativo":
        filtro_nivel_educativo()
