from flask import Flask, request
from flask import render_template
from time import sleep
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', name=None)

@app.route('/sign_in.html', methods=['GET', 'POST'])
def load():
	if request.method == 'POST':
		username = request.form['session[username_or_email]']
		password = request.form['session[password]']
		return username + ' ' + password
	else:
		return render_template('sign_in.html', name=None)

if __name__ == '__main__':
	app.run()
