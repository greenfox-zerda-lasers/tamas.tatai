#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


# Returns the median value of a list given as param
def median(pool):
    pool.sort()
    if len(pool) % 2 == 0:
        return (pool[int((len(pool) / 2) -1)] + pool[int(len(pool) / 2)]) / 2
    else:
        return pool[int((len(pool) - 1) / 2)]

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouéáőúűöüóí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
