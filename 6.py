# Question 6: triangle sides 10, 9, perimeter 36. Find 
# area.
a = 10
b = 9
p = 36
#p=sum of all three sides
c = p-(a+b)
c = p - (a + b)

s = p / 2

value = s * (s - a) * (s - b) * (s - c)

area = value ** 0.5

print(area)


