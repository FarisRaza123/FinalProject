from flask import Flask
from flask import request
from flask import render_template, make_response
import sqlite3


conn = sqlite3.connect('/tmp/data.db')

c = conn.cursor()

c.execute("""Create Table side_food (
            first itemid,
            last food_name,
            price integer)""")

c.execute("INSERT INTO side_food VALUES ('BowlsOfPasta', 'Bowls Of Pasta', 10.99)")

conn.commit()
conn.close()



app = Flask(__name__)


side_items = [
    {'itemid': 'BowlsOfPasta', 'name': 'Bowls of Pasta', 'price': 10.99},
    {'itemid': 'NumberOfBreadsticks', 'name': 'Number of Breadsticks', 'price': 7.99},
    {'itemid': 'NumberOfWings', 'name': 'Number of Wings', 'price': 10.99},
    {'itemid': 'NumberOfGarlicBread', 'name': 'Number of Garlic Bread', 'price': 5.99},
    {'itemid': 'NumberOfMozzarellaSticks', 'name': 'Number of Mozzarella Sticks', 'price': 3.99},
    {'itemid': 'NumberOfCheeseFries', 'name': 'Number of Cheese Fries', 'price': 6.99},
    {'itemid': 'NumberOfOrganicSalad', 'name': 'Number of Organic Salad', 'price': 9.99},
    {'itemid': 'NumberOfCoke', 'name': 'Number of Coke', 'price': 1.99},
    {'itemid': 'NumberOfSprite', 'name': 'Number of Sprite', 'price': 1.99}
]

pizzas = [
    {'itemid': 'small', 'name': 'Small Pizza', 'price': 10.99},
    {'itemid': 'medium', 'name': 'Medium Pizza', 'price': 12.99},
    {'itemid': 'large', 'name': 'Large Pizza', 'price': 15.99}
]

toppings = [
    {'itemid': 'pepperoni', 'name': 'Pepperoni', 'price': 2.99},
    {'itemid': 'mushroooms', 'name': 'Mushroooms', 'price': 1.99},
    {'itemid': 'jalepeno', 'name': 'Jalepeno', 'price': 1.99},
    {'itemid': 'olives', 'name': 'Olives', 'price': 2.99},
    {'itemid': 'pineapples', 'name': 'Pineapples', 'price': 3.99}
]



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    return render_template('register.html')

@app.route('/order')
def order_page():
    return render_template('order.html', items=side_items, pizzas = pizzas, toppings = toppings)

@app.route('/success', methods = ['POST', 'GET'])
def success():
   if request.method == 'POST':
      result = request.form

      cart = {}
      total_cost = 0.0
      for item in side_items:
        num_of_items = int(result.get(item['itemid']))
        cart[item['itemid']] = num_of_items
        total_cost = total_cost + (num_of_items * item['price'])

      for topping in toppings:
        num_of_toppings = int(result.get(topping['itemid']))
        cart[topping['itemid']] = num_of_toppings
        total_cost = total_cost + (num_of_toppings * topping['price'])

      for pizza in pizzas:
        num_of_pizzas = int(result.get(pizza['itemid']))
        cart[pizza['itemid']] = num_of_pizzas
        total_cost = total_cost + (num_of_pizzas * pizza['price'])

      total_cost_rounded = str(round(total_cost,2))

      return render_template("success.html", result=result, total=total_cost_rounded)


if __name__ == '__main__':
    app.run(debug=True)
