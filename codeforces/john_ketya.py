num = int(input())
john = 0
ketya = 0


def fact(n):
    flag = 1
    for i in range(1, n+1):
        flag = flag*i

    return flag
    
# x = fact(5)
# print(x)

for j in range(1, num+1):
    x = fact(j)
    # print(x)
    if (x%2!=0):
        john +=1

# for k in range(2, num+1, 2):
#     y = fact(k)

#     if (y%2!=0):
#         john+=1

# print(john)

num = num-john

if (john>num):
    print("Win")
elif(john==num):
    print("Draw")
elif (john<num):
    print("Lose")



