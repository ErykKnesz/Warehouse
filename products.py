from decimal import Decimal
import csv
import copy
import matplotlib.pyplot as plt


class Product:
    def __init__(self, name, unit, unit_price, quantity):
        self.name = name
        self.unit = unit
        self.unit_price = Decimal(unit_price)
        self.quantity = Decimal(quantity)

    def __str__(self):
        return f"{self.name} {self.unit} {self.unit_price} {self.quantity}"


item_1 = Product(
    name='apple juice', unit='l', unit_price=1.99, quantity=45.03)
item_2 = Product(
    name='cake flour', unit='kg', unit_price=1.23, quantity=644.09)


class Warehouse:
    def __init__(self, products, sold_items):
        if isinstance(products, dict) and isinstance(sold_items, dict):
            self.products = products
            self.sold_items = sold_items
        else:
            raise TypeError("self.products is not a dict instance")

    def show_stock(self):
        return self.products.values()

    def add_item(self, item):
        if item['name'] not in self.products.keys():
            new_product = Product(
                name=item['name'], unit=item['unit'],
                unit_price=item['unit_price'], quantity=item['quantity']
            )
            self.products[new_product.name] = new_product
        else:
            new_quantity = (item['quantity'] +
                            self.products[item['name']].quantity)
            self.products[item['name']] = Product(
                name=item['name'], unit=item['unit'],
                unit_price=item['unit_price'], quantity=new_quantity
            )
        return

    def sell_item(self, form, product_to_sell):
        if product_to_sell in self.products.keys():
            product_to_sell = self.products.get(product_to_sell)
            if product_to_sell.quantity - form['quantity'] < 0:
                form['quantity'] = product_to_sell.quantity
            new_quantity = product_to_sell.quantity - form['quantity']
            product_to_sell.quantity = new_quantity
            self.products[product_to_sell.name] = product_to_sell
            sold_product = copy.deepcopy(product_to_sell)
            sold_product.quantity = form['quantity']
            self.sold_items[sold_product.name] = sold_product
        return

    def get_costs(self):
        costs = map(
            lambda item: item.quantity * item.unit_price,
            self.products.values()
        )
        return sum(costs)

    def get_income(self, margin=2):
        revenue = map(
            lambda item: item.quantity * item.unit_price * margin,
            self.sold_items.values()
        )
        return sum(revenue)

    def get_profit(self):
        costs = self.get_costs()
        revenue = self.get_income()
        profit = revenue - costs
        return round(profit, 2)

    def save_csv(self, sold=False):
        if not sold:
            filename = "warehouse.csv"
            items = self.products
        else:
            filename = "sold items.csv"
            items = self.sold_items
        with open(f"{filename}", "w", newline='') as f:
            field_names = ['name', 'unit', 'unit_price', 'quantity']
            products = [product for product in items.values()]
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            for product in products:
                writer.writerow(
                    {
                        'name': product.name,
                        'unit': product.unit,
                        'unit_price': product.unit_price,
                        'quantity': product.quantity
                    }
                )

    def import_csv(self, sold=False):
        if not sold:
            filename = "warehouse.csv"
            self.products.clear()
            items = self.products
        else:
            filename = "sold items.csv"
            self.sold_items.clear()
            items = self.sold_items
        with open(f"{filename}", "r", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                items[row['name']] = Product(
                    name=row['name'],
                    unit=row['unit'],
                    unit_price=row['unit_price'],
                    quantity=row['quantity']
                )
        return items


class Dashboard(Warehouse):
    def __init__(self, *args):
        super().__init__(*args)

    def create_graph(self):
        self.bar_stock = sum(map(
                lambda item: item.quantity,
                self.products.values()
        ))
        self.bar_sold = sum(map(
                lambda item: item.quantity,
                self.sold_items.values()
        ))
        bars = [self.bar_stock, self.bar_sold]
        names = ['in stock', 'sold']
        return plt.bar(names, bars)


ITEMS = {
    item_1.name: item_1,
    item_2.name: item_2,
}
SOLD_ITEMS = {}

warehouse = Warehouse(ITEMS, SOLD_ITEMS)
dashboard = Dashboard(warehouse.products, warehouse.sold_items)