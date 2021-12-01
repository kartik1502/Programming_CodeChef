n=int(input())
p1=0
p2=0
l=0
for i in range(n):
    n,m=map(int,input().split())
    p1+=n
    p2+=m
    if(l<abs(p1-p2)):
        l=abs(p1-p2)
        if(p1-p2>0):
            w=1
        else:
            w=2
print(w,l)