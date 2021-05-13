x, y = map(int, input().split())


def gcd(a, b):
    if (a>b):
        while(b!=0):
            rem = a%b 
            a = b 
            b = rem 
        return a

    else:
        while(a!=0):
            rem = b%a 
            b = a 
            a = rem 
        return b 


def lcm(a, b):
    val = gcd(a, b)
    result = (a*b)//val 
    return result

    

g = gcd(x, y)
l = lcm(x, y)
print(f"GCD = {g}")
print(f"LCM = {l}")


