import sys
import flask
import gevent
from flask_sockets import Sockets
from flask import Flask, render_template

port=sys.argv[1]
app = Flask(__name__)
app.debug = 'DEBUG' in os.environ
sockets = Sockets(app)

@app.route('/')
def hello():
    return app.send_static_file('index.html')

@sockets.route('/socket')
def inbox(ws):
    while not ws.closed:
        gevent.sleep(0.1)
        message = ws.receive()
        if message:
        	print(message)
        	ws.send("Hello")