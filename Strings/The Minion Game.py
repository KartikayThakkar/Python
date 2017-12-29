Method 1:

def minion_game(string):
        vowel={'A','E','I','O','U'}
        countv=0
        countu=0
        for i in range(len(string)):
                j=i
                if string[i] in vowel:
                        
                        for j in range(len(string)-i):
                                if string[i] in vowel:
                                        countv=countv+1
                else:
                        
                        for j in range(len(string)-i):
                                if string[i] not in vowel:
                                        countu=countu+1
        if countu>countv:
                print('Stuart',countu)
        elif countu<countv:
                print('Kevin',countv)
        else:
                print('Draw')


Method 2:

def minion_game(string):
        vowel={'A','E','I','O','U'}
        countv=0
        countu=0
        for i in range(len(string)):
                if string[i] in vowel:
                        countv=countv + (len(string)-i)
                else:
                        countu=countu + (len(string)-i)
        if countu>countv:
                print('Stuart',countu)
        elif countu<countv:
                print('Kevin',countv)
        else:
                print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
