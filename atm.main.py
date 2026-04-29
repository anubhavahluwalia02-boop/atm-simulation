import atm_service

while True:
    print("\n====== ATM MENU ======")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Balance: ₹", atm_service.get_balance())

    elif choice == "2":
        try:
            amt = int(input("Enter amount: "))
            print(atm_service.deposit(amt))
        except:
            print("Invalid input")

    elif choice == "3":
        try:
            amt = int(input("Enter amount: "))
            print(atm_service.withdraw(amt))
        except:
            print("Invalid input")

    elif choice == "4":
        print("\n--- Statement ---")
        for t in atm_service.get_statement():
            print(t)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")