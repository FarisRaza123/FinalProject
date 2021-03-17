from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

cart = {}

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/order')
def order_page():
    return render_template('order.html')

@app.route('/success')
def success_page():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
