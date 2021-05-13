test = int(input())

for i in range(1, test+1):
    my_floor, lift_floor = input().split()

    my_floor = int(my_floor)
    lift_floor = int(lift_floor)

    if (my_floor<=lift_floor):
        time = lift_floor*4+19
        print(f"Case {i}: {time}")

    if (my_floor > lift_floor):
        extra = my_floor-lift_floor
        time = (my_floor+extra)*4+19

        print(f"Case {i}: {time}")