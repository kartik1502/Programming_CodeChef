def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
def main():
    n=int(input())
    for i in range(n):
        m=int(input())
        print(fact(m))
if __name__=="__main__":
    main()