from flask import request, render_template, make_response
from flask.views import MethodView
from files import make_files

class WebDAV_server(MethodView):

    def propfind(self):
        return self.parse_propfind(request)

    def options(self):
        response = make_response("GOT OPTIONS11 HERE")
        response.headers['Allow'] = 'OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, ORDERPATCH'
        response.headers['DAV'] = '1, 2, ordered-collections'
        return response

    def parse_propfind1(self,request):
        files = make_files()
        depth = request.headers['Depth']
        files['depth'] = depth
        template = render_template('propfind_file_generated.xml', values=files)
        response = make_response(template)
        return response

    def parse_propfind(self,request):

        # Taking Depth out: if depth is 0 - only container should be descripted
        # If depth is 1 - everything in container should be descripted
        # Depth = infinity is not implemented now

        depth = request.headers['Depth']
        files = make_files()

        url = request.url
        print("URI: " + str(url))

        # List only folder : depth == 0:
        if depth == '0':
            only_folder_list_ = True

        test = self.find_in_files(files,'test4')

        print("SEARCH: " + str(test))

        return self.parse_propfind1(request)

    def find_in_files(self,files,name):

        '''
        Finds files and dirs in given structure (dictionary)
        Example of structure is provided in files.py
        Accepts root element as initial one, but probably can accept any directory
        '''

        found = []
        print("find_in_files called for name == " + files['name'])

        for item in files['includes']:

            if item['is_directory'] == True:
                print("Here")
                print(str(item))
                found.extend(self.find_in_files(item,name))

            if item['name'] == str(name):
                print("FOUND!" + str(item))
                found.append(item)

        return found










