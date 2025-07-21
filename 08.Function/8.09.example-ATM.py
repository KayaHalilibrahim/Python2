# ATM Application

# Account information will be stored. (dict)
# menu, withdrawMoney, checkBalance, depositMoney functions will be defined.
# If the amount to be withdrawn is not in the account,
# the user will be asked if they want to use the extra account.


# ATM Application

# Account information will be stored. (dict)

accounts = [
    {
        "name": "Halil Kaya",
        "accountNo": "12345",
        "balance": 20000,
        "extraAccount": 5000,
        "username": "halilkaya",
        "password": "1234"
    },
    {
        "name": "Mehmet Kaya",
        "accountNo": "12345",
        "balance": 30000,
        "extraAccount": 10000,
        "username": "mehmetkaya",
        "password": "1234"
    }
]

def login(username, password):
    for account in accounts:
        if account["username"] == username and account["password"] == password:
            print(f"\nLogin successful. Welcome, {account['name']}!")
            menu(account)
            return
    print("Login failed. Incorrect username or password.\n")

def menu(account):
    while True:
        print("\nWhat do you want to do?")
        print("1 - Withdraw money")
        print("2 - Deposit money")
        print("3 - Balance inquiry")
        print("4 - Quit")

        select = input("Enter a number (1, 2, 3, 4): ")

        if select == "1":
            withdrawMoney(account)
        elif select == "2":
            depositMoney(account)
        elif select == "3":
            checkBalance(account)
        elif select == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

def withdrawMoney(account):
    amount = int(input("Enter amount to withdraw: "))
    if account["balance"] >= amount:
        account["balance"] -= amount
        print(f"Withdrawal successful. New balance: {account['balance']} TL")
    else:
        total_available = account["balance"] + account["extraAccount"]
        if total_available >= amount:
            use_extra = input("Not enough balance. Do you want to use extra account? (y/n): ")
            if use_extra.lower() == "y":
                required = amount - account["balance"]
                account["balance"] = 0
                account["extraAccount"] -= required
                print(f"Withdrawal successful using extra account.\nRemaining extra account: {account['extraAccount']} TL")
            else:
                print("Transaction cancelled.")
        else:
            print("Insufficient funds. Cannot complete withdrawal.")

def depositMoney(account):
    amount = int(input("Enter amount to deposit: "))
    account["balance"] += amount
    print(f"Deposit successful. New balance: {account['balance']} TL")

def checkBalance(account):
    print(f"Main balance: {account['balance']} TL")
    print(f"Extra account: {account['extraAccount']} TL")

# --- Run the program ---
# Example login (you can later loop this or ask repeatedly)
user = input("Enter username: ")
pw = input("Enter password: ")
login(user, pw)


