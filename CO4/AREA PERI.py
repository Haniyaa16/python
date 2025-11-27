class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


def get_rectangle(n):
    l = float(input(f"Enter length of Rectangle {n}: "))
    b = float(input(f"Enter breadth of Rectangle {n}: "))
    return Rectangle(l, b)


r1 = get_rectangle(1)
r2 = get_rectangle(2)

print("\nRectangle 1: Area =", r1.area(), ", Perimeter =", r1.perimeter())
print("Rectangle 2: Area =", r2.area(), ", Perimeter =", r2.perimeter())

print()
if r1.area() > r2.area():
    print("Rectangle 1 is larger")
elif r1.area() < r2.area():
    print("Rectangle 2 is larger")
else:
    print("Both rectangles have the same area")

