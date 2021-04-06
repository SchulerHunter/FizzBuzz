#!/home/hunter/anaconda3/bin/python
import sys

num = int(sys.argv[1])
ret = ""
if (num % 3 == 0):
    ret += "Fizz"
if (num % 5 == 0):
    ret += "Buzz"
if (ret == ""):
    ret = str(num)
print(ret)