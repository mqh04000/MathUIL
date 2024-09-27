import math

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

def reduce_coefficients(A, B, C):
    A, B, C = int(A), int(B), int(C)
    gcd = math.gcd(A, B)
    gcd = math.gcd(gcd, C)
    if gcd != 0:
        A, B, C = A // gcd, B // gcd, C // gcd
    if A < 0:
        A, B, C = -A, -B, -C
    return A, B, C

def line_equation(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    if x2 - x1 == 0:
        return None, None, None, None
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    A = y2 - y1
    B = x1 - x2
    C = A * x1 + B * y1
    A, B, C = reduce_coefficients(A*1000, B*1000, C*1000)
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
    
    slope = -1 / ((y2 - y1) / (x2 - x1))
    b = mid_y - slope * mid_x
    A = slope
    B = -1
    C = A * mid_x + B * mid_y  
    A, B, C = reduce_coefficients(int(A * 1000), int(B * 1000), int(C * 1000))
    return A, B, C, slope, b

def calculate_angle(A, B, C):
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    
    dot_product = AB[0] * BC[0] + AB[1] * BC[1]
    magnitude_AB = math.sqrt(AB[0] ** 2 + AB[1] ** 2)
    magnitude_BC = math.sqrt(BC[0] ** 2 + BC[1] ** 2)
    
    angle_radians = math.acos(dot_product / (magnitude_AB * magnitude_BC))
    angle_degrees = math.degrees(angle_radians)
    
    return 180 - angle_degrees

while True:
    print("Enter nothing to exit the program")
    print("1 - Money (Tax & Tip on subtotal)")
    print("2 - Geometry (Coordinate Plane / Shapes)")
    choice = input()
    if choice == "":
        exit()
    elif choice == "1":
        print("Enter as percentages without % sign")
        print("Enter tax: ")
        tax = float(input()) / 100
        print("Enter tip: ")
        tip = float(input()) / 100
        print("Enter prices or nothing to stop")
        subtotal = 0
        while True:
            x = input()
            if x == "":
                break
            subtotal += float(x)
        total = subtotal * (1 + tax + tip)
        print("Total: " + str(total))
    elif choice == "2":
        print("1 - Area and Perimeter (coordinate)")
        print("2 - Equation and Bisector of 2 points")
        print("2 - Angle (3 points)")
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
                print(f"1. {A}x + {B}y = {C}")
                print(f"2. y = {m}x + {b}")
                A_bisector, B_bisector, C_bisector, slope_bisector, b_bisector = perpendicular_bisector(points[0], points[1])
                print("Perpendicular Bisector: ")
                print(f"1. {A_bisector}x + {B_bisector}y = {C_bisector}")
                if slope_bisector is not None:
                    print(f"2. y = {slope_bisector}x + {b_bisector}")
                else:
                    print(f"2. x = {b_bisector}")
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
