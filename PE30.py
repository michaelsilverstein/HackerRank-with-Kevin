#Project Euler #30
#https://projecteuler.net/problem=30

Brute Force:

from time import *

start = clock()

def sum_fifth(num):
    #Sums each digit to the fourth power of a number
    return int(sum([int(x)**5 for x in str(num)]))

def check(num):
    if num == sum_fifth(num):
        return True
s = 0
for x in range(2,int(10e6)):
    if check(x):
        s += x
        print x
print 'Total:',s

print 'Time required: %f seconds'%(clock()-start)
--------------------------------------------------
Output:
4150
4151
54748
92727
93084
194979
Total: 443839
Time required: 56.114640 seconds
