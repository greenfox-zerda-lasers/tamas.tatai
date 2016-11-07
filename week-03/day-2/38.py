numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)

def find_min(list):
    min = list[0]
    for x in list:
        if x < min:
            min = x
    return min

print(find_min(numbers))
