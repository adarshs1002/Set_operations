x={2,4,6,8,10,12}
y={3,6,9,12,15,18}
print("x=",x)
print("y=",y)
#union of two sets
z1=x.union(y)

print("Union of x and y is ",z1)

#intersection of two sets
z2=x.intersection(y)

print("Intersection of x and y is ", z2)

#difference of two sets
z3=x.difference(y)

print("Difference of x and y is ", z3)

#symmetric difference of two sets
z4=x.symmetric_difference(y)

print("Symmetric difference of x and y is ", z4)