from flask import Flask, render_template, request
from flask import session as login_session
import pyrebase

app.config['SECRET_KEY'] = 'super-secret-key'

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()

app = Flask(__name__)

app.route('/')
def main_page():
    return render_template("signup.html")
	

@app.route('/signin')
def signin_page():
	return render_template("home.html")

app.route('/home')
def home_page():
	return render_template("signin.html")

app.route('/thanks')
def thanks_page():
	return render_template("home.html")

app.route('/display')
def display_page():
	return render_template('quotes')

app.route('/signout')
def signout_page():
	return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
       		login_session['user'] = 
			auth.create_user_with_email_and_password(email, password)
           return redirect(url_for('home_page'))
       		except:
           error = "Opsi, login failed"
   			return render_template("signup.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
       		login_session['user'] = 
			auth.create_user_with_email_and_password(email, password)
           return redirect(url_for('home'))
       		except:
           error = "Opsi, login failed"
   			return render_template("signin.html")


def quotes():
    quotes = ["Quote:"] 
    return render_template(
"display.html",
quote=quotes)




quotes = ["Quote:"]




if __name__ == '__main__':
    app.run(debug = True)
