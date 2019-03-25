import os
import threading

def run_npm():
	os.system("npm run dev")
def run_flask():
	os.system("export FLASK_APP=src/finder/finder.py;python3 -m flask run")
	
npm = threading.Thread(target = run_npm)
flask = threading.Thread(target = run_flask)

npm.start()
flask.start()
