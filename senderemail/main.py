from .dados import ler_dados
from app import capturar_email
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar_email():
    delivery_email, password, subject, acao = (capturar_email, acao)

    # Configurar a mensagem
    mensagem = MIMEMultipart()
    mensagem['Subject'] = subject
    mensagem['From'] = delivery_email
    mensagem['To'] = reciver_email
    mensagem.attach(MIMEText("Corpo do e-mail", 'plain'))

    # Configurar o contexto SSL
    contexto = ssl.create_default_context()

    # Enviando o e-mail
    try:
        with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=contexto) as servidor:
            servidor.login(delivery_email, password)
            servidor.sendmail(delivery_email, reciver_email, mensagem.as_string())
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar e-mail: {e}")