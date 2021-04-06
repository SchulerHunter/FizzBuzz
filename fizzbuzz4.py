#!/home/hunter/anaconda3/bin/python
import sys

def fizzbuzz(num):
    retVal = ""
    backup = num

    digSum = 0
    num = str(num)
    for dig in num:
        digSum = digSum + int(dig)
    
    while (digSum > 10):
        num = str(digSum)
        digSum = 0
        for dig in num:
            digSum = digSum + int(dig)

    if (digSum == 3 or digSum == 6 or digSum == 9):
        retVal = retVal + "Fizz"

    num = backup
    while (num > 0):
        num = num - 5
    try:
        15 / num
    except ZeroDivisionError:
        retVal = retVal + "Buzz"

    if (len(retVal) < 3):
        retVal = backup
    
    if __name__ == "__main__":
        print(retVal)

    return retVal

if __name__ == "__main__":
    fizzbuzz(int(sys.argv[1]))