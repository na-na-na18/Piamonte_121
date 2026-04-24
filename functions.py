num1 = 5
num2 = 3

def funtion():
    while True:
        print("Operations: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter the operation number: "))
    
        if choice == 1:
            result = num1 + num2
            print(result)
        
        elif choice == 2:
            result = num1 - num2
            print(result)
    
        elif choice == 3:
            result = num1 * num2
            print(result)
        
        elif choice == 4:
            result = num1 / num2
            print(result)
    
        elif choice == 5:
            print("Exiting the program.")
            break

funtion()   
