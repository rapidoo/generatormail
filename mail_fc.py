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
