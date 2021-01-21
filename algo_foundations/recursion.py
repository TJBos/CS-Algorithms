#some simple recursive functions in python

#countdown

def countdown(x):
    if (x == 0):
        print("done")
        return
    else:
        print(x)
        countdown(x-1)

#countdown(5)

#Power

def power(num, exp):
    if (exp == 0):
        return 1
    else:
        return num * power(num, exp-1)

#print(power(2,3))

#factorial?

def factorial(x):
    if (x==0):
        return 1
    else:
        return x * factorial(x-1)

print(factorial(4))



