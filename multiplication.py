#!/usr/bin/env python3
i = 1
print("-" * 50)
while i < 10:
    n = 1
    while n < 10:
        print("{:2d}*{:2d}={:3d}".format(i, n, i*n), end = ' ')
        n += 1
    print()
    i += 1
print("-" * 50)

