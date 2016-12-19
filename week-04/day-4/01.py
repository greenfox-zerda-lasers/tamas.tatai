# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def countdown(n):
    if n > 0:
        print n
        return countdown(n-1)
    else:
        return 0

countdown(10)
