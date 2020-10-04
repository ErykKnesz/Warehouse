items = [
    {'name': 'Coca-Cola', 'quantity': 20, 'unit': 'bottle', 'unit_price': 2},
    {'name': 'water', 'quantity': 50, 'unit': 'bottle', 'unit_price': 1},
    {'name': 'beer', 'quantity': 10, 'unit': 'barrel', 'unit_price': 15}
    ]

sold_items = []


def get_items():
    headings = f"{'Name':<20}{'Quantity':<20}{'Unit':<20}\
        {'Unit Price (PLN)':<20}"
    print(headings)
    for i in items:
        for j in i.values():
            print(j, end=f"{'':<20}")
        print('', end='\n')

    return None


def add_item():
    dictionary = {
        'name': input("Please provide product name: "),
        'quantity': input("Please provide product quantity: "),
        'unit': input("Please provide unit name: "),
        'unit_price': input("Please provide unit price: ")
        }
    return dictionary


def sell_item(name_to_sell, quantity_to_sell):
    for dictionary in items:
        stock_name = dictionary.get('name')
        if name_to_sell == stock_name.lower():   
            stock_quantity = dictionary.get('quantity')
            dictionary['quantity'] = stock_quantity - quantity_to_sell
            sold_items.append(
                {
                    'name': name_to_sell,
                    'quantity': quantity_to_sell,
                    'unit': dictionary['unit'], 
                    'unit_price': dictionary['unit_price']
                }
                )


def get_costs():
     return

def menu():
    # prompts user to state desired action and proceeds accordingly
    user = input("What would you like to do? ")
    if user.lower() == 'exit':
            print("Exitting...bye!")
            exit()
    if user.lower() == 'show':
        get_items()
    if user.lower() == 'add':
        items.append(add_item())
        print("Congrats! New item added. See the new stock-status")
        get_items()
    if user.lower() == 'sell':
        name_to_sell = input("Which product to sell?").lower()
        quantity_to_sell = int(input("How much to sell?"))
        sell_item(name_to_sell, quantity_to_sell)
        print("Sell action completed! See the new stock-status!")
        get_items()
        print(f"Here's what you sold already! \n {sold_items}")


if __name__ == "__main__":
    while True:
        menu()
        