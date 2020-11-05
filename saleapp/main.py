from flask import render_template, request
from saleapp import app, utils


@app.route("/")
def index():
    categories = utils.ReadData()
    return render_template('index.html', categories=categories)


@app.route('/products')
def product_list():
    cat_id = request.args.get('category_id')
    products = utils.read_product(cat_id)
    return render_template('product_list.html', products=products)


@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = utils.get_product_by_id(product_id)
    return render_template('product_detail.html', product=product)


if __name__ == "__main__":
    app.run(debug=True)