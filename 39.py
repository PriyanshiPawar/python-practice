# 39. Find the surface of the cylinder if its diameter is 12 centimeters 
# and its height is 9 centimeters.

d = 12
r = d/2
h = 9
#csa = 2 3.14 rh 
csa = 2*3.14*r*h
#TSA=2 3.14 r(h+r)
tsa = 2 * 3.14 * r * (h+r)
print(f"Curved surface area : {csa}and Total surface area :{tsa}" )