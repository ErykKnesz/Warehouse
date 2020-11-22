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
def products_list():
    form = ProductForm()
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
                           items=ITEMS,
                           form=form)


@app.route('/sell/<product_name>', methods=['GET', 'POST'])
def sell_product(product_name):
    form = ProductSaleForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            pass


if __name__ == '__main__':
    app.run(debug=True)