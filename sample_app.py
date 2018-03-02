from flask import Flask
from flask import request
import os
import subprocess

first_app = Flask(__name__)

@first_app.route("/")
def first_function():
	return "<html><body><h1>Helle World</h1></body><html>"


def shutdown_server():
	#func = request.environ.get('werkzeug.server.shutdown')
	#if func is None:
	#	raise RuntimeError('Not running with the Werkzeug Server')
	#func()
	os.system('sudo shutdown -h now')
	#subprocess.call(['shutdown', '-h', 'now'], shell=False)

@first_app.route('/shutdown', methods=['POST'])
def shutdown():
	shutdown_server()
	return 'Server shutting down...'
if __name__=="__main__":
	first_app.run(host='0.0.0.0')

