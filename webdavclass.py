from flask import request, render_template, make_response
from flask.views import MethodView
from files import make_files

class WebDAV_server(MethodView):

    def propfind(self,file=None):

        print("I have got FILE: " + str(file))
        print("RURI: " + str(request.url))

        files = {
            'files': make_files(),
            'depth': request.headers['Depth']
        }

        if file:
            files['only_files'] = True


        print("Files structure: " + str(files))
        print("Search result: " + str(files['files']['link'].find(str(file))) )

        if not file:
            print('LIST ONLY DIR')
            return make_response(render_template('propfind_file_generated.xml', values=files))
        elif file and files['files']['link'].find(str(file)):
            print('LIST ONLY FILE')
            return make_response(render_template('propfind_one_file.xml',values=(files['files']['link'].find(str(file)))))

        return 404


    def options(self):
        response = make_response("GOT OPTIONS11 HERE")
        response.headers['Allow'] = 'OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, ORDERPATCH'
        response.headers['DAV'] = '1, 2, ordered-collections'
        return response


    def get(self,file=None):

        print("I HAVE GET!!")
        print("I have got FILE in GET: " + str(file))
        print("RURI: " + str(request.url))

        return 200










    #
    #
    #
    #
    #     # Making files, but cutting the root
    #     files = make_files()
    #     files = files['includes'][0]
    #
    #     depth = request.headers['Depth']
    #
    #     files['depth'] = depth
    #
    #     print("Depth: " + str(files['depth']) )
    #
    #     print("\n" + str(files['includes'][0]) + "\n")
    #
    #     template = render_template('propfind_file_generated.xml', values=files['includes'][0])
    #     response = make_response(template)
    #     return response
    #
    # def parse_propfind(self,request):
    #
    #     # Taking Depth out: if depth is 0 - only container should be described
    #     # If depth is 1 - everything in container should be described
    #     # Depth = infinity is not implemented now
    #
    #     depth = request.headers['Depth']
    #     files = make_files()
    #
    #     url = request.url
    #     urlsplit = url.strip().split("/")
    #     print(urlsplit)
    #
    #     url_result = []
    #
    #     for elem in urlsplit:
    #         if elem:
    #             url_result.append(elem)
    #
    #     # List only folder : depth == 0:
    #
    #     res = self.find_in_files(files,url_result[-1],recursive=True)
    #
    #     if depth == '0':
    #         files['list_mode'] = 'folder'
    #     if depth == '1':
    #         files['list_mode'] = 'file'
    #     if depth !=0 and depth !=1:
    #         files['list_mode'] = 'unknown'
    #
    #
    #     test = self.list_dir(files)
    #
    #     return self.parse_propfind1(request)
    #
    #
    #
    #
    # def find_in_files(self,files,name,recursive=False):
    #
    #     '''
    #     Finds files and dirs in given structure (dictionary) recursively if flag is set
    #     Example of structure is provided in files.py
    #     Accepts root element as initial one, but probably can accept any directory
    #     Returns an array with every entity, matched by name
    #     '''
    #
    #     found = []
    #
    #     for item in files['includes']:
    #
    #         if item['is_directory'] == True and recursive:
    #             print(str(item))
    #             found.extend(self.find_in_files(item,name))
    #
    #         if item['name'] == str(name):
    #             found.append(item)
    #
    #     return found
    #
    # def list_dir(self,files):
    #
    #     '''
    #     Lists a directory
    #     Returns everything underlying (a dictionary with everything in 'includes' section)
    #     '''
    #
    #     res = {}
    #     for item in files['includes']:
    #         res.update(item)
    #     return res
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
