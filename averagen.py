#!/usr/bin/env python3
N = 10
sum = 0
for num in range(0,N):
#    print("Please input 10 numbers:")
    number = float(input('Please input 10 numbers:'))
    sum += number
average = sum / N
print("N = {}, Sum = {}".format(N,sum))
print("Average = {:.2f}".format(average))

