"""
Designer Door Mat

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints



Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
Note: 
More than  lines of code will result in a score of . Comment lines are counted. Blank lines are not counted."""
N, M = map(int,input().split())
K=int((N-1)/2)
P=int((M-3)/2)
O=P
t=1

for i in range(K): 
        for i in range(P,0,-1): 
                print("-",end="")
        P=P-3
        
        for l in range(t):
                print(".|.",end="")
        t=t+2
        
        for i in range(0,O,1): 
                print("-",end="")
        O=O-3
        print()
for i in range(N):
        print("-",end="")
print("WELCOME",end="")
for i in range(N):
        print("-",end="")

P=P+3
O=O+3
t=t-2

for i in range(K): 
        print()
        for i in range(P,0,-1): 
                print("-",end="")
        P=P+3
        
        for l in range(t):
                print(".|.",end="")
        t=t-2
        
        for i in range(0,O,1): 
                print("-",end="")
        O=O+3

"""
Note: 
More than  lines of code will result in a score of . Comment lines are counted.
"""

N, M = map(int,input().split())
for i in range(1,N,2): 
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, "-"))

