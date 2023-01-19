import math
import cmath

a=int(input("Please enter first number:"))
b=int(input("Please enter second number:"))

def checkDivisibility(n, digit):
    return (digit != 0 and n % digit == 0)
def allDigitsDivide(n):
    nlist = map(int, set(str(n)))
    for digit in nlist:
        if not (checkDivisibility(n, digit)):
            return False
    return True

array = []
for i in range(a,b+1):
    if checkDivisibility(i):
        array.append(i)
print(array)
