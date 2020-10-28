import re
s=input()
a=re.findall('\w[a,e,i,o,u,A,E,I,O,U][a,e,i,o,u,A,E,I,O,U]+\w',s)
for i in a:
    p=re.findall('[a,e,i,o,u,A,E,I,O,U][a,e,i,o,u,A,E,I,O,U]+',i)
    print(p[0])
