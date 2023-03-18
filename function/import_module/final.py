import sys
from module1 import hello
print(sys.argv)
if len(sys.argv)==2:
    hello(sys.argv[1])