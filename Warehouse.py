items = [
    {'name': 'Coca-Cola', 'quantity': 20, 'unit': 'bottle', 'unit_price': 2},
    {'name': 'water', 'quantity': 50, 'unit': 'bottle', 'unit_price': 1},
    {'name': 'beer', 'quantity': 10, 'unit': 'barrel', 'unit_price': 15}
    ]


def user_inputs():
    prompt = input("What would you like to do? ")
    return prompt


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



if __name__ == "__main__":
    while True:
        user = user_inputs()
        if user.lower() == 'exit':
            print("Exitting...bye!")
            exit()
        if user.lower() == 'show':
            get_items()
        if user.lower() == 'add':
            items.append(add_item())

#for item in dictionary:
#print(f"{item:>30}", end = '\n')
#print(get_items())