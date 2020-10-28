def swap_case(s):
    news=''
    for i in s:
        p=i
        p=p.upper()
        q=i.lower()
        if i==p:
            news+=i.lower()
        elif i==q:
            news+=i.upper()
    return news

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
