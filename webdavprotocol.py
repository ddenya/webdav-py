from flask.views import MethodView

from flask import request, make_response, render_template, send_file
from logger_class import Logger
import io

logger = Logger()

class WebDavProtocol(MethodView):

    """This class handles WebDav protocol, but does not implement any FS logic"""

    def __init__(self):
        # self.files = __class__.files
        pass

    def propfind(self, path=None, pathname=None):

        self.files['depth'] = request.headers['Depth']

        if not pathname:
            return make_response(render_template('propfind_file_generated.xml', values=self.get_file(pathname)), 207)

        elif pathname and self.find_file(pathname):
            self.files['only_files'] = True
            return make_response(render_template('propfind_one_file.xml', values=self.find_file(pathname) ), 207)

        return make_response('', 404)


    def options(self):
        response = make_response("GOT OPTIONS11 HERE")
        response.headers[
            'Allow'] = 'OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, ORDERPATCH'
        response.headers['DAV'] = '1, 2, ordered-collections'
        return response


    def get(self, pathname=None):

        logger.add_custom(self.files)

        if not pathname or not self.find_file(pathname):
            return make_response('', 404)

        elif pathname and self.find_file(pathname):

            file_to_send = self.find_file(pathname)

            data_bytes = io.BytesIO()
            data_bytes.write(bytes(file_to_send['data'], 'utf-8'))
            data_bytes.seek(0)

            if file_to_send['mimetype'] == 'text/plain':
                return send_file(data_bytes, mimetype=file_to_send['mimetype'])
            else:
                return send_file(data_bytes, attachment_filename=file_to_send['name'], mimetype=file_to_send['mimetype'],
                                 as_attachment=True)