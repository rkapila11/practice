import math


print('Hello World!')
x = 5

for x in range(1, 6):
    print(x)

def pythagorean(a, b):
    c = math.sqrt(a**2 + b**2)
    return c


side_a = 12
side_b = 25

hypo = pythagorean(side_a, side_b)
print(f"the hypotenuse of your triangle is {hypo}")