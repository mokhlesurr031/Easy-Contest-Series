num = int(input())


for i in range(num):
    a, b, c, n = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)

    if((a+b+c+n)%3==0):
        print("YES\n")
    else: 
        print("NO\n")