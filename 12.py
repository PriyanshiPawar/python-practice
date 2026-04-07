#12. Find the area of a right angled triangle whose hypotenuse is 13 cm and one of its 
# sides containing the right angle is 12 cm. Find the length of the other side.

h = 13
a = 12
#a^2 + b^2 = h^2
b = (h*h - a*a) ** 0.5
print("Other side =", b)
area = (a * b) / 2
print("Area =", area)