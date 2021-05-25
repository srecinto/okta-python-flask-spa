import os
import json

from functools import wraps
from flask import Flask, request, send_from_directory, redirect, make_response, render_template

"""
GLOBAL VARIABLES ########################################################################################################
"""
app = Flask(__name__)
app.config.update({
    "SECRET_KEY": "9e93b0f6-d644-484a-986e-1991d244ffb6"  # For the session
    })


"""
UTILS ###################################################################################################################
"""


"""
ROUTES ##################################################################################################################
"""


@app.route('/<path:filename>')
def serve_static_html(filename):
    """ serve_static_html() generic route function to serve files in the 'static' folder """
    # print("serve_static_html('{0}')".format(filename))
    root_dir = os.path.dirname(os.path.realpath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)


@app.route('/')
def index():
    """ handler for the root url path of the app """
    print("index()")

    return serve_static_html("index.html")