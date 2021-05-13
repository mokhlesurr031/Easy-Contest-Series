test = int(input())
flag = 0
catch = 0

for i in range(1, test+1):
    num = int(input())

    for j in range(num):
        name = input()
        if(name[0:4]=="wine"):
            flag+=1
            
        else:
            flag+=0
        catch+=1

    # print(flag)


    # print(catch)
    if (flag==0):
        print(f"Case {i}: Yes")
    if (flag>0):
        print(f"Case {i}: No")
    flag = 0