from webdavprotocol import WebDavProtocol
from testwebdavprotocol import TestWebDavProtocol

from flask import Flask, request, make_response

import os
from logger_class import Logger

# Enables request logging to log file
debug = True

# Logger
logger = Logger()
logger.flush()

# Crunch, needed for path_join in jinja_handler. Temporary.
host = '192.168.88.56'
#host = '192.168.1.120'

# List of allowed methods
ALLOWED_METHODS = ['GET', 'PUT', 'PROPFIND', 'PROPPATCH', 'MKCOL', 'DELETE',
                   'COPY', 'MOVE', 'OPTIONS']

app = Flask(__name__)

webdav_view = TestWebDavProtocol.as_view('webdav')
app.add_url_rule('/webdav', defaults={'path': ''}, view_func=webdav_view, methods=ALLOWED_METHODS)
app.add_url_rule('/webdav/<path:pathname>', view_func=webdav_view, methods=ALLOWED_METHODS)

@app.before_request
def logging():
    if debug:
        logger.add('request',request)

@app.after_request
def logging(response):
    if debug:
        logger.add('response',response)
    return response


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

@app.context_processor
def jinja_handler():
    '''
    Allows to pass results of execution of python functions to jinja2 templates
    I just wonder how it works
    '''

    def pathjoin(*args):
        return os.path.join('http://',host,*args)

    return dict(pathjoin=pathjoin)

if __name__ == "__main__":
    app.run('0.0.0.0',80, True)