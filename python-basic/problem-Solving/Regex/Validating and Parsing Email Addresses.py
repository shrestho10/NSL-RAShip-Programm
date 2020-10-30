import email.utils
import re

n=int(input())
for i in range(0,n):
    a=input()
    c=email.utils.parseaddr(a)
    d=email.utils.formataddr(c)


    p=re.search('^[a-zA-Z].*@[a-zA-Z]+\.[a-zA-Z]{1,3}$',c[1])

    if p:
        print(a)

