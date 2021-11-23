t=int(input())
for i in range(t):
    n=int(input())
    sum=0
    while(n>0):
        t=n%10
        sum=sum*10+t
        n=n//10
    print(sum)