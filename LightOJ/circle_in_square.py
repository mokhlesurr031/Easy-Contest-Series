import math
test = int(input())

half_pi = math.acos(0.0)
pi = half_pi*2


for i in range(1, test+1):
    radius = float(input())
    sq_area = (2*radius)**2
    circle_area = pi* (radius)**2

    print(f"Case {i}: %.2f" %(sq_area-circle_area))
