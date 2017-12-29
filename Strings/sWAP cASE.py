# sWAP cASE

##def swap_case(s):
##    return str.swapcase(s)
##    #or
def swap_case(s):
        lst=[]
        for i in range(len(s)):
                if s[i].isupper():
                        lst.append(s[i].lower())
                else:
                        lst.append(s[i].upper())
        print(lst)
        p="".join(lst)
        return p    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
