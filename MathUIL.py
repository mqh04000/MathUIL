import math

def pointToPlane(x, y, z, a, b, c, d):
    numerator = abs(a*x + b*y + c*z - d)
    denominator = (a**2 + b**2 + c**2)**0.5
    result = numerator / denominator
    return round(result, 5)


def calcAreaPerim(coords):
    n = len(coords)
    area = 0
    perimeter = 0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]  
        area += x1 * y2 - x2 * y1
        perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    area = abs(area) / 2
    return area, perimeter

def line_equation(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    if x2 == x1:
        return None, None, 1, 0, -x1
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    A = -m
    B = 1
    C = b
    return m, b, A, B, C


def perpendicular_bisector(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    if x2 - x1 == 0:
        A, B, C = 1, 0, -mid_x
        return A, B, C, None, mid_x
    if y2 - y1 == 0:
        A, B, C = 0, 1, -mid_y
        return A, B, C, 0, mid_y
    m = (y2 - y1) / (x2 - x1)
    perp_m = -1 / m
    b = mid_y - perp_m * mid_x
    A = perp_m
    B = -1
    C = b
    return A, B, C, perp_m, b


def calculate_angle(A, B, C):
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    
    dot_product = AB[0] * BC[0] + AB[1] * BC[1]
    magnitude_AB = math.sqrt(AB[0] ** 2 + AB[1] ** 2)
    magnitude_BC = math.sqrt(BC[0] ** 2 + BC[1] ** 2)
    
    angle_radians = math.acos(dot_product / (magnitude_AB * magnitude_BC))
    angle_degrees = math.degrees(angle_radians)
    
    return 180 - angle_degrees

def distance_from_point_to_line(x0, y0, m, b):
    A = -m
    B = 1
    C = -b
    distance = abs(A * x0 + B * y0 + C) / math.sqrt(A**2 + B**2)
    
    return distance

def distance_from_point_to_line_general(x0, y0, a, b, c):
    distance = abs(a * x0 + b * y0 - c) / math.sqrt(a**2 + b**2)
    return distance

while True:
    print("Enter nothing to exit the program")
    print("1 - Algebra")
    print("2 - Geometry (Coordinate Plane / Shapes)")
    choice = input()
    if choice == "":
        exit()
    elif choice == "1":
        #wtv u wana add
        x = 0
    elif choice == "2":
        print("1 - Area and Perimeter (coordinate)")
        print("2 - Equation and ⟂Bisector of 2 points")
        print("3 - Angle of 3 points")
        print("4 - Heron's formula (area from 3 sides)")
        print("5 - Distance from point and line (2D)")
        print("6 - Distance from point and plane (3D)")
        choice = input()
        if choice == "1":
            print("Enter coordinates in x (enter) y (enter) or nothing to stop")
            coordinates = []
            while True:
                x_input = input("x: ")
                if x_input == "":
                    break
                y_input = input("y: ")
                if y_input == "":
                    break            
                x = float(x_input)
                y = float(y_input)
                coordinates.append((x, y))
            area, perimeter = calcAreaPerim(coordinates)
            print(f"Area of the polygon: {area:.3f}")
            print(f"Perimeter of the polygon: {perimeter:.3f}")
        elif choice == "2":
            print("Enter vertex point second")
            points = []
            while len(points) < 2:
                x = float(input("Enter x coordinate: "))
                y = float(input("Enter y coordinate: "))
                points.append((x, y))
            m, b, A, B, C = line_equation(points[0], points[1])    
            if m is not None:
                print(f"Equation of the line:")
                print(f"1. {A:.4f}x + {B:.4f}y = {C:.4f}")
                print(f"2. y = {m:.4f}x + {b:.4f}")
                A_bisector, B_bisector, C_bisector, slope_bisector, b_bisector = perpendicular_bisector(points[0], points[1])
                print("Perpendicular Bisector: ")
                print(f"1. {A_bisector:.4f}x + {B_bisector:.4f}y = {C_bisector:.4f}")
                if slope_bisector is not None:
                    print(f"2. y = {slope_bisector:.4f}x + {b_bisector:.4f}")
                else:
                    print(f"2. x = {b_bisector:.4f}")
            else:
                print("Perpendicular Bisector: x = " + str(points[0][0]))
        elif choice == "3":
            points = []    
            for i in range(3):
                x = float(input(f"Enter x coordinate for point {i + 1}: "))
                y = float(input(f"Enter y coordinate for point {i + 1}: "))
                points.append((x, y))    
            A, B, C = points
            angle = calculate_angle(A, B, C)    
            print(f"The angle is {angle:.3f} degrees")
        elif choice == "4":
            print("Enter side lengths ")
            a = float(input())
            b = float(input())
            c = float(input())
            s = (a+b+c)/2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"The area of the triangle is: {area:.3f} square units")
        elif choice == "5":
            print("1: y = mx + b")
            print("2: ax + by = c")
            choice = input()
            if choice == "1":
                x = float(input("x: "))
                y = float(input("y: "))
                m = float(input("m: "))
                b = float(input("b: "))
                distance = distance_from_point_to_line(x, y, m, b)
                print(f"Distance: {distance:.3f}")
            elif choice == "2":
                x = float(input("x: "))
                y = float(input("y: "))
                a = float(input("a: "))
                b = float(input("b: "))
                c = float(input("c: "))
                print("Distance: " + str(distance_from_point_to_line_general(x, y, a, b, c)))
        elif choice == "6":
            print("x,y,z ax+by+cz = d")
            x = float(input())
            y = float(input())
            z = float(input())
            a = float(input())
            b = float(input())
            c = float(input())
            d = float(input())
            print("Distance: " + str(pointToPlane(x,y,z,a,b,c,d)))



                        
            
