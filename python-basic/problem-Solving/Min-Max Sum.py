
def miniMaxSum(arr):
    
    l=[]
    s=arr
    for i in s:
        
        p=s.copy()
        p.remove(i)
        #print(p)
        a=sum(p)
        l.append(a)
        #print(arr)
    #print(l)
    print(str(min(l))+' '+str(max(l)))



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
