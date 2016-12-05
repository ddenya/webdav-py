import os
from datetime import datetime
from flask import Flask, request, g, make_response, redirect, url_for,render_template

class Logger(object):

    def __init__(self,file='debug.log'):
        self.file = str(file)

    def add(self,type,link):

        # Should be placed in every method, because if placed in __init__ - file gets closed(?) after __init__
        # even if I did not close it
        self.log_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file), mode='a')
        self.link_to_req = link

        if type == 'response':
            self.log_file.write("Response to : " + self.last_req_link.method + "\n")
            self.log_file.write(str(self.link_to_req.status) + "\n")
            self.log_file.write(str(self.link_to_req.headers) + "\n")
            self.link_to_req.direct_passthrough = False
            self.log_file.write("Data: " + self.link_to_req.get_data(as_text=True) + "\n")

        if type == 'request':
            self.log_file.write("Request: \n")
            self.log_file.write((self.link_to_req.method) + "\n")
            self.log_file.write("RURI: " + str(self.link_to_req.url) + "\n \r")
            self.log_file.write("Headers: " + str(self.link_to_req.headers) + "\n \r")
            self.log_file.write("Data: " + str(self.link_to_req.data.decode().split('\n')))
            self.last_req_link = request

    def flush(self):
            with open( os.path.join( os.path.dirname( os.path.abspath(__file__) ), self.file),mode='w' ) as log_file:
                log_file.write('')
                log_file.close()

    def add_custom(self,data):
        self.log_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file), mode='a')
        self.log_file.write("/n" + str(data) + "/n")
