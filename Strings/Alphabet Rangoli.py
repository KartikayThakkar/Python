"""
Alphabet Rangoli

You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

Input Format

Only one line of input containing , the size of the rangoli.

Constraints


Output Format

Print the alphabet rangoli in the format explained above.

Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------"""
def print_rangoli(size):
        s="abcdefghijklmnopqrstuvwxyz"
        p=size
        t=1
        l=size
        a=1
        u=1
        y=(2*size)-3
        for i in range(size-1):
                for o in range((2*p)-2):
                        print("-",end="")
                
                
                for  j in range(t):
                        print(s[size-j-1],end="")
                        print("-",end="")
                        
                t=t+1
                
                if i>0:
                        for  j in reversed(range(a-1)):
                                print(s[size-j-1],end="")
                                if i!= size:
                                        print("-",end="")
                                
                                
                for o in range(y):
                        print("-",end="")
                y=y-2
                l=l-1
                p=p-1
                a=a+1
                print()        
        if size>1:
                d=size-1
        
                for i in range(size):
                        print(s[d],end="")
                        print("-",end="")
                        d=d-1
                d=d+1        
                
                for i in range(size-2):
                        d=d+1
                        print(s[d],end="")
                        print("-",end="")
                
                
                print(s[d+1])
        else:
                print("a")
        p=2
        t=size-1
        a=1
        r=4
        for i in range(size-1):
                for o in range(p):
                        print("-",end="")
                p=p+2
                
                
                for j in range(t):
                        print(s[size-j-1],end="")
                        print("-",end="")
                r=size-j        
                for j in range(t-1):
                        print(s[r],end="")
                        print("-",end="")
                        r=r+1
                
                
                t=t-1
                
                for o in range(u):
                        print("-",end="")
                u=u+2
                print()
 if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
