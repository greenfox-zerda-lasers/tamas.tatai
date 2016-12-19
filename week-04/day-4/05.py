# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def bunnies(n):

    if n <= 0:
        return 0

    else:
        return bunnies(n-1) + 2

print bunnies(45)
