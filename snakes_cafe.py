def main():
    menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

"""
    menuItems = {
        "Wings": 0, "Cookies": 0, "Spring Rolls": 0,
        "Salmon": 0, "Steak": 0, "Meat Tornado": 0, "A Literal Garden": 0,
        "Ice Cream": 0, "Cake": 0, "Pie": 0,
        "Coffee": 0, "Tea": 0, "Unicorn Tears": 0,
    }

    print(menu)

    order = input("""***********************************
** What would you like to order? **
***********************************

Order: """)

    while order != "quit":
        if order in menuItems:
            menuItems[order] += 1
            order = input(f"""You ordered {menuItems[order]} {order}, would you like anything else?

Order: """)
        elif order != menuItems:
            print("Sorry, I dont recognize that item...")
            order = input("Order: ")
        # elif order == "submit":
        #     print(f"Your full order is {menuItems[order]} orders of {order}.")
        #     order = input("Order: ")
        # elif order == "quit":
        #     print("Thanks for stopping by!")
        #     break


if __name__ == "__main__":
    main()
