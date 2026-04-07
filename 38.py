#38. The cylinder has a volume of 1287. The base has a radius 10. What is the area
#  of the surface of the cylinder?

v = 1287
r = 10
# v = 3.14 r^2 h
h = v / (3.14 * r * r)
# a = 2  3.14  r (r+h)
area = 2 * 3.14 * r * (r + h)
print("Area",area)