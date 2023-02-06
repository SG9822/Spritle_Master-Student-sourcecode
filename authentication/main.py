def expr(number, operation=None):
    if operation:
        return operation(number)
    else:
        return number

def zero(operation = None):
    return expr(0, operation)

def one(operation = None):
    return expr(1, operation)

def two(operation = None):
    return expr(2, operation)

def three(operation = None):
    return expr(3, operation)

def four(operation = None):
    return expr(4, operation)

def five(operation = None):
    return expr(5, operation)

def six(operation = None):
    return expr(6, operation)

def seven(operation = None):
    return expr(7, operation)

def eight(operation = None):
    return expr(8, operation)

def nine(operation = None):
    return expr(9, operation)

def plus(a):
    return lambda b: a + b

def minus(a):
    return lambda b: b-a

def times(a):
    return lambda b: a * b

def divided_by(a):
    return lambda b: b // a

print(seven(times(five())))
print(four(plus(nine()))) # must return 13
print(eight(minus(three()))) # must return 5
print(six(divided_by(two()))) # must return 3
print(eight(divided_by(three())))
