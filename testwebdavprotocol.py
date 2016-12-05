from webdavprotocol import WebDavProtocol
from files import make_files

class TestWebDavProtocol(WebDavProtocol):

    """This class instantiates from WebDavProtocol and handles FS logic."""

    def __init__(self):
        self.files = {}
        self.files['files'] = make_files()

    def get_file(self, path):
        if not path or path == "/":
            return self.files
        if path:
            return self.find_file(path)

    def put_file(self, path, filedata):
        # save file somehow
        pass

    def find_file(self,file):
        return self.files['files']['link'].find(str(file))