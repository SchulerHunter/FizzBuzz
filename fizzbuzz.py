#!/home/hunter/anaconda3/bin/python
import sys

num = int(sys.argv[1])
if (num % 15 == 0): print("FizzBuzz")
elif (num % 3 == 0): print("Fizz")
elif (num % 5 == 0): print("Buzz")
else: print(num)