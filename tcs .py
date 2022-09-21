int1='abcD'
if len(int1)>0:
    for i in int1:
        if i.islower():
            print(i.upper(),end='')
        if i.isupper():
            print(i.lower(),end='')
        else:
            pass
