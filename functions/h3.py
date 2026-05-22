# Write a Program to Calculate diameter and area of circle using user defined function
def circle(rad):
    diameter = rad * 2
    area = 3.14 * rad * rad
    print("Area of circle:", area)
    print("Diameter of circle:", diameter)

r=float(input("Enter radius of circle: "))
circle(r)