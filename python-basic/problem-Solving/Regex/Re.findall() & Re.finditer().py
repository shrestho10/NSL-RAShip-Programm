import re
s=input()
a=re.findall('[a,e,i,o,u,A,E,I,O,U][a,e,i,o,u,A,E,I,O,U]+[qwrtypsdfghjklzxcvbnm]',s)

if len(a)==0:
    print('-1')
else:
    for i in a:
        p=re.findall('[a,e,i,o,u,A,E,I,O,U][a,e,i,o,u,A,E,I,O,U]+',i)
        print(p[0])
