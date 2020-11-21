import numpy

a=input().strip().split(' ')
p=[]
for i in a:
    p.append(int(i))
a=numpy.array(p)
print(numpy.reshape(a,(3,3)))

