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

"""Problem 4: Largest palindrome project"""
def checkPalindrome(n):
  return str(n) == (str(n))[::-1]

def maxPal():
  a = 999
  num = 0
  while a > 99:
    b = 999    
    while b >= a:
      prod = a * b
      if prod > num and checkPalindrome(prod): 
        num = prod
      b = b-1
    a = a-1
  return num

def Problem4():
  print maxPal()


"""Problem 5: Smallest Multiple"""

"""first attempt"""
def nec(x,l):
  for item in l:
    if item % x == 0:
      return False
  return True

def twentyList():
  list = range(1,20)
  newList = [20]
  for i in reversed(list):
    if nec(i,newList):
      newList.append(i)
  return newList

"""solved using prime factors"""
def primeFactors(n):
  dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 0}
  primes = [2,3,5,7,11,13,17,19]
  num = n
  check = True
  while(check):
    for i in primes:
      if num % i == 0:
        num = num / i
        dict[i] += 1
        if num==1:
          check = False
  return dict

def necFactors():
  dict = primeFactors(20)
  for n in range(2,20):
    dict2 = primeFactors(n)
    for key, value in dict2.iteritems():
      if dict[key] < value:
        dict[key] = value
  return dict

def Problem5():
  n = 1
  dict = necFactors()
  for key, value in dict.iteritems():
    if value != 0:
      n = n * (key ** value)
  print n

"""Problem 6: Sum Square Difference"""
def squareSum():
  n = 0
  for i in range(1,101):
    n += i
  return (n**2)

def sumSquares():
  n = 0
  for i in range(1,101):
    n += (i**2)
  return n

def Problem6():
  print squareSum() - sumSquares()

"""Problem 7: 10001st Prime"""
def isPrime(n):
  if n % 2 == 0: return False
  check = 3
  while check < n**0.5 + 1:
    if n % check == 0: 
      return False
    check += 2
  return True

def nthPrime(n):
  prime = 2
  count = 1
  iteration = 3
  while count < n:
    if isPrime(iteration):
      prime = iteration
      count += 1
    iteration += 2
  return prime

def Problem7():
  print nthPrime(10001)

#TODO: Implement problem 7 using Sieve















































