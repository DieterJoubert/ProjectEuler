"""Problem 1: Sum Multiples of 3 and 5"""
def sumThreeFive(n):
    list = []
    curr = 3
    while curr < n:
        if curr % 3 == 0 or curr % 5 == 0:
            list.append(curr)
        curr += 1
    sum = 0
    for item in list:
        sum += item
    return sum

def problem1():
    print sumThreeFive(1000)

"""Problem 2: Sum Even Fibonnaci"""
def Fibb(n):
    list = [1,1]
    next = 0
    while next <= n:
        list.append(next)
        next = list[-1] + list[-2]
    return list

def listEvens(l):
    newList = []
    for i in l:
        if i % 2 == 0:
            newList.append(i)
    return newList

def sumList(l):
    sum = 0
    for i in l:
        sum += i
    return sum
        
def Problem2():
    print sumList( listEvens(Fibb(4000000)))

"""Problem 3: Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?"""
def prime_factors(n):
    factors = []
    d = 2
    while n>1:
        while n%d==0:
            factors.append(d)
            n = n/d
        d = d+1
    return factors

def Problem3():
    print max(prime_factors(600851475143))

"""Problem 4: Largest palindrome project
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

