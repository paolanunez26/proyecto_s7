import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
st.header('Estadísticas de anuncios de venta de coches')

hist_button = st.button('Construir histograma') #Crear un botón

if hist_button: #Al hacer clic en el botón
    #Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    #Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    #Mostrar un gráfico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir un gráfico de dispersión') #Crear un botón

if disp_button:
    #Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    #Crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price")

    #Mostrar un gráfico plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
