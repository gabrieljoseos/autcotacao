import yfinance as yf

# ler dados da acao
def ler_fechamento(acao, data_inicio, data_final):
    dados = yf.Ticker(acao).history(start=data_inicio, end=data_final, auto_adjust=True)
    fechamento = dados.Close
    abertura = dados.Open

    fechamento_max = round(fechamento.max(), 2)
    fechamento_min = round(fechamento.min(), 2)
    fechamento_medio = round(fechamento.mean(), 2)

    abertura_max = round(abertura.max(), 2)
    abertura_min = round(abertura.min(), 2)
    abertura_medio = round(abertura.mean(), 2)



    return fechamento_max, fechamento_min, fechamento_medio, abertura_max, abertura_min, abertura_medio, fechamento