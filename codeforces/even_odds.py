num, k = input().split()

num = int(num)
k = int(k)

if (num%2==0):
    odd = int(num/2)
    even = int(num/2)

    # print(f"odd {even+odd}")

    if (k<=odd):
        print(2*k-1)
    if (k>odd):
        print(2*(k-odd))

if (num%2!=0):
    odd = int((num+1)/2)
    even = int(num/2)

    # print(odd, even)

    # print(f"odd {even+odd}")

    if (k<=odd):
        print(2*k-1)
    if (k>odd):
        print(2*(k-odd))