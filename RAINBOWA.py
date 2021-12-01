t=int(input())
for i in range(t):
    x=True
    n=int(input())
    a = list(map(int,input().split()))
    for i in range(n//2):
        if(i==0):
            if(a[i]!=1 or a[i]!=a[n-i-1]):
                x=False
        elif((a[i]!=a[n-i-1]) and (a[i]!=a[i-1] or a[i]!=a[i-1]+1)):
            x=False
    if(x):
        print("yes")
    else:
        print("no")