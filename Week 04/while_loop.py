MENU = "l) Login, S) Sign up, Q) Quit"

done = False
while not done:
    print(MENU)
    user_choice = input("Choose [l/s/q]: ")
    if user_choice == "l":
        print("Logging you in...")
    elif user_choice == "s":
        print("Signing you up...")
    elif user_choice == "q":
        print("Quitting the program...")
        done = True
    else:
        print("Invalid choice")
