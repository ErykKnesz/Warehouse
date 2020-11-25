from flask import Flask, render_template, request, redirect, url_for, flash
from products import Product, ITEMS
from forms import ProductForm, ProductSaleForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
headings = ['#', 'Name', 'Quantity', 'Unit', 'Unit Price']


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/products', methods=['GET', 'POST'])
def products_list(items=ITEMS):
    form = ProductForm()
    items = items.values()
    if request.method == 'POST':
        if form.validate_on_submit():
            Product.add_item(form.data)
            return redirect(url_for("products_list"))
        else:
            error = form.errors
            for field, problem in error.items():
                flash(f"{field}: {problem[0]}")
    return render_template("product_list.html",
                           headings=headings,
                           items=items,
                           form=form)


@app.route('/sell/<product_name>', methods=['GET', 'POST'])
def sell_product(product_name):
    form = ProductSaleForm()
    item = ITEMS[product_name]
    if request.method == 'POST':
        if form.validate_on_submit():
            quantity = form.data
            quantity.pop('csrf_token')
            Product.sell_item(quantity, product_to_sell=product_name)
            flash("Please enter a valid email address", 'error')
            flash (f"Sold {quantity['quantity']} of {product_name}") 

            return redirect(url_for("products_list"))
    return render_template("sell_product.html",
                           form=form, 
                           item=item,
                           headings=headings[1:])


@app.route('/save', methods=['POST'])
def save_csv():
    Product.save_csv(ITEMS)
    return redirect(url_for("products_list"))


@app.route('/load', methods=['POST'])
def import_csv():
    return products_list(items=Product.import_csv())


if __name__ == '__main__':
    app.run(debug=True)
    #FLASK_ENV=development