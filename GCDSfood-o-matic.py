'''
Name: Ellie Hochberg
Date: May 09, 2022
Description: A program that prints possible menu items from the GCDS Cafeteria
Features:
    1) Can generate up to 2 items from L1 and L3
    2) Does not repeat menu items
    3) Gives price of each menu item
    4) Stops generating items once a list is empty
Bugs: No bugs
Log: Submitted for grading on May 08, 2022
Plan:
    1) Ask for number of menu items
    2) Randomly generates how many items from L1 and L3 to have (either 1 or 2 items)
    3) Generate menu with that number of items
    4) Gives price of each menu item
    5) If a list becomes empty it stops generating items and tells you how many items were not able to be generated

Created on Apr 25, 2022

@author: EHochberg23
'''

import random


def main():
    L1 = ['Local', 'Roasted', 'Grilled', 'Garlic Mashed', 'Oven Dried', 'Spiced', 'Stewed', 'Assorted', 'Iced',
          'Sliced', 'Braised', 'Free-Range', 'Baby', 'Teriaki Glazed', 'Steamed']
    L2 = ['Cauliflower', 'Tilapia Fillet', 'Pork Loin', 'Green Beans', 'Basmati Rice', 'Rainbow Carrots',
          'Fingerling Potatoes', 'Three Color Squash', 'Potatoes', 'Eggplant', 'Drumstick', 'Short Rib', 'Duck Breast',
          'Eye Round of Beef', 'Baguette']
    L3 = ['with Fennel', 'Gratin', 'Bengali Style', 'with Peas', 'Pizza', 'with Balisamico',
          'with Garlic and Olive Oil', 'with Pigeon Peas', 'with Minted Yogurt', 'Soup', 'Chutney', 'Salad',
          'with Tropical Fruit Salsa', 'over Sticky Rice', 'au jus']

    P2 = [3, 5, 5, 3, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 1]  # L2 prices
    P3 = [0, 0, 0, 2, 0, 0, 0, 2, 3, 0, 0, 0, 2, 3, 0]  # L3 prices

    lunch = True
    while lunch == True:
        try:
            menu = int(input("How many menu items would you like?\n"))  # number of menu items requested
            lunch = False

        except:
            print("Please enter a number")  # a number was not entered
            lunch = True
            continue

    if menu < 0:
        print("Please input a positive number")
        main()

    '''
        The code below: 
        - Determines how many items from each list to have
        - It randomly chooses an item from each list, then removes the item from the list so it won't repeat
        - Determines the price of each individual item
        - Calculates total price of that menu item
        - When a list is empty the code stops and displays all menu items that were able to be generated and tells how many items were not able to be generated
    '''

    while menu > 0:  # run this code 'x' number of times to display 'x' number of menu items. Stop loop when menu = 0 or when a list is empty

        try:

            y = random.randint(0, 1)  # randomize how many items from L1
            z = random.randint(0, 1)  # randomize how many items from L3

            if y == 1 and z == 0:  # 2 items from L1 and 1 item from L3

                num1 = random.randint(0, len(L1) - 1)  # choose random number from 0 to the length of L1
                item1 = L1[int(num1)]  # item from L1
                L1.remove(item1)  # remove that item from L1 so it won't repeat items
                numx = random.randint(0, len(L1) - 1)  # choose another random number from 0 to the length of L1
                itemx = L1[int(numx)]  # that second item from L1
                num2 = random.randint(0, len(L2) - 1)  # choose random number from 0 to the length of L2
                item2 = L2[int(num2)]  # item from L2
                price2 = P2[int(num2)]  # price of that item
                num3 = random.randint(0, len(L3) - 1)  # choose random number from 0 to the length of L3
                item3 = L3[int(num3)]  # item from L3
                price3 = P3[int(num3)]  # price of that item

                caf_list = (item1 + " " + itemx + " " + item2 + " " + item3)  # menu item
                item_price = (price2 + price3)  # item price
                print(caf_list)
                print("Item price:", item_price, "dollars\n")
                L1.remove(itemx)  # remove second item from L1 so it won't repeat items
                L2.remove(item2)  # remove item from L2 so it won't repeat
                P2.remove(price2)  # remove price from P2 because it goes with the L2 item that was removed
                L3.remove(item3)  # remove item from L3
                P3.remove(price3)  # remove price from P3 that goes with the item from L3

                menu -= 1



            elif y == 1 and z == 1:  # 2 items from L1 and 2 items from L3

                num1 = random.randint(0, len(L1) - 1)
                item1 = L1[int(num1)]
                L1.remove(item1)
                numx = random.randint(0, len(L1) - 1)
                itemx = L1[int(numx)]
                num2 = random.randint(0, len(L2) - 1)
                item2 = L2[int(num2)]
                price2 = P2[int(num2)]
                num3 = random.randint(0, len(L3) - 1)
                item3 = L3[int(num3)]
                price3 = P3[int(num3)]
                L3.remove(item3)
                P3.remove(price3)
                numz = random.randint(0, len(L3) - 1)  # second random number from L3
                itemz = L3[int(numz)]  # second item from L3
                pricez = P3[int(numz)]  # price of that second item

                caf_list = (item1 + " " + itemx + " " + item2 + " " + item3 + " " + itemz)  # menu item
                item_price = (price2 + price3 + pricez)
                print(caf_list)
                print("Item price:", item_price, "dollars\n")
                L1.remove(itemx)
                L2.remove(item2)
                P2.remove(price2)
                L3.remove(itemz)  # remove second item from L3 to avoid repeats
                P3.remove(pricez)  # remove price from P3 that corresponds to the second item from L3

                menu -= 1


            elif y == 0 and z == 0:  # 1 item from L1 and 1 item from L3

                num1 = random.randint(0, len(L1) - 1)
                item1 = L1[int(num1)]
                num2 = random.randint(0, len(L2) - 1)
                item2 = L2[int(num2)]
                price2 = P2[int(num2)]
                num3 = random.randint(0, len(L3) - 1)
                item3 = L3[int(num3)]
                price3 = P3[int(num3)]

                caf_list = (item1 + " " + item2 + " " + item3)
                item_price = (price2 + price3)
                print(caf_list)
                print("Item price:", item_price, "dollars\n")
                L1.remove(item1)
                L2.remove(item2)
                P2.remove(price2)
                L3.remove(item3)
                P3.remove(price3)

                menu -= 1


            elif y == 0 and z == 1:  # 1 items from L1 and 2 items from L3

                num1 = random.randint(0, len(L1) - 1)
                item1 = L1[int(num1)]
                L1.remove(item1)
                num2 = random.randint(0, len(L2) - 1)
                item2 = L2[int(num2)]
                price2 = P2[int(num2)]
                num3 = random.randint(0, len(L3) - 1)
                item3 = L3[int(num3)]
                price3 = P3[int(num3)]
                L3.remove(item3)
                P3.remove(price3)
                numz = random.randint(0, len(L3) - 1)  # second random number from L3
                itemz = L3[int(numz)]  # second item from L3
                pricez = P3[int(numz)]  # price of that second item

                caf_list = (item1 + " " + item2 + " " + item3 + " " + itemz)  # menu item
                item_price = (price2 + price3 + pricez)
                print(caf_list)
                print("Item price:", item_price, "dollars\n")
                L2.remove(item2)
                P2.remove(price2)
                L3.remove(itemz)  # remove second item from L3 to avoid repeats
                P3.remove(pricez)  # remove price from P3 that corresponds to the second item from L3

                menu -= 1


        except:
            if len(L1) == 0 or len(L2) == 0 or len(L3):
                print("Here are all the items able to be generated.", abs(lunch - menu),
                      "menu items not able to be generated.")
                break


if __name__ == '__main__':
    main()


