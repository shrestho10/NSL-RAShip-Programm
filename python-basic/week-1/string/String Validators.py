if __name__ == '__main__':
    s = str(input())
    a=0
    b=0
    c=0
    d=0
    e=0
    for i in s:
        if i.isalnum()==True and a==0:
            a=1
            print('True')
    if a==0:
        print('False')
    for i in s:
        if i.isalpha()==True and b==0:
            b=1
            print('True')

    if b==0:
        print('False')
    for i in s:
        if i.isdigit()==True and c==0:
            c=1
            print('True')
    if c==0:
        print('False')
    for  i in s:
        if i.islower()==True and d==0:
            d=1
            print('True')
    if d==0:
        print('False')

    for i in s:
        if i.isupper()==True and e==0:
            e=1
            print('True')
    
    if e==0:
        print('False')
  
  
        

        
