test = int(input())


for i in range(1, test+1):
    num = int(input())
    if(num%2!=0 or num==0):
        print(f"Case {i}: Impossible")
    else:
        div = int(num/2)
        val = 2 
        while(div%2==0):
            div = int(div/2) 
            val = val*2
        print(f"Case {i}: {div} {val}")