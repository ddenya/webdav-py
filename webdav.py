from flask import Flask, request, g, make_response, redirect, url_for,render_template
from lxml import etree
import os
from webdavclass import WebDAV_server

# http:\\192.168.1.120\webdav\
# Enables request logging to console
debug = True

# Log files

request_log = 'requests.log'
response_log = 'responces.log'

# List of allowed methods
ALLOWED_METHODS = ['GET', 'PUT', 'PROPFIND', 'PROPPATCH', 'MKCOL', 'DELETE',
                   'COPY', 'MOVE', 'OPTIONS']

app = Flask(__name__)

app.add_url_rule('/webdav/', view_func=WebDAV_server.as_view('webdav'),methods=ALLOWED_METHODS)

@app.before_request
def modify_request():

    # It seems that Windows client is missing a trailing slash in RURI
    if request.method == 'PROPFIND':
        # print("Initial RURI: " + str(request.url))
        if request.url[-1] != '/':
        #     pass
        #     request.url = request.url + '/'
        # print("Modified RURI: " + str(request.url))
            return redirect(url_for('webdav'))

    if debug:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), request_log),mode='a') as file:
            file.write("-----\n")
            file.write("Method: " + str(request.method) + "\n")
            file.write("RURI: " + str(request.url) + "\n")
            file.write("Headers: " + str(request.headers) + "\n")
            file.write("Data: " + str(request.data) + "\n")
            file.write("-----\n")

@app.after_request
def logging(response):
    if debug:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), response_log),mode='a') as file:
            file.write("-----\n")
            file.write("Method: " + str(response.status) + "\n")
            file.write("Headers: " + str(response.headers) + "\n" )
            file.write("Data: " + str(response.get_data()) + "\n" )
            file.write("-----\n")
    return response


# @app.route('/webdav/',methods = ALLOWED_METHODS)
# def methods_handler():
#
#     print("Request on /webdav/: " + str(request.method))
#
#     response = make_response('hello',200)
#
#     if request.method == 'OPTIONS':
#         response = make_response("GOT OPTIONS11 HERE")
#         response.headers['Allow'] = 'OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, ORDERPATCH'
#         response.headers['DAV'] = '1, 2, ordered-collections'
#
#     if request.method == 'PROPFIND':
#         print("I HAVE PROPFIND HERE")
#         depth = request.headers['Depth']
#         print("GOT DEPTH: " + str(depth) + " end \n")
#
#         response = parse_propfind(request)
#
#
#     return response
#
# @app.route('/webdav',methods=ALLOWED_METHODS)
# def handler():
#     if request.method == 'PROPFIND':
#         make_response('HAHAHAHA PROPFND',200)



@app.route('/',methods=ALLOWED_METHODS)
def capture_options():

    '''
    Windows client sends first OPTIONS request to server root despite any path
    which was entered in network mount Window
    '''

    resp = make_response('GOT something else: + str(request.method)', 200)

    if request.method == 'OPTIONS':

        # TO DO: Last Allow overrides previous.
        # Add multiple 'Allow'
        resp = make_response("GOT OPTIONS HERE")
        resp.headers['Allow'] = 'OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, COPY, MOVE, \
        MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, ORDERPATCH'
        resp.headers['DAV'] = '1, 2, ordered-collections'
        return resp

    return resp




if __name__ == "__main__":
    app.run('0.0.0.0',80, True)

