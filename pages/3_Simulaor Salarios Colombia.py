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
barrios_u = sorted(df['barrio'].unique())
sectores_u = sorted(df['sector_económico'].unique())
cargos_u = sorted(df['nombre_cargo'].unique())
niveles_educativos_u = sorted(df['nivel_educativo'].unique())

# -----------------------------------------------------------------------------------
def filtro1():    
    col1, col2 = st.columns(2)
    with col1:
        municipio = st.selectbox("Municipio", municipios_u) 
    with col2:
        sector = st.selectbox("Sector Económico", sectores_u)
    resultado = df[(df['municipio'] == municipio) & (df['sector_económico'] == sector)]
   
    resultado = resultado.reset_index(drop=True) 
    # Gráfico de barras
    cargo = resultado['nombre_cargo']
    fig = go.Figure(data=[
        go.Bar(name='vacantes', x=cargo, y=resultado['numero_de_vacantes']),
        go.Bar(name='salario', x=cargo, y=resultado['salario_honorarios'])
    ])   
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    # Tabla
    st.table(resultado[["nombre_cargo", "numero_de_vacantes", "salario_honorarios", "tipo_de_contrato", "duración_contrato_(meses)"]])
    
# -----------------------------------------------------------------------------------
def filtro2():
    col1, col2, col3 = st.columns(3)
    with col1:
        municipio = st.selectbox("Municipio", municipios_u)
    with col2:
        barrio = st.selectbox("Barrio", barrios_u)
    with col3:
        cargos_u.append("Todos")
        cargo = st.selectbox("Cargo", cargos_u)   

    if cargo == "Todos":
        resultado = df[(df['municipio'] == municipio) & (df['barrio'] == barrio)]
        # Gráfico de barras
        barrios = sorted(df['barrio'].unique())
        fig = go.Figure(data=[
            go.Bar(name='vacantes', x=barrios, y=resultado['numero_de_vacantes']),
            go.Bar(name='salario', x=barrios, y=resultado['salario_honorarios'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado = resultado.reset_index(drop=True) 
        v1 = resultado.loc[0, ['numero_de_vacantes', 'salario_honorarios']]
        v2 = resultado.loc[1, ['numero_de_vacantes', 'salario_honorarios']]
        v3 = resultado.loc[2, ['numero_de_vacantes', 'salario_honorarios']]
        tv = pd.Series([v1.mean(), v2.mean(), v3.mean()])       
        st.subheader("Promedio")
        st.subheader(round(tv.mean(), 1)) 
    else:   
        resultado = df[(df['municipio'] == municipio) & (df['barrio'] == barrio) & (df['nombre_cargo'] == cargo)]
        # Gráfico de barras
        barrio = resultado['barrio']
        fig = go.Figure(data=[
            go.Bar(name='vacantes', x=barrio, y=resultado['numero_de_vacantes']),
            go.Bar(name='salario', x=barrio, y=resultado['salario_honorarios'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado = resultado.reset_index(drop=True) 
        vacantes_salario = resultado.loc[0, ['numero_de_vacantes', 'salario_honorarios']]
        st.subheader("Promedio")
        st.subheader(round(vacantes_salario.mean(), 1)) 
  
# -----------------------------------------------------------------------------------
def filtro3():
    municipio = st.selectbox("Municipio", municipios_u)
    municipio_data = df[df['municipio'] == municipio]
    
    # Gráfico de línea para mostrar las ofertas a lo largo del tiempo (si hay una variable de tiempo disponible)
    fig = go.Figure()
    for index, row in municipio_data.iterrows():
        fig.add_trace(go.Scatter(x=barrios_u, y=[row['numero_de_vacantes'], row['salario_honorarios']],
                                 mode='lines+markers',
                                 name=row['barrio']))
    
    fig.update_layout(title=f"Ofertas de Empleo en {municipio} a lo largo del tiempo",
                      xaxis_title='Barrio',
                      yaxis_title='Datos',
                      legend_title='Barrio')
    
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------------------------------
def filtro4():
    nivel_educativo = st.selectbox("Nivel Educativo", niveles_educativos_u)
    resultado = df[df['nivel_educativo'] == nivel_educativo]

    # Mostrar los datos filtrados por nivel educativo seleccionado.
    st.write(resultado)

# -----------------------------------------------------------------------------------
filtros =[
    "Ofertas por Municipio y Sector",
    "Ofertas por Municipio, Barrio y Cargo",
    "Ofertas por Municipio a lo largo del tiempo",
    "Ofertas por Nivel Educativo"
]

filtro = st.selectbox("Filtros", filtros)

if filtro:
    filtro_index = filtros.index(filtro)

    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()
    elif filtro_index == 2:
        filtro3()
    elif filtro_index == 3:
        filtro4()
