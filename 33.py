# 33. A rectangular garden has dimensions of 30 m by 20 m and is divided in to 
# 4 parts by two pathways that run perpendicular from its sides. One pathway
#  has a width of 3 m and the other, 4 m. Calculate the total usable area of the garden.

total = 30 * 20
path1 = 30 * 3
path2 = 20 * 4
area = total - (path1 + path2)
print(area)