from flask import Flask
from flask import request, render_template
import os
import subprocess

reboot_app = Flask(__name__)

@reboot_app.route("/")
def index_function():
	return render_template('index.html')


def shutdown_server(mode):
        if mode==0:
    	    os.system('sudo shutdown -h now')
    	else:
    	    os.system('sudo reboot')

@reboot_app.route('/shutdown', methods=['POST'])
def shutdown():
	shutdown_server(0)
	return 'Server shutting down...'

@reboot_app.route('/reboot', methods=['POST'])
def reboot():
	shutdown_server(1)
	return 'Server reboot...'

if __name__=="__main__":
	reboot_app.run(host='0.0.0.0')

