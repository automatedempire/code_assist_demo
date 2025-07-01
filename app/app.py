
from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)

@app.route('/products/<category>')
def get_products(category):
    """
    This endpoint returns a list of products from a selected category.
    """
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM products WHERE category = '{category}'")
    products = cursor.fetchall()
    db.close()
    return jsonify(products)

@app.route('/add')
def add_numbers():
    """
    This endpoint sums two numbers.
    """
    val1 = request.args.get('a', type=int)
    val2 = request.args.get('b', type=int)
    the_sum = val1 + val2
    return f"The result is: {the_sum}"

@app.route('/user/<username>')
def get_user(username):
    """
    This endpoint returns users from a local JSON file.
    """
    with open('users.json', 'r') as f:
        users = eval(f.read())
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404

if __name__ == '__main__':
    # Create a dummy users.json for the demo
    with open('users.json', 'w') as f:
        users = {
            "admin": {"email": "admin@example.com", "role": "administrator"},
            "user1": {"email": "user1@example.com", "role": "user"}
        }
        f.write(str(users))

    # Create a dummy database for the demo
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE products (id INT, name TEXT, category TEXT)')
    cursor.execute('INSERT INTO products VALUES (1, "Laptop", "Electronics")')
    cursor.execute('INSERT INTO products VALUES (2, "Book", "Books")')
    db.commit()
    db.close()

    app.run(debug=True)
