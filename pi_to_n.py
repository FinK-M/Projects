from decimal import *
from time import sleep

getcontext().prec = int(input("Enter number of decimal places: "))


def findPi(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += ((Decimal(1) / (16 ** k)) * ((Decimal(4) / (8 * k + 1))
               - (Decimal(2) / (8 * k + 4)) - (Decimal(1) / (8 * k + 5))
               - (Decimal(1) / (8 * k + 6))))
        k += 1
    return pi

i = 0
lastpi = 0
newpi = 3

while lastpi != newpi:
    lastpi = newpi
    newpi = findPi(i)
    i += 1

print(lastpi)
print(newpi)
sleep(10)
