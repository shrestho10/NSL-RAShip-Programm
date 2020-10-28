if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(0,N):
        
        a=input()
        a=a.split(" ")

        if a[0]=="insert":
            

            L.insert(int(a[1]),int(a[2]))
        elif a[0]=="remove":
             L.remove(int(a[1]))
        elif a[0]=="append":
            L.append(int(a[1]))
        elif a[0]=="sort":
            L.sort()
        elif a[0]=="pop":
            L.pop()
        elif a[0]=="reverse":
            L.reverse()
        elif a[0]=="print":
            print(L)
