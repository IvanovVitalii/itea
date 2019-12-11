from flask import (Flask,
                   render_template,
                   request)
from task_7.ContextManagerSQLite import ContextManagerSQLite

app = Flask(__name__)


@app.route('/ventportal/product-category')
def categories():
    category = []
    with ContextManagerSQLite('product.db') as s:
        query_response = s.execute('SELECT category FROM categories ')
        for c in query_response:
            category += c
    title = 'VentPortal'
    return render_template('category.html',
                           title=title,
                           category=category)


@app.route('/ventportal/product-category/<string:category>')
def products(category):
    products = []
    with ContextManagerSQLite('product.db') as s:
        sql = f'SELECT product FROM products ' \
              f'INNER JOIN categories ' \
              f'ON products.id_category=categories.id ' \
              f'WHERE category="{category}" AND quantity <> 0 '
        query_response = s.execute(sql)
        for p in query_response:
            products += p
    title = 'VentPortal'
    return render_template('products.html',
                           title=title,
                           category=category,
                           products=products)


@app.route('/ventportal/product-category/<string:category>/<string:products>')
def product(category, products):
    with ContextManagerSQLite('product.db') as s:
        sql = f'SELECT product, price, description, quantity ' \
              f'FROM products ' \
              f'INNER JOIN categories ' \
              f'ON products.id_category=categories.id ' \
              f'WHERE category="{category}" AND product="{products}" '
        query_response = s.execute(sql)
        for p in query_response:
            p_product, p_price, p_description, p_quantity = p
            p_productl = p_product
            p_pricel = p_price
            p_descriptionl = p_description
            p_quantityl = p_quantity
    title = 'VentPortal'
    return render_template('product.html',
                           title=title,
                           category=category,
                           products=products,
                           p_product=p_productl,
                           p_price=p_pricel,
                           p_description=p_descriptionl,
                           p_quantity=p_quantityl)


@app.route('/ventportal/product-category/<string:category>/<string:products>/Buy')
def buy(category, products):
    with ContextManagerSQLite('product.db') as s:
        sql = f'SELECT product, price ' \
              f'FROM products ' \
              f'WHERE product="{products}" '
        query_response = s.execute(sql)
        for p in query_response:
            p_product, p_price = p
            p_productl = p_product
    title = 'VentPortal'
    return render_template('buy.html',
                           title=title,
                           category=category,
                           products=products,
                           p_product=p_productl)


@app.route('/ventportal/admin')
def categories_admin():
    category = []
    with ContextManagerSQLite('product.db') as s:
        query_response = s.execute('SELECT category FROM categories ')
        for c in query_response:
            category += c
    title = 'VentPortal'
    return render_template('admin.html',
                           title=title,
                           category=category)


@app.route('/ventportal/admin/add-category', methods=['POST', 'GET'])
def add_category():
    if request.method == 'POST':
        new_category = request.form['new_category']
        with ContextManagerSQLite('product.db') as s:
            sql = f'INSERT INTO categories (category) VALUES (?)'
            s.execute(sql, [new_category])
    title = 'VentPortal'
    return render_template('add_category.html',
                           title=title)


@app.route('/ventportal/admin/add-product', methods=['POST', 'GET'])
def add_product():
    category = {}
    with ContextManagerSQLite('product.db') as s:
        query_response = s.execute('SELECT id, category FROM categories ')
        for c in query_response:
            (c_id, c_category) = c
            category.update({c_id: c_category})
    if request.method == 'POST':
        new_product = request.form['new_product']
        price = request.form['price']
        description = request.form['description']
        quantity = request.form['quantity']
        id_category = request.form['id_category']
        with ContextManagerSQLite('product.db') as s:
            sql = f'INSERT INTO products (product, price, description, quantity, id_category) VALUES (?, ?, ?, ?, ?)'
            s.execute(sql, [new_product, price, description, quantity, id_category])
    title = 'VentPortal'
    return render_template('add_product.html',
                           title=title,
                           category=category)


if __name__ == '__main__':
    app.run(debug=True)
