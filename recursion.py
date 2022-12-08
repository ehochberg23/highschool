def get_product_of_2_whole_numbers(a, b):
    '''
    Get the product of two whole numbers
    Arguments:
        a: the first number
        b: the second number
    Returns:
        The product of a and b
    '''

    if a < b:  # if a is less than b switch the numbers
        return get_product_of_2_whole_numbers(b, a)


    elif b != 0:  # calculate b, times sum of a
        return (a + get_product_of_2_whole_numbers(a, b - 1))

    else:  # if a number is 0 return 0
        return 0


def get_sum_of_numbers_digits(n):
    """
    Add together a number's digits
    Arguments:
        n: the number
    Returns:
        sum: the sum of the number's digits
    """
    sum = 0
    for digit in str(n):  # for each digit of the number
        sum += int(digit)  # add together the digits
    return sum


def get_factorial(n):
    """
    Get the factorial of a number
    Arguments:
        n: the number
    Returns:
        The factorial of the number
    """

    if n == 0:
        return 1  # the factorial of 0 is 1
    else:
        return n * get_factorial(n - 1)  # find the factorial, ex: 5! = 5*4*3*2*1


def main():
    print("Hello World")


if __name__ == '__main__':
    main()

