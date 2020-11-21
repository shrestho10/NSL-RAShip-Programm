import numpy

a,b=input().strip().split(' ')
a=int(a)
b=int(b)
k=[]
for i in range(0,a):
   
        c=input().strip().split(' ')
        k.append(c)
    

k=numpy.array(k)
s=numpy.transpose(k)
print(s.astype(numpy.int))
print(k.flatten().astype(numpy.int))

