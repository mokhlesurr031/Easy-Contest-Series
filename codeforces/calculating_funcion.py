num = int(input())

if (num%2==0):
    even = int(num/2)
    odd = int(num/2)

    # print(even, odd)

    even_total = even*(even+1)
    odd_total = odd**2

    print(even_total-odd_total)


elif(num%2!=0):
    even = int(num/2)
    odd = int((num+1)/2)

    # print(even, odd)

    even_total = even*(even+1)
    odd_total = odd**2

    print(even_total-odd_total)