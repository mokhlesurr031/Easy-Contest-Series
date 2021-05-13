num = int(input())

h_that = "I hate that "
l_that = "I love that "
l_it = "I love it"
h_it = "I hate it"
s = ''

if(num == 1):
    print(h_it)


else:
    for i in range(1, num):
        if (i%2==0):
            s+= l_that
        elif(i%2!=0):
            s+= h_that

if(num>1):
    if (num%2==0):
        print(s+l_it)
    else:
        print(s+h_it)

