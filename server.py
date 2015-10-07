from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail, Message
from flask.ext import excel
from pdfs import create_pdf

import model
import pyexcel.ext.xls 

import xlwt
import StringIO
import mimetypes
from flask import Response
from werkzeug.datastructures import Headers


app = Flask(__name__)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp-mail.outlook.com',
	MAIL_PORT=25,
	MAIL_USE_SSL=False,
	MAIL_USE_TLS = True,
	MAIL_USERNAME = 'flebris@outlook.com',
	MAIL_PASSWORD = 'cspr!3204'
	)

mail = Mail()
mail.init_app(app)
# ...



@app.route("/pdf")
def index():

	array = [[1,2], [3, 4]]
 	msg = Message("Hello",
                  sender="flebris@outlook.com",
                  recipients=["flebris@gmail.com"])
 	msg.body = "This is the email body"
 	pdf = create_pdf(render_template('template.html', data=model.getItems()))
 	msg.attach("file.pdf", "application/pdf",  pdf.getvalue())
 	mail.send(msg)
 	return 'Sent'

@app.route("/template")
def temp():
	array = [[1,2], [3, 4]]
 	return render_template('template.html', data=model.getItems())

@app.route("/test_xls", methods=['GET'])
def download_file():
	array = [[1,2], [3, 4]]
	return excel.make_response_from_array(array, "xls", status=200)

@app.route('/')
def hello_world():
    return 'Hello World!'



#... code for setting up Flask

@app.route('/xls/')
def export_view():
    #########################
    # Code for creating Flask
    # response
    #########################
    response = Response()
    response.status_code = 200


    ##################################
    # Code for creating Excel data and
    # inserting into Flask response
    ##################################
    workbook = xlwt.Workbook()
    ws = workbook.add_sheet('A Test Sheet')

    i = 1
    ws.write(0, 0, "id")
    ws.write(0, 1, "data")
    
    for item in model.getItems():
   
    	ws.write(i, 0, item['id'])
    	ws.write(i, 1, item['data'])
    	i = i +1
    
    #.... code here for adding worksheets and cells

    output = StringIO.StringIO()
    workbook.save(output)
    response.data = output.getvalue()

    ################################
    # Code for setting correct
    # headers for jquery.fileDownload
    #################################
    filename = "test.xls"
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
	app.run()
