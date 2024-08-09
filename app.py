import streamlit as st
import pandas as pd
import plotly.express as px
from fechamento.main import ler_fechamento
import time

# configuração app
st.set_page_config(page_title='Análise Cotação de Ações', 
                   layout='wide', 
                   menu_items={"about": "https//www.linkedin.com/in/gabrieljos"})

# Titulo APP
st.sidebar.title("Análise Cotação de Ações")

## Bloco de Input
acao = st.sidebar.text_input("Digite o código da ação (ex: AAPL)")
data_inicio = st.sidebar.date_input("Data de Início")
data_final = st.sidebar.date_input("Data Final")

# Filtro para cotações
filtro_opcoes = ['Close', 'Open', 'Volume']

# Bloco retorno Input
if st.sidebar.button("Verificar"):
    with st.expander("Clique para verificar"):
        col1, col2, col3 = st.columns(3)
        col4,col5 = st.columns([1, 2])
        if acao and data_inicio and data_final:
            fechamento_max, fechamento_min, fechamento_medio, abertura_max, abertura_min, abertura_medio, dados_filtrados = ler_fechamento(acao, data_inicio, data_final)
        
        # Exibir valores de fechamento
        col1.metric(label="Cotação Máximo",value=fechamento_max, delta=abertura_max)
        col2.metric(label="Cotação Minímo",value=fechamento_min, delta=abertura_min)
        col3.metric(label="Cotação Médio",value=fechamento_medio, delta=abertura_medio)

        # Converter dados para DataFrame
        df = pd.DataFrame(dados_filtrados)
        df.reset_index(inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])

        # Filtrar DataFrame com base nas datas selecionadas
        df = df[(df['Date'] >= data_inicio) & (df['Date'] <= data_final)]

         # Filtro multiselect
        filtro_selecionado = st.sidebar.multiselect(
            "Selecione o tipo",
            options=filtro_opcoes,
            default=['Close']  # Valor padrão para exibir no início
        )

        # Atualizar DataFrame com base na seleção do filtro
        filtro_df = df[['Date'] + filtro_selecionado]

        # Exibir tabela
        col4.write(filtro_df)

        # Criação do gráfico com plotly.express
        fig = px.line(filtro_df, x='Date', y=filtro_selecionado, markers=True, title='Cotação das Ações')
        
        # Ajustar o tamanho do gráfico
        fig.update_layout(width=800, height=400)
        
        # Rotacionar os rótulos do eixo x para melhor visualização
        fig.update_xaxes(tickangle=45)
        
        # Exibir o gráfico no Streamlit
        col5.plotly_chart(fig)
else:
    st.sidebar.error("Por favor, preencha todos os campos.")