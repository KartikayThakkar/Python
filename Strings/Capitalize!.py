def capitalize(string):
        lst=string.split(" ")
        for i in range(len(lst)):
                lst[i]=lst[i].capitalize()
        str=" ".join(lst)
        return str

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
