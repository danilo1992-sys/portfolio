from flask import (
    Blueprint, current_app, redirect, render_template, request, url_for
)
import sendgrid
from sendgrid.helpers.mail import *

bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index ():
    return render_template ('portfolio/index.html')
        
@bp.route('/sobre mi',  methods=['GET'])
def mi():
    return render_template('portfolio/mi.html')

@bp.route('/mail', methods=['GET','POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        send_mail(name, email, message)
        return render_template('portfolio/sent_mail.html')
    return redirect(url_for('portfolio.index'))

def send_mail(name, email, message):
    mi_mail = 'sanfracaceresdanilo@gmail.com' 
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
    from_email = Email(mi_mail)
    to_email = To(mi_mail, substitutions={
        "-name-":name,
        "-email-":email,
        "-message-":message,
    })

    html_content = """
    <p> Hola danilo tienes un nuebo contacto desde la web:</p>
    <p>Nombre: -name- </p>
    <p>Correo: -email- </p>
    <p>Mensaje: -message- </p>
    """

    mail = Mail(mi_mail, to_email, 'Nuevo contacto desde la web', html_content=html_content)
    response = sg.client.mail.send.post(request_body=mail.get())
