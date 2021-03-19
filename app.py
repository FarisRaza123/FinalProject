from flask import Flask
from flask import request
from flask import render_template, make_response

app = Flask(__name__)

"""users = {'usernames':{'name':'bob'}
        'passwords':{'name':'spot'}}"""
users = {'username' : {'name':'bob', 'place':'lawn', 'animal':'man'},
              'password' : {'name':'spot', 'place':'bed', 'animal':'dog'}}
cart = {}

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    return render_template('register.html')
    print(dict_names)


@app.route('/order')
def order_page():
    return render_template('order.html')

@app.route('/success', methods = ['POST', 'GET'])
def success():
   if request.method == 'POST':
      result = request.form
      cart = request.args.get('type')
      print(cart)
      return render_template("success.html", result = result)

if __name__ == '__main__':
    app.run(debug=True)
