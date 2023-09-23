def add(x, y):
    total = x + y
    return total


def sub(x, y):
    total = x - y
    return total


def mul(x, y):
    total = x * y
    return total


def div(x, y):
    total = x / y
    return total


x = int(input("Enter Number 1 :"))
y = int(input("Enter Nmuber 2 :"))
print("Total after ADD :", add(x, y))
print("Total after SUB :", sub(x, y))
print("Total after MUL :", mul(x, y))
print("Total after DIV :", div(x, y))
print("----------------- part 2 -----------------")
print("""If You Want to Calculate rectangle area type >> 1 <
If You Want to Calculate circle area type >> 2 <
If You Want to Calculate triangle area type >> 3 <
-If not type >> 0 <""")
N = int(input())
if N == 1:
    L = int(input("Enter the length :"))
    W = int(input("Enter the width :"))
    sum = L * W
    print("The area is : ", sum)
elif N == 2:
    R = int(input("Enter the Radius :"))
    sum = 3.14 * R * R
    print("The area is : ", sum)
elif N == 3:
    B = int(input("Enter the Base :"))
    H = int(input("Enter the Height :"))
    sum = B * H / 2
    print("The area is : ", sum)

else:
    print("^_^ THANKS YOU ^_^")
