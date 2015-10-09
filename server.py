from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail, Message
from flask.ext import excel
from flask import Response

import StringIO
import mimetypes
from werkzeug.datastructures import Headers

from pdfs import create_pdf
from database import getMarvel
from xls_generator import genXls, useTemplate



app = Flask(__name__)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp-mail.outlook.com',
	MAIL_PORT=25,
	MAIL_USE_SSL=False,
	MAIL_USE_TLS = True,
	MAIL_USERNAME = 'flebris@outlook.com',
	MAIL_PASSWORD = 'Passwordtest35'
	)

mail = Mail()
mail.init_app(app)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route("/")
def temp():
	print getMarvel()
 	return render_template('index.html', data=getMarvel())


@app.route("/send/pdf")
def send_pdf():
	filename = "file.pdf"
	#pdf = create_pdf(render_template('template.html', data=model.getItems()))
 	pdf = create_pdf(render_template('template.html', data=getMarvel()))
 	return SendMail(pdf, filename, "flebris@gmail.com")

@app.route("/send/xls")
def send_xls():
	filename = "file.xls"
	output = genXls(getMarvel())
 	return SendMail(output, filename, "flebris@gmail.com")


@app.route("/download/pdf")
def get_pdf():
	output = create_pdf(render_template('template.html', data=getMarvel()))
	filename = "test.pdf"
	return genResponse(output, filename)
#... code for setting up Flask

@app.route('/download/xls')
def get_xls():
	output = useTemplate(getMarvel())
	filename = "test.xls"
	return genResponse(output, filename)



def SendMail(output, filename, to):
	msg = Message("Hello",
                  sender="flebris@outlook.com",
                  recipients=[to])
 	msg.body = "This is the email body"
 	
 	msg.attach(filename, "application/pdf",  output.getvalue())
 	mail.send(msg)
 	return 'Sent'


def genResponse(output, filename):
#########################
    # Code for creating Flask
    # response
    #########################
    response = Response()
    response.status_code = 200

    response.data = output.getvalue()

    ################################
    # Code for setting correct
    # headers for jquery.fileDownload
    #################################
        
    mimetype_tuple = mimetypes.guess_type(filename)

    #HTTP headers for forcing file download
    response_headers = Headers({
            'Pragma': "public",  # required,
            'Expires': '0',
            'Cache-Control': 'must-revalidate, post-check=0, pre-check=0',
            'Cache-Control': 'private',  # required for certain browsers,
            'Content-Type': mimetype_tuple[0],
            'Content-Disposition': 'attachment; filename=\"%s\";' % filename,
            'Content-Transfer-Encoding': 'binary',
            'Content-Length': len(response.data)
        })

    if not mimetype_tuple[1] is None:
        response.update({
                'Content-Encoding': mimetype_tuple[1]
            })

    response.headers = response_headers

    #as per jquery.fileDownload.js requirements
    response.set_cookie('fileDownload', 'true', path='/')

    ################################
    # Return the response
    #################################
    return response


if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0", port=80)
