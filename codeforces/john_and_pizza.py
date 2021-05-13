a, b = input().split()

a = int(a)
b = int(b)

if (a>=b):
    inter = 2*a-1
    print(inter*b)

elif(a<b):
    inter = 2*b-1
    print(inter*a)