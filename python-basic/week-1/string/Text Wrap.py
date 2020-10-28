import textwrap

def wrap(string, max_width):
    p=0
    s=''
    for i in range(0,len(string)):
        
        p+=1
        s+=string[i]
        if p==max_width:
            s+='\n'
            p=0


    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
