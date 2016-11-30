import os
from datetime import datetime
from flask import Flask, request, g, make_response, redirect, url_for,render_template

class Logger(object):

    def __init__(self,file='debug.log'):
        self.file = str(file)

    def add(self,type,link):

        self.link_to_req = link

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file), mode='a') as log_file:

            log_file.write("\n ------------------ \n")
            log_file.write(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + "\n")

            if type == 'response':
                log_file.write("Response to : " + self.last_req_link.method + "\n")
                log_file.write(str(self.link_to_req.status) + "\n")
                log_file.write(str(self.link_to_req.headers) + "\n")
                log_file.write("Data: " + self.link_to_req.data.decode() + "\n")

            if type == 'request':
                log_file.write("Request: \n")
                log_file.write((self.link_to_req.method) + "\n")
                log_file.write("RURI: " + str(self.link_to_req.url) + "\n \r")
                log_file.write("Headers: " + str(self.link_to_req.headers) + "\n \r")
                log_file.write("Data: " + str(self.link_to_req.data.decode().split('\n')))
                self.last_req_link = request

            log_file.close()

    def flush(self):
            with open( os.path.join( os.path.dirname( os.path.abspath(__file__) ), self.file),mode='w' ) as log_file:
                log_file.write('')
                log_file.close()

