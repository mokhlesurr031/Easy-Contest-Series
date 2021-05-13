x, y = input().split()
direction = input()

x = int(x)
y = int(y)

x_flag = 0
y_flag = 0


for i in direction:
    if (i == 'U'):
        y_flag+=1 
    elif(i== 'D'):
        y_flag-=1 

    elif(i=='R'):
        x_flag+=1

    elif(i=='L'):
        x_flag-=1

print(x+x_flag, y+y_flag)

