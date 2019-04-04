import os
import threading
from screeninfo import get_monitors
import webview
width = 0
height = 0
for m in get_monitors():
	width = m.width-20
	height = m.height-20

def run_npm():
	
	print("WELCOME TO MUSICK")	
	print("Report Bugs Here: https://github.com/pythongiant/skrrt/issues")
	w = webview.WebView(width=width, height=width, title="Musick", url="file://"+os.getcwd()+"/index.html", resizable=True, debug=False)
	
	w.run()
def run_flask():
	os.system("export FLASK_APP=src/finder/finder.py;python3 -m flask run;clear")
	
npm = threading.Thread(target = run_npm)
flask = threading.Thread(target = run_flask)

npm.start()
flask.start()
