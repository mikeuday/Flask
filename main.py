from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to Flask application...."

@app.route('/add/<int:a>/<int:b>', methods = ['GET','POST'])
def addition(a, b):
    a = a
    b = b
    c = a+b
    return " sum of a and b is "+ str(c)





if __name__ =='__main__':
    app.run()