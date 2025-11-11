import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
scatter_button = st.button('Criar gráfico de dispersão') # criar um botão
hist_checkbox = st.checkbox('Exibir histograma') # criar uma caixa de seleção
scatter_checkbox = st.checkbox('Exibir gráfico de dispersão') # criar uma caixa de seleção

if hist_checkbox: # se a caixa de seleção estiver marcada
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    fig.show()

if scatter_checkbox: # se a caixa de seleção estiver marcada
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
    fig.show()

if hist_button: # se o botão for clicado
            # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            # criar um histograma
    fig = px.histogram(car_data, x="odometer")
            # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
    fig.show()


if scatter_button: # se o botão for clicado
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
    fig.show()