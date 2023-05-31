for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:

                f = ((x <= y) <= w) or (z <= (y and w))

                if f:
                    continue

                print(x,y,z,w,int(f), sep=" ")