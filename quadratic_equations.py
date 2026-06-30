a = int(input("enter 'a' value:"))
b = int(input("enter 'b' value:"))
c = int(input("enter 'c' value:"))

d = b**2 - 4*a*c

root1 = -b+d**(0.5)/2*a
root2 = -b-d**(0.5)/2*a

print(f"root1:{root1}")
print(f"root2:{root2}")
