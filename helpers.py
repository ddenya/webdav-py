from flask import Flask, request, g, make_response, redirect, url_for,render_template
from files import make_files

# def parse_propfind(request):
#
#     method = request.method
#
#     # Determine depth for request:
#     # depth may be 0,1,infinite.
#     # infinite is not implemented and it seems that is not used by Microsoft MiniRedir
#     # returns response type
#
#     # First time MiniRedir connects - calls PROPFIND with Depth == 0
#     # When client lists a directory - it uses depth 1
#
#     print("Parse_propfind got: " + str(method))
#
#     depth = request.headers['Depth']
#
#     print("Parse_propfind depth: " + str(depth))
#
#
#     if depth == '0':
#         template = render_template('propfind_depth_0.xml')
#         response = make_response(template)
#
#     elif depth == '1':
#         template = render_template('propfind_depth_1.xml')
#         response = make_response(template)
#
#     response.headers['Content-Type'] = 'application/xml'
#     response.status = '207 MultiStatus'
#
#     print("I made files:" + str(make_files()))
#
#     return response


def parse_propfind(request):

    files = make_files()
    depth = request.headers['Depth']
    files['depth'] = depth
    template = render_template('propfind_file_generated.xml',values=files)
    response = make_response(template)
    return response
