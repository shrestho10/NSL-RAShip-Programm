import re
n =int(input())
for i in range(0,n):
    num=input()
    pat=r"^[7,8,9][0-9]+"
    a=re.findall(pat,num)
    if len(a)==0:
        print("NO")
    else:
        if len(a[0])==10:
            print("YES")
        else:
            print("NO")
