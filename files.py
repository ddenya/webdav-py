from random import randint
import mimetypes

class File(object):

    def __init__(self, name):

        '''
        File properties
        '''

        self.name = name
        self.id = str(randint(0,10000000))
        self.type = 'file'
        self.data = ''
        self.size = '0'
        self.mimetype = mimetypes.guess_type(self.name)



    def set_data(self,data):

        '''
        Adds data and corrects file size
        #TODO: Add correct size calculation (data is just str, size now is just len(str) )
        '''

        self.data = str(data)
        self.size = str(len(data))

    def get_data(self):
        return self.data

    def list(self):
        '''
        Lists properties of file
        '''

        return {'link':self,
                'name':self.name,
                'id':self.id,
                'data':self.data,
                'size':self.size,
                'type':self.type,
                'mimetype':self.mimetype[0]
                }

class Directory(object):

    def __init__(self, name):

        '''
        Defining directory properties
        '''
        self.name = name
        self.includes = []
        self.type = 'directory'

    def push(self,links_to_obj):

        '''
        Adds file to directory
        '''

        self.includes.extend(links_to_obj)

    def pop(self,links_to_obj):

        '''
        Removes file from directory
        '''

        del self.includes[includes.index(links_to_obj)]

    def list(self):

        '''

        Lists a directory. Returns a dictionary in format:

        d = {
        'id_of_file' = {
                        'prop_name':prop_value
                        }
            }

        '''

        list_result = {}
        list_result['link'] = self

        for item in self.includes:
            list_result[item.id] = item.list()

        return list_result

    def find(self, name):

        '''
        Finds entity by name in directory.
        Returns output of its list method.
        '''

        for item in self.includes:
            if item.name == str(name):
                return item.list()

def make_files():

    '''
    Makes directory webdav and 3 files in it
    '''

    a = File('test1.png')
    a.set_data("hello")

    b = File('test2.txt')
    b.set_data("sometext")

    c = File('test3.jpg')

    d = Directory('webdav')

    # In the form of ARRAY!
    d.push([a, b, c])

    #print("List" + str(d.list() ))

    return d.list()