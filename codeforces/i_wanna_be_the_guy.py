n = int(input())
flag = 0 


x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.remove(x[0])
y.remove(y[0])
# print(x)
# print(y)

all = x+y 
# print(all)

all_set = set(all)



all_list = list(all_set)
# print(all_list)

n_list = [i for i in range(1, n+1)]
# print(n_list)

# print(len(all_list))
# print(len(n_list))

if (len(all_list)==len(n_list)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")



