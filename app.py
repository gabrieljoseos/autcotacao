import streamlit as st
import pandas as pd
import plotly.express as px
from fechamento.main import ler_fechamento
from senderemail.main import enviar_email
from utils.utils import capturar_email

# configuração app
st.set_page_config(page_title='Análise Cotação de Ações', 
                   layout='wide', 
                   menu_items={"about": "https//www.linkedin.com/in/gabrieljos"})

# Titulo APP
st.sidebar.title("Análise Cotação de Ações")

## Bloco de Input
acao = st.sidebar.text_input("Digite o código da ação (ex: PETR3.SA)")
data_inicio = st.sidebar.date_input("Data de Início")
data_final = st.sidebar.date_input("Data Final")

# Bloco Output
if st.sidebar.button("Verificar"): #Botão verificar
    with st.expander("Clique para verificar"): #Expander
        col1, col2, col3 = st.columns(3)
        col4,col5 = st.columns([1, 2])
        if acao and data_inicio and data_final:
            fechamento_max, fechamento_min, fechamento_medio, abertura_max, abertura_min, abertura_medio, fechamento = ler_fechamento(acao, data_inicio, data_final)
        
        # Exibir valores de fechamento
        col1.metric(label="Cotação Máximo",value=fechamento_max, delta=abertura_max)
        col2.metric(label="Cotação Minímo",value=fechamento_min, delta=abertura_min)
        col3.metric(label="Cotação Médio",value=fechamento_medio, delta=abertura_medio)

        # Converter dados para DataFrame
        df = pd.DataFrame(fechamento)
        df.reset_index(inplace=True)
        df.columns = ['Data', 'Fechamento']

        # Exibir tabela
        col4.write(df)

        # Criação do gráfico com plotly.express
        fig = px.line(df, x='Data', y='Fechamento', markers=True, title='Cotação das Ações')
        
        # Ajustar o tamanho do gráfico
        fig.update_layout(width=800, height=400)
        
        # Rotacionar os rótulos do eixo x para melhor visualização
        fig.update_xaxes(tickangle=45)
        
        # Exibir o gráfico no Streamlit
        col5.plotly_chart(fig)

# Formulário envio de e-mail dentro do expander
        with st.popover("Enviar e-mail"):
            st.markdown("Preencha os campos abaixo! 👋")

    # Entrada de e-mail
        def capturar_email(reciver_email):
            reciver_email = st.text_input("Qual e-mail deseja receber o relatório")
            return reciver_email
            st.write("Será enviado para o e-mail:", reciver_email)

    # Botão para capturar e enviar o e-mail
            st.button("Enviar", on_click=enviar_email)

else:
    st.sidebar.error("Por favor, preencha todos os campos.")