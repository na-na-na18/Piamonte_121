x = 300

print("Find the closest number to", x)

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

def closest_to_x(num1, num2, num3):
    diff1 = abs(x - num1)
    diff2 = abs(x - num2)
    diff3 = abs(x - num3)

    if diff1 <= diff2 and diff1 <= diff3:
        return "A or " + str(num1)
    elif diff2 <= diff1 and diff2 <= diff3:
        return "B or " + str(num2)
    else:
        return "C or " + str(num3)

result = closest_to_x(a, b, c)
print("Letter", result, "is the closest number to", x)
