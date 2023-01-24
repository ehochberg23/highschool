
"""
PROBLEM STATEMENT:
Given 3 positive integers, n, b, and s, generate the next n numbers in base b starting with sin the given base.
We guarantee that the base will be between 2 and 9 inclusive.
We guarantee that s is a valid number in base b. Find the base 10 value for the number of times the largest possible digit in the given base is found among all of the digits in the numbers generated.

EXAMPLE:
If n=15, b=8, and 5-2, the numbers generated are 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20.
The largest possible digit in base 8 is 7 which occurs 2 times.

TASK:
Complete the function countLargestDigit:
    The function has 3 parameters: an integer, num, representing the number of values to be found, an integer, base, representing the base to be used between 2 and 9 inclusive, and an integer, start, representing the starting value in the base given
    The function returns a base 10 number representing the number of times the largest possible digit in the given base is found among all of the digits in the numbers generated
You may create additional functions that are called from countLargestDigit if needed in solving the problem.
"""




#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countLargestDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num
#  2. INTEGER base
#  3. INTEGER start
#


def countLargestDigit(num, base, start):
    decimalvalue = 0
    start = str(start)
    for i in range(len(start)):
        decimalvalue += int(start[i]) * (base ** (len(start) - i - 1))
    start = decimalvalue
    list = []
    for i in range(num):
        list.append(start)
        start += 1
    # return list

    if base == 2:
        base2_nums = []
        for number in list:
            base2_num = ""
            while number > 0:
                remainder = number % 2
                base2_num = str(remainder) + base2_num
                number = number // 2
            base2_nums.append(base2_num)

        split_numbers = []
        for yas in base2_nums:
            digits = [int(digit) for digit in str(yas)]
            split_numbers.extend(digits)

        i = 1
        for i in split_numbers:
            return split_numbers.count(1)

    elif base == 3:
        base3_nums = []
        for number in list:
            base3_num = ""
            while number > 0:
                remainder = number % 3
                base3_num = str(remainder) + base3_num
                number = number // 3
            base3_nums.append(base3_num)
        split_numbers = []
        for yas in base3_nums:
            digits = [int(digit) for digit in str(yas)]
            split_numbers.extend(digits)
        i = 2
        for i in split_numbers:
            return split_numbers.count(2)

    elif base == 4:
        base4_nums = []
        for number in list:
            base4_num = ""
            while number > 0:
                remainder = number % 4
                base4_num = str(remainder) + base4_num
                number = number // 4
            base4_nums.append(base4_num)
        split_numbers = []
        for yas in base4_nums:
            digits = [int(digit) for digit in str(yas)]
            split_numbers.extend(digits)
        i = 3
        for i in split_numbers:
            return split_numbers.count(3)

    elif base == 5:
        base5_nums = []
        for number in list:
            base5_num = ""
            while number > 0:
                remainder = number % 5
                base5_num = str(remainder) + base5_num
                number = number // 5
            base5_nums.append(base5_num)
        split_numbers = []
        for yas in base5_nums:
            digits = [int(digit) for digit in str(yas)]
            split_numbers.extend(digits)
        i = 4
        for i in split_numbers:
            return split_numbers.count(4)


    elif base == 6:
        base6_nums = []
        for number in list:
            base6_num = ""
            while number > 0:
                remainder = number % 6
                base6_num = str(remainder) + base6_num
                number = number // 6
            base6_nums.append(base6_num)
        split_numbers = []
        for yas in base6_nums:
            digits = [int(digit) for digit in str(yas)]
            split_numbers.extend(digits)
        i = 5
        for i in split_numbers:
            return split_numbers.count(5)

    elif base == 7:
        base7_nums = []
        for number in list:
            base7_num = ""
            while number > 0:
                remainder = number % 7
                base7_num = str(remainder) + base7_num
                number = number // 7
            base7_nums.append(base7_num)
        split_numbers = []
        for yas in base7_nums:
            digits = [int(digit) for digit in str(yas)]
            split_numbers.extend(digits)
        i = 6
        for i in split_numbers:
            return split_numbers.count(6)

    elif base == 8:
        base8_nums = []
        for number in list:
            base8_num = ""
            while number > 0:
                remainder = number % 8
                base8_num = str(remainder) + base8_num
                number = number // 8
            base8_nums.append(base8_num)

        split_numbers = []
        for yas in base8_nums:
            digits = [int(digit) for digit in str(yas)]
            split_numbers.extend(digits)
        i = 7
        for i in split_numbers:
            return split_numbers.count(7)

    elif base == 9:
        base9_nums = []
        for number in list:
            base9_num = ""
            while number > 0:
                remainder = number % 9
                base9_num = str(remainder) + base9_num
                number = number // 9
            base9_nums.append(base9_num)
        split_numbers = []
        for yas in base9_nums:
            digits = [int(digit) for digit in str(yas)]
            split_numbers.extend(digits)
        i = 8
        for i in split_numbers:
            return split_numbers.count(8)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num = int(input().strip())

    base = int(input().strip())

    start = int(input().strip())

    result = countLargestDigit(num, base, start)

    fptr.write(str(result) + '\n')

    fptr.close()
