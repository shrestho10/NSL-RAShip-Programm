import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a=numpy.array(arr)
    p=[]
    for i in range(1,len(a)+1):
        p.append(float(a[-i]))
    
    return numpy.array(p)
arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
