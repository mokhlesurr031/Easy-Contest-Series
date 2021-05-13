import math 
num = int(input())

def divisor1(n):  #efficient way 
    div = set()
    for i in range(1, int(math.sqrt(num)+1)):
        if (n%i==0):
            div.add(int(i))
            div.add(int(n/i))
    return list(div)

def divisor2(n):
    div = list()

    for i in range(1, n+1):
        if (n%i==0):
            div.append(i)
    return div

result1 = divisor1(num)
print(result1)

result2 = divisor1(num)
print(result2)