numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

#numbers.reverse()
#print numbers

def reverse(list):
    newlist = []
    for x in reversed(list):
        #for x in range(len(list)-1, -1, -1)
        newlist.append(x)
    print(newlist)

reverse(numbers)
