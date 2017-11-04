Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
Submissions:54063
Max Score:10
Difficulty: Easy
Rate This Challenge:
More
Current Buffer (saved locally, editable)     
 
Python 2

''' 
l=[]
n=int(input())
           
for i in range(n):
    s=raw_input()
    s=s.split( )
    if list(s[0])==list('insert'):
        position=int(s[1])
        value=int(s[2])
        l.insert(position,value)
    elif list(s[0])==list('remove'):
        value=int(s[1])
        l.remove(value)
    elif list(s[0])==list('pop'):
        l.pop()
    elif list(s[0])==list('reverse'):
        l.reverse()
    elif list(s[0])==list('sort'):
        l.sort()
    elif list(s[0])==list('append'):
        value=int(s[1])
        l.append(value)
    elif list(s[0])==list('print'):
        print(l)
