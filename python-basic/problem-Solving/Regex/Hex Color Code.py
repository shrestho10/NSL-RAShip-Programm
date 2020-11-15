# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=input()
s=''
for i in range(0,int(n)):
    a=input()
    j=re.findall(r'(?<!^)(#[\da-f|A-F]{3,6})',a)
    if len(j)>1:
        for k in j:
            print(k)
    elif len(j)==1:
            print(j[0])
    
            
#here (?<!^) refers to not in first of each line    
    

