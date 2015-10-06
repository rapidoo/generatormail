from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail, Message
from pdfs import create_pdf
# ...

app = Flask(__name__)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp-mail.outlook.com',
	MAIL_PORT=25,
	MAIL_USE_SSL=False,
	MAIL_USE_TLS = True,
	MAIL_USERNAME = 'flebris@outlook.com',
	MAIL_PASSWORD = 'password_test'
	)

mail = Mail()
mail.init_app(app)
# ...

@app.route('/your/url')
def your_view():
    subject = "Mail with PDF"
    receiver = "flebris@gmail.com"
    mail_to_be_sent = Message(subject=subject, recipients=[receiver])
    mail_to_be_sent.body = "This email contains PDF."
    pdf = create_pdf(render_template('template.html'))
    mail_to_be_sent.attach("file.pdf", "application/pdf", pdf.getvalue())
    mail_ext.send(mail_to_be_sent)
    return redirect(url_for('other_view'))

@app.route("/test")
def index():

	user = {'nickname': 'Miguel'}
 	msg = Message("Hello",
                  sender="flebris@outlook.com",
                  recipients=["flebris@gmail.com"])
 	msg.body = "This is the email body"
 	pdf = create_pdf(render_template('template.html'))
 	msg.attach("file.pdf", "application/pdf",  pdf.getvalue())
 	mail.send(msg)
 	return 'Sent'


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
	app.debug = True
	app.run()
