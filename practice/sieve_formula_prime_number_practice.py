from math import sqrt
test = int(input("Test Case: "))

def prime_generator(num):
    num_list  = [True]* (num+1)
    num_list[0] = False
    num_list[1] = False
    # print(num_list)

    sq_num = int(sqrt(num))+1
    print(sq_num)

    for each in range(2, sq_num):
        if num_list[each] == True:
            for i in range(each*each, num+1, each):
                num_list[i] = False

    
    for prime in range(0, len(num_list)):
        if (num_list[prime]==True):
            print(prime, end = ' ')




while test:
    num = int(input())
    if (num==0 or num==1):
        print(" ")
        continue;
    prime_generator(num)
    print("\n")

    test-=1 