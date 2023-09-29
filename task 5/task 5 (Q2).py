def Area_rectangle(length,width):
    if length <= 0 or width <= 0:
        raise ValueError("length and width are not positive numbers")
    area = width * length
    return area

def perimeter_rectangle(length,width):
    if length <= 0 or width <= 0:
        raise ValueError("length and width are not positive numbers")
    perimeter = (width + length) / 2
    return perimeter

try:
    length = int(input("Enter The Length : "))
    width = int(input("Enter The Width : "))
    Area_rectangle(length,width)
    perimeter_rectangle(length, width)
    print("the area for rectangle is :",Area_rectangle(length,width))
    print("the perimeter for rectangle is :",perimeter_rectangle(length,width))
except Exception as e:
    print("just positive inputs")