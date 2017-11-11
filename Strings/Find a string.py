Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints

 
Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
Concept

Some string processing examples, such as these, might be useful. 
There are a couple of new concepts: 
In Python, the length of a string is found by the function len(s), where  is the string. 
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])'''

def count_substring(string, sub_string):
        count=0
        ans=False
        for i in range(len(string)):
                if string[i]==sub_string[0]:
                        k=i
                        for j in range(len(sub_string)):
                                if len(string)-k+1<=len(sub_string):
                                        return count
                                if sub_string[j] == string[k+j]:
                                        ans=True
                                else:
                                        ans=False
                                        break
                        if ans==True:
                                count =count+1
                                ans=False
        return count 
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
A range function is used to loop over some length:

range (0, 5)
Here, the range loops over  to .  is excluded.
