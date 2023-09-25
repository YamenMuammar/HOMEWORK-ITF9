# def add(x, y):
#     total = x + y
#     return total
#
#
# def sub(x, y):
#     total = x - y
#     return total
#
#
# def mul(x, y):
#     total = x * y
#     return total
#
#
# def div(x, y):
#     total = x / y
#     return total
#
#
# x = int(input("Enter Number 1 :"))
# y = int(input("Enter Nmuber 2 :"))
# print("Total after ADD :", add(x, y))
# print("Total after SUB :", sub(x, y))
# print("Total after MUL :", mul(x, y))
# print("Total after DIV :", div(x, y))
# print("----------------- part 2 -----------------")
# print("""If You Want to Calculate rectangle area type >> 1 <
# If You Want to Calculate circle area type >> 2 <
# If You Want to Calculate triangle area type >> 3 <
# If not type >> 0 <""")
# N = int(input())
# if N == 1:
#     L = int(input("Enter the length :"))
#     W = int(input("Enter the width :"))
#     sum = L * W
#     print("The area is : ", sum)
# elif N == 2:
#     R = int(input("Enter the Radius :"))
#     sum = 3.14 * R * R
#     print("The area is : ", sum)
# elif N == 3:
#     B = int(input("Enter the Base :"))
#     H = int(input("Enter the Height :"))
#     sum = B * H / 2
#     print("The area is : ", sum)
#
# else:
#     print("^_^ THANKS YOU ^_^")

def get_inputs():
    n1 = int(input("Enter Number 1 : "))
    n2 = int(input("Enter Number 2 : "))
    return [n1,n2]
def get_inputs_2():
    B = int(input("Enter THE Base : "))
    H = int(input("Enter the height : "))
    return [B,H]
def get_inputs_3():
    R = int(input("Enter THE Radius : "))
    return [R]
def get_inputs_4():
    L = int(input("Enter THE Length : "))
    W = int(input("Enter the Width : "))
    return [L,W]

def get_sum(n1,n2):
    return n1 + n2
def get_sub(n1,n2):
    return n1 - n2
def get_mul(n1,n2):
    return n1 * n2
def get_div(n1,n2):
    return n1 / n2
def get_tri(B,H):
    return B * H / 2
def get_cir(R):
    return R * R * 3.14
def get_rec(L,H):
    return L *H


while True:
    selection = int(input("""1. Sum
2. Subtract
3. Multiply
4. Division
5. Calculate triangle area
6. Calculate circle area
7. Calculate rectangle area
8. Exit
>>>>>>>"""))
    if selection == 1:
        numbers = get_inputs()
        result = get_sum(numbers[0],numbers[1])
        print(f"Sum {numbers} = ", result)

    elif selection == 2:
        numbers = get_inputs()
        result = get_sub(numbers[0],numbers[1])
        print(f"Sub {numbers} =", result)
    elif selection == 3:
        numbers = get_inputs()
        result = get_mul(numbers[0],numbers[1])
        print(f"Mul {numbers} =", result)
    elif selection == 4:
        numbers = get_inputs()
        result = get_div(numbers[0],numbers[1])
        print(f"Div {numbers} =", result)
    elif selection == 5:
        numbers = get_inputs_2()
        result = get_tri(numbers[0],numbers[1])
        print(f" area {numbers} =", result)
    elif selection == 6:
        numbers = get_inputs_3()
        result = get_cir(numbers[0])
        print(f" area {numbers} =", result)
    elif selection == 7:
        numbers = get_inputs_4()
        result = get_rec(numbers[0],numbers[1])
        print(f" area {numbers} =", result)
    elif selection == 8:
        print("^_^ THANKS YOU ^_^")
        exit()
