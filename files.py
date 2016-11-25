def make_files():
    directory_root = '/webdav/'
    includes = []

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

    root = {
    'name': directory_root,
    'is_directory': True,
    'includes': [file1,file2]

    }

    return root

