#!/usr/bin/env python3
for num in range(1,101):
    a,b = divmod(num,10)
    if (a==7) or (b==7):
        continue
    elif num % 7 == 0:
        continue
    else:
        print(num)
