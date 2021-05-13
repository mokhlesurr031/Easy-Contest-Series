# x 

# x/2 + x/2 + x = 


# 100/50 = .5 

# 100/100 = 1 

# .5x + .5x + 1 x = 2x 

# 3x total 
# 2x/3x ans 


n = int(input())

val = list(map(int, input().split()))
frac = 0

val_len = len(val)

for i in val:
    frac+= i/100



# print(frac)

result = (frac/val_len)*100

print("%.12f" %result)

# print((frac/val_len)*100)