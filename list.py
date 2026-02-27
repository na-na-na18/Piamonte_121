users = []

while True:
    print("\nMenu:")
    print("1. Show users")
    print("2. Add user")
    print("3. Update user")
    print("4. Delete user")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        if users:
            print("\nUser List:")
            for index, user in enumerate(users, start=1):
                print(f"{index}. {user}")
        else:
        
            print("\nNo users found.")

    elif choice == '2':
        new_user = input("Enter the name of the new user: ")
        users.append(new_user)
        print(f"{new_user} has been added to the user list.")

    elif choice == '3':
        if users:
            user_index = int(input("Enter the number of the user to update: ")) - 1
            if 0 <= user_index < len(users):
                updated_user = input("Enter the new name for the user: ")
                users[user_index] = updated_user
                print(f"User {user_index + 1} has been updated to {updated_user}.")
            else:
                print("Invalid user number.")
        else:
            print("\nNo users found.")

    elif choice == '4':
        if users:
            user_index = int(input("Enter the number of the user to delete: ")) - 1
            if 0 <= user_index < len(users):
                deleted_user = users.pop(user_index)
                print(f"{deleted_user} has been deleted from the user list.")
            else:
                print("Invalid user number.")
        else:
            print("\nNo users found.")

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
