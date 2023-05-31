for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                f = x and (y <= z) and ((not y) <= ((not z) == w))

                if f == 0:
                    continue

                print(x,y,z,w,int(f), sep=" ")



# XZYW








# from itertools import *
#
#
# def f(x, y, z, w):
#     return x and (y <= z) and ((not y) <= ((not z) == w))
#
#
# for a in product([0, 1], repeat=5):
#     table = {
#         (a[0], a[1], 0, 0),
#         (a[2], 0, 0, a[3]),
#         (1, a[4], 1, 1),
#     }
#
#     for p in permutations("xyzw"):
#         if [f(**dict(zip(p, t))) for t in table] == [1, 0, 0]:
#             print("".join(p))
