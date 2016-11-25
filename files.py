def make_files():

    directory_root = '/webdav/'

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

    root = {
    'name': directory_root,
    'is_directory': True,
    'includes': [file1,file2,file5,dir1,dir2]

    }

    return root

