from fechamento.main import ler_fechamento

def ler_dados(captura_email, acao):
    delivery_email = "nulexlol@gmail.com"
    password = "255698741"
    subject = f"{acao} - Relatório de cotação"
    
    return delivery_email, password, subject, acao