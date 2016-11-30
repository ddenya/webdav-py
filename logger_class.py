import os
from datetime import datetime
from flask import Flask, request, g, make_response, redirect, url_for,render_template

class Logger(object):

    def __init__(self,file='debug.log'):
        self.file = str(file)

    def add(self,type,link):

        self.link_to_req = link

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file), mode='w') as log_file:
            log_file.write(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + "------------------ \n" )

            if type == 'response':
                log_file.write(str(self.link_to_req.status) + "\n \r")
                log_file.write(str(self.link_to_req.status) + "\n \r")
                log_file.write(str(self.link_to_req.headers) + "\n \r")
                bytesdecoded = self.link_to_req.data.decode()
                log_file.write("Data: " + bytesdecoded )
            if type == 'self.link_to_req':
                log_file.write((self.link_to_req.method) + "\n \r")
                log_file.write("RURI: " + str(self.link_to_req.url) + "\n \r")
                log_file.write("Headers: " + str(self.link_to_req.headers) + "\n \r")
                bytesdecoded = self.link_to_req.data.decode()
                log_file.write("Data: " + str(bytesdecoded.split('\n')))

    def flush(self):
            with open( os.path.join( os.path.dirname( os.path.abspath(__file__) ), self.file),mode='w' ) as log_file:
                log_file.write('')
                log_file.close()

