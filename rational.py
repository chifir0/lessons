import math

class Rational:
    pass

def check(numer, denom):
    nod = math.gcd(numer, denom) 
    if nod != 0:
        new_numer = numer // nod
        new_denom = denom // nod
        if new_denom < 0:
            new_numer = -new_numer
            new_denom = -new_denom
    return [new_numer, new_denom]

def create(numer, denom):
    if denom == 0:
         print('Cannot divide by zero')
         return
    return check(numer, denom)

def add(a, b):
    new_numer = a[0] * b[1] + b[0] * a[1]
    new_denom = a[1] * b[1]
    return check(new_numer, new_denom)

def sub(a, b):
    new_numer = a[0] * b[1] - b[0] * a[1]
    new_denom = a[1] * b[1]
    return check(new_numer, new_denom)

def mul(a, b):
    new_numer = a[0] * b[0]
    new_denom = a[1] * b[1]
    return check(new_numer, new_denom)

def div(a, b):
    if b[0] == 0:
        return 'Cannot divide by zero'
    new_numer = a[0] * b[1]
    new_denom = a[1] * b[0]
    return check(new_numer, new_denom)

def power(r, power):
    if power >= 0:
        new_numer = r[0] ** power
        new_denom = r[1] ** power
    else:
        new_numer = r[1] ** (-power)
        new_denom = r[0] ** (-power)
    return check(new_numer, new_denom)

def compare(a, b):
    left = a[0] * b[1]
    right = b[0] * a[1]
    if left < right:
        return -1
    elif left == right:
        return 0
    else:
        return 1

def to_int(r):
    return r[0] // r[1]

def to_float(r):
    return r[0] / r[1]

def to_str(r):
    return f"{r[0]}/{r[1]}"