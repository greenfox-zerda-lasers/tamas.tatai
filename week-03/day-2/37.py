numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def filter(list):
    newlist = []
    for x in list:
        if x % 2 == 0:
            newlist.append(x)
    return newlist

print filter(numbers)
