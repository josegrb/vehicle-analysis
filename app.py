import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Análise de Veículos')

car_data = pd.read_csv('vehicles.csv')

st.header('Análise Exploratória')

if st.button('Criar Histograma da Quilometragem'):
    st.write('Histograma gerado:')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)



if st.button('Criar Gráfico de Dispersão (Quilometragem vs Preço)'):
    st.write('Gráfico de dispersão gerado:')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2)

