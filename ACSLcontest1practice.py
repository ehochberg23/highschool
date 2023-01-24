"""
 Given a positive integer (call it N) and a position in that integer (call it P) transform N.
 To transform N, find the Pth digit of N from the right.
 Replace each of the digits to the left of the Pth digit by the sum of that digit and the Pth digit.
 If the sum is greater than 9, use just the units digits (see the second example below).
 Replace each of the digits to the right of the Pth digit by the absolute value of the difference between it and the Pth digit.
 Do not change the Pth digit.

 Example 1: N=102439, P=3.  Answer is: (1+4)(0+4)(2+4)4(|3-4|)(|9-4|) => 546415
 Example 2: N=4329, P=1. Answer is: (4+9)(3+9)(2+9)9 => (13)(12)(11)9 => 3219

 INPUT: There will be 5 sets of data. Each set contains two positive integers: N and P.
    N will be less than 10^15 , and P will be valid.
    No input will cause an output to have a leading digit of 0.
 OUTPUT:  The transformed value of each input set.
    The printed number may not have any spaces between the digits.
"""

def numTransform(n,p):
    numberList = []
    finalList=[]
    finalStr=("")
    numberList.insert(0, n % 10)
    while n > 10:
        n = int(n / 10)
        numberList.append(n % 10)
    try:
        counter = p
        while 1==1:
            new=int(numberList[counter])+int(numberList[p-1])
            finalList.insert(0, new % 10)
            counter=counter+1
    except:
        finalList.append(numberList[p-1])
        counter = p-2
        while counter>=0:
            new=int(numberList[counter])-int(numberList[p-1])
            finalList.append(abs(new) % 10)
            counter=counter-1
        for iteam in finalList:
            final_str= final_str +str(iteam)
    return final_str




def main():
    data=str(input("numbers\n"))
    data=data.split()
    n = int(data[0])
    p = int(data[1])
    print(numTransform(n,p))


if __name__ == "__main__":
    main()