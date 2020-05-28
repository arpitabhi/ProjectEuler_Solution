# -*- coding: utf-8 -*-
"""
Created on Fri May 29 00:04:34 2020

@author: arpit
@ ProjectEuler.net Problems

"""
#Question 1 : Multiples of 3 and 5

def sumof3n5(n):
    l=[]
    for i in range(1,n):
        if i%3==0 or i%5==0:
            l.append(i)
    return sum(l)

#Question 2 : Even Fibonacci numbers
    
def FibonacciEvenSum():
    l=[]
    a,b=1,2
    while True:
        if b>4000000 or a>4000000:
            break
        if a%2==0:
            l.append(a)
        if b%2==0:
            l.append(b)
        #print(a,b)
        a+=b
        b+=a
    #print(l)  
    print(sum(l))
FibonacciEvenSum()
        
        

