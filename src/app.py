from flask import app, Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import src.pwd

host = "smtp.gmail.com"
port = "587"
login = "develog80@gmail.com"
senha = src.pwd.pwd()
#

meu_app = Flask(__name__)
@meu_app.route('/')
def home():
    return render_template('home.html')

@meu_app.route('/contato',methods = ['GET','POST'])
def contato():

    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        message = request.form.get('mensagem')

        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(login, senha)

        msg=(f'Fabrício! Você ecebeu uma mensagem de: \n {nome} {sobrenome} \n com o email:  {email} com a mensagem: \n\n {message}')

        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['To'] = login
        email_msg['Subject'] = "Email do Profile"
        email_msg.attach(MIMEText(msg,'Plain'))
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        server.quit()

        return render_template('contato.html', message=message)
    return render_template('contato.html')


@meu_app.route('/experiencia')
def experiencia():
    return render_template('experiencia.html')

@meu_app.route('/formacao')
def formacao():
    return render_template('formacao.html')

@meu_app.route('/interesses')
def interesses():
    return render_template('interesses.html')

@meu_app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@meu_app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
   meu_app.run('0.0.0.0')