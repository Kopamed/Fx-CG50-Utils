print("LineCalc V1.0 by Konstantin")
print("Enter coords in the following format: 'coord_x coord_y'\n e.g: Enter coord a: 21 42")
print()


ax, ay = (float(i) for i in input("Enter coords for point a: ").split())
bx, by = (float(i) for i in input("Enter coords for point b: ").split())

cx = ax + (bx - ax) * 2
cy = ay + (by - ay) * 2

mx = (ax + bx) / 2
my = (ay + by) / 2

m = (by - ay) / (bx - ax)
c = ay - ax * m
equation = "y = " + str(m) + "x + " + str(c)

perp_m = -1 / m
perp_c = my - mx * perp_m
perp_equation = "y = " + str(perp_m) + "x + " + str(perp_c)

print("Point a coords: (" + str(ax) + ", " + str(ay) + ")")
print("Point b coords: (" + str(bx) + ", " + str(by) + ")")

print("Point c coords: (" + str(cx) + ", " + str(cy) + ")")
print("Midpoint of a and b coords: (" + str(mx) + ", " + str(my) + ")")

print("Gradient of line: " + str(m))
print("Y-intersection of line: " + str(c))
print("Formula for line: " + str(equation))

print("Gradient of perpendicular line: " + str(perp_m))
print("Y-intersection of perpendicular line: " + str(perp_c))
print("Formula for perpendicular line: " + str(perp_equation))
