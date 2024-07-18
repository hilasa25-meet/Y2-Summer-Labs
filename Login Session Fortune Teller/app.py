from flask import Flask, render_template, request
from flask import session as login_session
import random
app = Flask(__name__,)


template_folder='templates'
static_folder='static'

app.config['SECRET_KEY'] = "Your_password"

@app.route('/login', methods=['GET', 'POST'])
    def login():
   if request.method == 'POST':
       username = request.form['username']
       if username == 'admin':
           login_session['admin'] = True
       return redirect(url_for('home'))
   return render_template("login.html")

@app.route('/fortune')
def fortune():
    return render_template("fortune.html")


class theusersfortune({{fortune}}):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        

@app.route('/fortune')
def fortune():
    return render_template("fortune.html")

    
print("your fortune is {{fortune}}!! you are now in the final page.")


@app.route('/home')
def home():
    return render_template("hello.html")

@app.route('/fortune')
def fortune():
    return render_template("fortune.html")

if __name__ == '__main__':
    app.run(debug=True)

import random 
ul = random.randit(1,10)
print( your fortune is "ul")





