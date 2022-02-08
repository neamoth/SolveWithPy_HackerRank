# Problem source: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
'''
import math
import os
import random
import re
import sys
'''
'''
Adding extra in this qustion are:

1. User Input
2. While loop
'''

while True:

    n = int(input("Enter a number: "))
    #Checking the number odd or even

    even = False
    odd = False

    if(n%2) == 0:
        even = True
    else:
        odd = True
        
    # Printing the desire task:

    # task1: if odd print weird

    if(odd):
        print("weird")
        
    # task2: even and range(2,5) print "Not Weird"
    elif ((even) and n in range(2,5)):
        print("Not Weird")
    # task3: even and range(6,20) print "Weird"
    elif((even) and n in range(6,20)):
        print("Weird")
    # task4: even and greater than 20 print "Not Weird"
    elif(even) and (n>=20):
        print("Not Weird")
    # This else for error handling
    else:
        print("Error")
    
    user = input("Continue or exit? (y/n)")
    if(user == "y" or user == "yes"):
        continue
    else:
        break