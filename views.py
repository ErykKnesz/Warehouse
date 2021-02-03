from flask import (Flask, render_template, request, redirect, url_for, flash,
                   make_response)
from products import warehouse, dashboard
from forms import ProductForm, ProductSaleForm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
headings = ['#', 'Name', 'Quantity', 'Unit', 'Unit Price']


@app.route('/')
def homepage():
    dashboard.create_graph()
    plot_url = 'static/dashboard.png'
    plt.savefig(plot_url)
    response = make_response(render_template("main.html"))
    if ('Cache-Control' not in response.headers):
        response.headers['Cache-Control'] = 'no-cache, no-store, \
        must-revalidate'
        response.headers['Pragma'] = 'no-cache'
    return response


@app.route('/products', methods=['GET', 'POST'])
def products_list():
    form = ProductForm()
    items = warehouse.show_stock()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.data.pop('csrf_token')
            warehouse.add_item(form.data)
            return redirect(url_for("products_list"))
        else:
            error = form.errors
            for field, problem in error.items():
                flash(f"{field}: {problem[0]}", 'danger')
    return render_template("product_list.html",
                           headings=headings,
                           items=items,
                           form=form)


@app.route('/sell/<product_name>', methods=['GET', 'POST'])
def sell_product(product_name):
    form = ProductSaleForm()
    item = warehouse.products[product_name]
    if request.method == 'POST':
        if form.validate_on_submit():
            form_quantity = form.data
            form_quantity.pop('csrf_token')
            quantity = warehouse.sell_item(
                form_quantity,
                product_to_sell=product_name
            )
            if quantity == 0:
                flash (f"Sold out all of {product_name}", 'success')
            else:
                flash (
                    f"Sold {form_quantity['quantity']} of {product_name}",
                    'success'
                ) 
            return redirect(url_for("products_list"))
    return render_template("sell_product.html",
                           form=form, 
                           item=item,
                           headings=headings[1:])


@app.route('/save', methods=['POST'])
def save_csv():
    if 'revenue' in request.headers['Referer']:
        warehouse.save_csv(sold=True)
        return redirect(url_for("revenue"))
    else:
        warehouse.save_csv(warehouse.products)
        return redirect(url_for("products_list"))


@app.route('/load', methods=['POST'])
def import_csv():
    if 'revenue' in request.headers['Referer']:
        warehouse.import_csv(sold=True)
        return redirect(url_for("revenue"))
    else:
        warehouse.import_csv()
        return redirect(url_for("products_list"))


@app.route('/revenue')
def revenue():
    items = warehouse.sold_items.values()
    revenue = warehouse.get_income()
    return render_template(
        'revenue.html',
        items=items,
        headings=headings,
        revenue=revenue)


if __name__ == '__main__':
    app.run(debug=True)