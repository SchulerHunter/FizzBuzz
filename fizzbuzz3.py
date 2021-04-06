#!/home/hunter/anaconda3/bin/python
import sys

num = int(sys.argv[1])
backup = num
ret = ""
while (num > 2): num -= 3
if (num == 0): ret += "Fizz"

num = backup
while (num > 4): num -= 5
if (num == 0): ret += "Buzz"

if (ret == ""): print(backup)
else: print(ret)
