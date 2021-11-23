t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    x=max(a,max(b,c))
    y=min(a,min(b,c))
    if(a!=x and a!=y):
        print(a)
    elif(b!=x and b!=y):
        print(b)
    else:
        print(c)