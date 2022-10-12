menu = {
    1: "Goulash Soup",
    2: "Chicken Soup",
    3: "Beef Stew with Spatzle",
    4: "Stuffed cabbage",
    5: "Somlauer Nockerln",
    6: "Pancakes"
}

order = []


def find_index(option):
    for item in menu.items():
        if option == item[1]:
            return item[0]
            break


def see_menu():
    print('MENU:')
    for item in menu.items():
        print(f'   Item {item[0]}: {item[1]}')
    print('')


def add_order():
    while True:
        if len(order) == 3:
            print('Order completed!')
            print('')
            break
        else:
            option = input('Enter order number (enter 0 to finish order): ')
            if option == '0':
                print('')
                break
            else:
                try:
                    if int(option) in menu.keys():
                        order.append(menu[int(option)])
                    else:
                        print('INVALID OPTION!')
                        continue
                except:
                    if option.lower().title() in menu.values():
                        order.append(menu[find_index(option.lower().title())])
                    else:
                        print('INVALID OPTION!')
                        continue


def see_order():
    if len(order) == 0:
        print('Your order is empty.')
    else:
        print('Your current order is:')
        for item in menu.items():
            if order.count(item[1]) != 0:
                print(f'   {order.count(item[1])} {item[1]}')
    print('')


while True:
    print('Tasks available:\n   1: see menu\n   2: order\n   3: see current order\n   4: Exit')
    task = input('Please choose task : ')
    print('')
    if task == '1':
        see_menu()
    elif task == '2':
        add_order()
    elif task == '3':
        see_order()
    elif task == '4':
        break
    else:
        print('INVALID TASK!')
        continue
