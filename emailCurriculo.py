#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#         IMPORTAÇÕES

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#         DECLARAÇÃO DE VARIÁVEIS

#host

sender      = "exemplo@gmail.com"                                                   # email do remetente (seu email)
password    = "senha"                                                               # senha do email acima
port        = 584                                                                   # porta do email
receiver    = input ("Informe o email do destinatário: ")                           # email do destinatário
job         = input ("Informe o nome da vaga: ")                                    # nome da vaga
body        =  '''Venho por meio deste email, me candidatar para a vaga descrita.
                Segue em anexo o currículo.'''                                      # corpo do email

'''
Observação: é necessário encontrar a senha de segurança do google para fazer
login com senhas de app. Mais detalhes no link abaixo: 

https://support.google.com/accounts/answer/185833?visit_id=638137423597285247-3416429218&p=InvalidSecondFactor&rd=1

Também é necessário que a opção "Acesso a app menos seguro" esteja habilitada ou ativar a autenticação de dois
fatores e criar a senha para aplicativo (desktop) e utilizar essa senha no seu código..

'''

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#         SETUP DO MIME

message             = MIMEMultipart()
message['From']     = sender
message['To']       = receiver
message['Subject']  = 'Acerca da vaga descrita de ' + job

message.attach(MIMEText(body, 'plain'))

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#         PREPARANDO PDF

pdfname     = "C://Users//..."                                                      # nome/caminho do arquivo
binary_pdf  = open(pdfname, 'rb')                                                   # abrir o arquivo
payload     = MIMEBase('application', 'octate-stream', Name=pdfname)                # dar load no arquivo com o mime
payload.set_payload((binary_pdf).read())                                            # ler o arquivo

encoders.encode_base64(payload)                                                     # codificando o arquivo na base64

payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)         # adicionar leitor com o nome do pdf
message.attach(payload)                                                             # upar messagem com o pauload

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#         CRIANDO SESSÃO SMTP PARA ENVIAR EMAIL

session = smtplib.SMTP('smtp.gmail.com', port)                                       # gmail + port 
session.starttls()                                                                  # ativar "segurança" 
session.login(sender, password)                                                     # login
 
text = message.as_string()                                                          # texto do email
session.sendmail(sender, receiver, text)                                            # enviar o email de fato
session.quit()                                                                      # sair da sessão
print('Mail Sent')                                                                  # informar que o email foi enviado

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#         FIM