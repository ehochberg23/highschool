'''
Name: Ellie Hochberg
Date: March 10, 2022
Description: Read a txt file, turn it into a dictionary and convert into a CSV file
Bugs: No bugs
'''

import csv


def main():
    """
    Read a txt file, turn it into a dictionary and convert into a CSV file
    Arguments:
        N/A
    Returns:
        N/A
    """

    """
    BELOW IS CODE FOR ROMEO AND JULIET
    """
    file = open("romeoandjuliet.txt", "r")  # open txt file

    counts1 = dict()

    for line in file:  # for each line
        print(line)
        words1 = line.split()  # split line by each word

        # to count the number of each word
        for word1 in words1:  # for each word in each line
            if word1 not in counts1:  # if new word
                counts1[word1] = 1
            else:  # add up the words
                counts1[word1] += 1

    romcsv = open('ROM_CSV.csv', 'w')  # convert to CSV
    for key, value in counts1.items():
        if value > 20:  # if value is less than 0
            romcsv.write(key + "," + str(value) + "\n")  # delete that word from dictionary

    """
    BELOW IS CODE FOR ALLS WELL THAT ENDS WELL
    """

    file = open("ALLS.txt", "r")  # open txt file

    counts2 = dict()

    for line in file:  # for each line
        print(line)
        words2 = line.split()  # split line by each word

        # to count the number of each word
        for word2 in words2:  # for each word in each line
            if word2 not in counts2:  # if new word
                counts2[word2] = 1
            else:  # add up the words
                counts2[word2] += 1

    allcsv = open('ALL_OUT.csv', 'w')  # convert to CSV
    for key, value in counts2.items():
        if value > 20:  # if value is less than 0
            allcsv.write(key + "," + str(value) + "\n")  # delete that word from dictionary


if __name__ == '__main__':
    main()
