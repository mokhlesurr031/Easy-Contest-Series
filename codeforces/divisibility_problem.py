test = int(input())

for i in range(test):
    a, b = map(int, input().split())
    flag = 0

    if (a%b==0):
        print(0)
    else:
        # div = a//b 
        rem = a%b 
        print(b-rem)
        # print()

        

    # print(flag)


