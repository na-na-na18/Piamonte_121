print("Find the largest number among three numbers entered by the user.") 

def checking(A, B, C):
   
    if A >  B and A > C:
        print(f"The largest number is {A}\n")
        
    elif B >  A and B > C:
        print(f"The largest number is {B}\n")
        
    elif C > A and C > B:
        print(f"The largest number is {C}\n")
        
    elif A == B == C:
        print(f"{A}, {B}, {C} are equal.\n")

A = int(input("Enter your first number: "))
B = int(input("Enter your second number: "))
C = int(input("Enter your third number: "))        
        
    
checking (A, B, C)    
