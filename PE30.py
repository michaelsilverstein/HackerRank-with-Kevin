#Project Euler #30
#https://projecteuler.net/problem=30

Brute Force:

#Problem 30

from time import *

start = clock()

def sum_fifth(num):
    #Sums each digit to the fifth power of a number
    return int(sum([int(x)**5 for x in str(num)]))

def check(num):
    if num == sum_fifth(num):
        return True
def find_constraint():
    ##Find constraint
    nines = ''
    n9 = range(1,101)
    sums = []
    for x in range(100):
        nines += '9'
        n = int(nines)
        s = sum_fifth(n)
        sums.append(s)
        print nines,s,len(nines),len(str(s))
def main():
    s = 0
    for x in range(2,int(10e5)):
        if check(x):
            s += x
            print x
    print 'Total:',s
main()

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
Time required: 4.798988 seconds
