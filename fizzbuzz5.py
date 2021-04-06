#!/home/hunter/anaconda3/bin/python
import os
import sys
import fizzbuzz4 as fb

total = int(sys.argv[1])
f = open("fizzbuzz4.c", "w")
n = 1
f.write("#include <stdio.h>\n#include <stdlib.h>\n#include <stdint.h>\n\nvoid main(int argc, char *argv[]) {\n\tuint64_t n = atoi(argv[1]);\n")
while n < total+1:
    tabs = "\t"*(n+1)
    s = ""
    s = s+tabs
    s = s+("if (n > %d) {\n" % n)
    f.write(s)
    n += 1
n -= 1
f.write(tabs+"\tprintf(\"Out of Bounds\\n\");\n")

while n > 0:
    tabs = "\t"*(n)
    s = ""
    s = s+("%s} else {\n%s\tprintf(\"%s\\n\");\n%s}\n" % (tabs, tabs, fb.fizzbuzz(n), tabs))
    f.write(s)
    n -= 1
f.write("}")
f.close()

os.system("gcc fizzbuzz4.c -o fizzbuzz4")
os.system("./fizzbuzz4 %d" % total)