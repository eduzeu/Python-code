def reverse(n):
    if n == '':
        return ''
    else:
        return  reverse(n[1:]) + n[0] 

def subset(n, l):
    if n == 0:
        return 0
    if l == []:
        return 0
    if l[0] > n:
        return subset(n, l[1:])
    if l[0] == n:
        return n
    if l[0] < n:
        useit = l[0] + subset(n-l[0], l[1:])
        loseit = subset(n, l[1:])
        return max(useit,loseit)
    
#Write a Python program to calculate the sum of a list of numbers

def sumOfNumbers(n):
    if n == []:
        return 0
    else:
        return n[0] + sumOfNumbers(n[1:])

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) 

def sumOfIntegers(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumOfIntegers(int(n/10))


def power(a,b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * power(a,b-1) 
        



'''def count(num, L):
     if L == []:
        return 0
     elif L[0] == num :
        return 1 + count(num, L[1:])   
     else:
        return 0 + count(num, L[1:])  '''


 
def countSymbol(symbol, string):
    if string == '':
        return 0
    elif string[0] == symbol:
        return 1 + countSymbol(symbol, string[1:])
    else:
        return 0 + countSymbol(symbol, string[1:])


def countPattern(shortString, longString):
    if longString == '':
        return 0
    elif shortString[0:2] == longString: 
        return 1 + countPattern(shortString, longString[1:])
    else:
        return 0 + countPattern(shortString, longString[1:])
    

def zipp(list1,list2):
    if list1 == []:
        return []
    elif list2 == []:
        return []
    else:
        return list1[0:] + zipp(list1, list2[0:])

def reverseString(s):
    if s == '':
        return ''
    else:
        return reverseString(s[1:]) + s[0]



def lengthList(myList):
    if myList == []:
        return 0
    else:
        return 1 + lengthList(myList[1:])

def inverse(n):
    return 1/n


def harmonicSum(n):
    if n == 0:
        return 0
    else:
        return 1/n + harmonicSum(n-1)

def intToString(n):
    if n == 0:
        return ''
    else:
        return str(n)


def fibonacci(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


 



