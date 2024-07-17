from flask import Flask


app = Flask(__name__,)
template_folder='templates'
static_folder='static'

@app.route('/home')
def home():
    return render_template("hello.html")

@app.route('/fortune')
def fortune():
    return render_template("hello.html")

if __name__ == '__main__':
    app.run(debug=True)

import random 
ul = random.randit(1,10)
print( your fortune is "ul")





