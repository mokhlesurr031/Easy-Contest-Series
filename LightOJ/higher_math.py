test = int(input())


for i in range(1, test+1):
    a, b, c = input().split()
    # print(type(a))
    a = int(a)
    b = int(b)
    c = int(c)

    

    max = ((a+b)+ abs(a-b))/2

    maximum = ((max+c)+ abs(max-c))/2


    if (b==maximum):
        if((a**2+c**2)==maximum**2):
            print(f"Case {i}: yes")
        else:
            print(f"Case {i}: no")
    
    if (a==maximum):
        if((b**2+c**2)==maximum**2):
            print(f"Case {i}: yes")
        else:
            print(f"Case {i}: no")

    if (c==maximum):
        if((a**2+b**2)==maximum**2):
            print(f"Case {i}: yes")
        else:
            print(f"Case {i}: no")
    


    # print(maximum)