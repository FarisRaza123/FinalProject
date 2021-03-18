from flask import Flask
from flask import request
from flask import render_template, make_response

app = Flask(__name__)

users = {}
cart = {}

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    return render_template('register.html')

@app.route('/your_flask_funtion')
def get_ses():
    cart = request.form['breadsticks']
    print(cart)
    return make_response('success.html', 200)

@app.route('/order')
def order_page():
    return render_template('order.html')

@app.route('/success')
def success_page():
    cost = 15
    return render_template('success.html', title='Welcome', username=cost)

if __name__ == '__main__':
    app.run(debug=True)
