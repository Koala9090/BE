rows = 9

i = 1
while i <= rows:
    space = rows - i
    while space >0:
        print(" ",end="")
        space -= 1

    asteriske = 0
    while asteriske<(2*i-1):
        print("hm", end="")
        asteriske +=1
    print()
    i+=1


