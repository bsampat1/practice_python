#!/usr/bin/python

div_seven_not_five = []

for i in xrange(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        div_seven_not_five.append(i)

print div_seven_not_five
