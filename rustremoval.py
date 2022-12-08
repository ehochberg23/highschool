"""
Name: Ellie Hochberg
Date: Sept 8, 2022
Description: This program determines the cost to mail an item
Features:
    1) Determines zone mail is in and is going to
    2) Determines whether item is unmailable or mailable
    3) Finds cost based off of number of zones and size of item
    4) Determines what the mail type it is
    5) Checks for invalid inputs such as characters, letters, and negative numbers
Bugs: No bugs
Log: Submitted for grading on Oct 3, 2022
Plan:
    1) Ask for measurements and zipcodes
    2) Determine how many zones the mail is going through
    3) Figure out which mailtype it is based off of the measurements
    4) Figure out cost based off mailtype and number of zones
    5) Return cost to mail
"""


def zone(zipcode):
    """
    Find which zone the zipcode is in
    Arguments:
        zipcode: Which zipcode the mail is in/going to
    Returns:
        Which zone those zipcodes are in
    """

    zipcode = int(zipcode)
    output = 0
    if zipcode > 00000 and zipcode < 7000:
        output = 1  # zone 1
    elif zipcode > 6999 and zipcode < 20000:
        output = 2  # zone 2
    elif zipcode > 19999 and zipcode < 36000:
        output = 3  # zone 3
    elif zipcode > 35999 and zipcode < 63000:
        output = 4  # zone 4
    elif zipcode > 62999 and zipcode < 85000:
        output = 5  # zone 5
    elif zipcode > 84999 and zipcode < 100000:
        output = 6  # zone 6
    else:
        output = 7  # unmailable
    return output


def mailtype(l, h, w):
    """
     Find which item is being mailed based off of its size
     Arguments:
         h: Height of item
         l: Length of item
         w: Width of item
     Returns:
         Which mailtype the item is
    """

    if (3.5 <= l <= 4.25) and (3.5 <= h <= 6.0) and (.007 <= w <= .016):
        type = 1  # regular post card
    elif (4.25 < l < 6) and (6 < h < 11.5) and (.007 <= w <= .015):
        type = 2  # large post card
    elif (3.5 <= l <= 6.125) and (5 <= h <= 11.5) and (.016 < w < .25):
        type = 3  # envelope
    elif (6.125 < l < 24) and (11 <= h <= 18) and (.25 <= w <= .5):
        type = 4  # large envelope
    elif (l > 24) and (h > 11) and (w > .5) and (2 * w + 2 * h + l < 84):
        type = 5  # package
    elif 84 < 2 * w + 2 * h + l < 130:
        type = 6  # large package
    else:
        type = 7  # unmailable
    return type


def getCost(type, totalzones):
    """
    Determine the cost to mail based off of how many zones the mail is going through
    Arguments:
        type: Which mail type
        totalzones: How many zones the mail is going through
    Returns:
        Cost to mail the item
    """

    cost = 0
    if type == 1:  # post card
        cost = .20 + (.03 * totalzones)
    elif type == 2:  # large post card
        cost = .37 + (.03 * totalzones)
    elif type == 3:  # envelope
        cost = .37 + (.04 * totalzones)
    elif type == 4:  # large envelope
        cost = .60 + (.05 * totalzones)
    elif type == 5:  # package
        cost = 2.95 + (.25 * totalzones)
    elif type == 6:  # large package
        cost = 3.95 + (.35 * totalzones)
    else:
        cost = "UNMAILABLE"
    return cost


def main():
    """
    Determine cost to mail an item
    Arguments:
        N/A
    Returns:
        N/A
    """

    go = 5
    while go > 0:

        while True:
            try:
                user_inputs = input("Enter length, height, width, from zipcode, and to zipcode:").split(",")
                l = float(user_inputs[0])
                h = float(user_inputs[1])
                w = float(user_inputs[2])
                from_zip = float(user_inputs[3])
                to_zip = float(user_inputs[4])

                if l < 3.5 or w < .007 or h < 3.5 or from_zip < 1 or to_zip < 1:  # if numbers out of range, create error so that it goes to the except
                    l = l / 0
                break

            except:
                print(
                    "Invalid, please enter valid, positive numbers and use commas between each number and make sure to enter all 5 inputs")

        type = mailtype(l, h, w)  # which mail type based off of length, width, height

        if zone(to_zip) == 7 or zone(from_zip) == 7:  # zipcode isn't in a zone
            print("UNMAILABLE")


        else:
            total_zones = abs(zone(to_zip) - zone(from_zip))  # how many zones its going through
            total_cost = getCost(type, total_zones)  # total cost to mail
            dollars = '${:,.2f}'.format(total_cost)
            print("Cost to mail is:", dollars)

        go -= 1


if __name__ == '__main__':
    main()
