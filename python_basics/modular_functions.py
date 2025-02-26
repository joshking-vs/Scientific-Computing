import math

shapes = ["circle","triangle","rectangle"]

def calculate_area(shape,dimension1,dimension2=0):
    

    if (shape == "circle"):
        area = math.pi * dimension1**2
        return area

    elif(shape == "triangle"):
        area = 0.5 * dimension1 * dimension2
        return area

    elif(shape == "rectangle" ):
        area = dimension1 * dimension2
        return area
    
    

shape = input("Enter your shape(circle/triange/rectangle): ").strip().lower()

if shape == "circle":
    dimension1 = float(input("enter your radius: "))
    print(f"area :{calculate_area(shape,dimension1)}")

elif shape=="triangle":
    dimension1= float(input("base: "))
    dimension2= float(input("height: "))
    print(f"area :{calculate_area(shape,dimension1,dimension2)}")

elif shape =="rectangle":
    dimension1= float(input("length: "))
    dimension2= float(input("width: "))
    print(f"area :{calculate_area(shape,dimension1,dimension2)}")

else:
    print("invalid shape entered")


