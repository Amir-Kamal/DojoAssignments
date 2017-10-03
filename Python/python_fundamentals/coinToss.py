from random import *

def coinToss():
    print("Starting the program...")
    hCount = 0
    tCount = 0
    for i in range(1, 51):
        flip = round(random())
        if flip == 1:
            flip = "Heads"
            hCount += 1
        else:
            flip = "Tails"
            tCount += 1
    
    print("Attempt #{}: Throwing a coin.. It's {}! ... Got {} Head(s) so far and {} tail(s) so far".format(i, flip, hCount, tCount))
    return hCount
