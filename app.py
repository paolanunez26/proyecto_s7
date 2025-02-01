import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('C:/Users/HP/Documents/PAOLA DOCS/Curso Ciencia de Datos/SPRINT 7/proyecto_s7/vehicles_us.csv')
st.header('Estadisticas de anuncios de venta de autos')
hist_button = st.button('Construir histograma') #Crear un botón

if hist_button: #Al hacer clic en el botón
    #Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    #Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    #Mostrar un gráfico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
