test = int(input())


for i in range(1, test+1):
    a, b = input().split()
    a = int(a)
    b = int(b)

    if(a%b == 0 or b%a==0):
        print(f"Case {i}: divisible")
    else:
        print(f"Case {i}: not divisible")