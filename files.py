import random

class File(object):

    def __init__(self, name):
        self.name   = name
        self.id = random.randint(0,10000000)
        self.type = 'file'
        self.data = ''

    def set_data(self,data):
        self.data = str(data)

    def get_data(self):
        return self.data

class Directory(object):

    def __init__(self, name):
        self.name = name
        self.includes = []
        self.type = 'directory'

    def push(self,links_to_obj):
        self.includes.extend(links_to_obj)

    def pop(self,links_to_obj):
        del self.includes[includes.index(links_to_obj)]

    def list(self):

        list_result = {}

        print(self.includes)

        for item in self.includes:

            print("Type: " + str(type(item)) + "Obj: " + str(item) )

            list_result[item.id] = {
                'type':item.type,
                'name':item.name,
                'data':item.data
            }

        return list_result


a = File('test1')
b = File('test2')
c = File('test3')


d = Directory('webdav')
d.push([a,b,c])

print(d.list())

a.set_data("hello")

print(d.list())






def make_files():

    file1 = {
    'name':'test1',
    'is_directory': False,
    'data': 'hello'
    }

    file2 = {
    'name':'test2',
    'is_directory': False,
    'data': 'hello2'
    }

    file3 = {
    'name':'test3',
    'is_directory': False,
    'data': 'hello'
    }

    file4 = {
    'name':'test4',
    'is_directory': False,
    'data': 'hello2'
    }

    file5 = {
    'name':'test4',
    'is_directory': False,
    'data': 'hello5'
    }

    file6 = {
    'name':'test4',
    'is_directory': False,
    'data': 'hello6'
    }

    file7 = {
    'name':'test7',
    'is_directory': False,
    'data': 'hello7'
    }


    dir1 = {
        'name':'dirtest1',
        'is_directory': True,
        'includes': [file3,file4]
    }

    dir2 = {
        'name':'dirtest2',
        'is_directory': True,
        'includes': [file6,file7]
    }

    webdav = {
        'name':'webdav',
        'is_directory': True,
        'includes': [file1,file2,file5,dir1,dir2]
    }

    root = {
    'name': 'root',
    'is_directory': True,
    'includes': [webdav]
    }

    return root

