# 34. A wooded area is in the shape of a a trapezoid whose bases measure 128 m 
# and 92 m and its height is 40 m. A 4 m wide walkway is constructed which runs 
# perpendicular to the two bases. Calculate the area of the wooded area after the
#  addition of the walkway.

a = 128
b = 92
h = 40
area_trapeziod = 0.5 * (a + b) * h
area_pathway = 40*4
Area = area_trapeziod-area_pathway
print("Area",Area)