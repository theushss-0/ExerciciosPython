import os
from string import Template
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from dotenv import load_dotenv

load_dotenv()

class MyTamplate(Template):
    delimiter="%"



#Caminho arquivo HTML
CAMINHO_ARQUIVO = Path(__file__).parent / "pagina_dados_envio.html"


#Dados do remetente e do destinatario
remetente = os.getenv("FROM_EMAIL", "")
destinatario = remetente

#Configuração do SMTP GMAIL
servidor_smtp = 'smtp.gmail.com'
porta_smtp = 587
usuario_smtp = remetente
senha_smtp = os.getenv("EMAIL_PASSWORLD","")


#Mensagem envio
with open(CAMINHO_ARQUIVO, "r") as arquivo:
    mensagem_arquivo = arquivo.read()
    tamplate = MyTamplate(mensagem_arquivo)
    mensagem_envio = tamplate.substitute(nome="Matheus", nome_remetente="Otávio Cursos")

print(mensagem_envio)

# Transformar a mensagem em MIMEMultpart
mime_multpart = MIMEMultipart()
mime_multpart['from'] = remetente
mime_multpart['to'] = destinatario
mime_multpart['subject'] = 'Este é um email para teste'

corpo_email = MIMEText(mensagem_envio, "html", "utf-8")
mime_multpart.attach(corpo_email) # prepara o envio


#Envia o email
with smtplib.SMTP(servidor_smtp, porta_smtp) as server:
    server.ehlo()
    server.starttls()
    server.login(usuario_smtp, senha_smtp)
    server.send_message(mime_multpart)
    print("E-mail enviado com sucesso!")