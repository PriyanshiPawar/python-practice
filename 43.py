#43. Find the cost of polishing the base of a cone whose height is 4cm and slant
#  height 5 cm at the rate of 10 rs. Per sq. cm
h = 4
l = 5
 # csa = 3.14 * r * l 
 # l^2 = r^2 + h^2
r1= l*l - (h*h) 
r= r1**0.5
csa = 3.14 * r * l
print("Cost : Rs",10*csa)