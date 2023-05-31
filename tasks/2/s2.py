for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                f = y and (x <= w) and ((not x) <= ((not w) == z))

                if f == 1:
                    continue

                print(x,y,z,w,int(f), sep=" ")

# xzyw