from decimal import *
from time import sleep


def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)


def chudnovskyBig(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += ((Decimal(-1) ** k) * (Decimal(factorial(6 * k)) /
              ((factorial(k) ** 3) * (factorial(3 * k))) *
              (13591409+545140134*k)/(640320**(3*k))))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi ** (-1)
    return pi


getcontext().prec = int(input("Enter number of decimal places: "))
i = 0
lastpi = 0
newpi = 3

while lastpi != newpi:
    lastpi = newpi
    newpi = chudnovskyBig(i)
    i += 1
print(i, newpi)

sleep(10)
