import random
from datetime import datetime

# Dictionary to store all bank accounts
accounts = {}


# -------------------------------------------------
# 1. CREATE BANK ACCOUNT
# -------------------------------------------------
def create_account():
    print("\n================================")
    print("        CREATE BANK ACCOUNT")
    print("================================")

    name = input("Enter your name: ").strip()
    phone = input("Enter your phone number: ").strip()

    # Check name
    if name == "":
        print("Name cannot be empty.")
        return

    # Check phone number
    if not phone.isdigit():
        print("Please enter a valid phone number.")
        return

    # Create PIN
    pin = input("Create a 4-digit PIN: ")

    if not pin.isdigit() or len(pin) != 4:
        print("PIN must contain exactly 4 digits.")
        return

    # Generate unique account number
    while True:
        account_number = str(random.randint(10000000, 99999999))

        if account_number not in accounts:
            break

    # Store account details
    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("--------------------------------")
    print("Account Number :", account_number)
    print("Account Holder :", name)
    print("Phone Number   :", phone)
    print("Balance        : ₹0.00")
    print("--------------------------------")
    print("Please remember your Account Number and PIN.")


# -------------------------------------------------
# 2. LOGIN USING ACCOUNT NUMBER & PIN
# -------------------------------------------------
def login():
    print("\n================================")
    print("             LOGIN")
    print("================================")

    account_number = input("Enter Account Number: ").strip()
    pin = input("Enter PIN: ").strip()

    if account_number not in accounts:
        print("Account not found.")
        return

    if accounts[account_number]["pin"] != pin:
        print("Incorrect PIN.")
        return

    print("\nLogin successful!")
    print("Welcome,", accounts[account_number]["name"])

    # Open account menu
    account_menu(account_number)


# -------------------------------------------------
# 3. CHECK ACCOUNT BALANCE
# -------------------------------------------------
def check_balance(account_number):
    print("\n================================")
    print("        ACCOUNT BALANCE")
    print("================================")

    balance = accounts[account_number]["balance"]

    print("Account Number :", account_number)
    print("Account Holder :", accounts[account_number]["name"])
    print("Current Balance: ₹" + format(balance, ".2f"))


# -------------------------------------------------
# 4. DEPOSIT MONEY
# -------------------------------------------------
def deposit_money(account_number):
    print("\n================================")
    print("          DEPOSIT MONEY")
    print("================================")

    try:
        amount = float(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        # Add amount to balance
        accounts[account_number]["balance"] += amount

        # Record transaction
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        transaction = (
            time + " | Deposit | ₹" + format(amount, ".2f")
        )

        accounts[account_number]["transactions"].append(transaction)

        print("\nDeposit successful!")
        print("Deposited Amount : ₹" + format(amount, ".2f"))
        print(
            "New Balance      : ₹"
            + format(accounts[account_number]["balance"], ".2f")
        )

    except ValueError:
        print("Please enter a valid amount.")


# -------------------------------------------------
# 5. WITHDRAW MONEY
# -------------------------------------------------
def withdraw_money(account_number):
    print("\n================================")
    print("         WITHDRAW MONEY")
    print("================================")

    try:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        current_balance = accounts[account_number]["balance"]

        # Check balance before deduction
        if amount > current_balance:
            print("\nInsufficient balance!")
            print("Available Balance: ₹" + format(current_balance, ".2f"))
            return

        # Deduct amount
        accounts[account_number]["balance"] -= amount

        # Record transaction
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        transaction = (
            time + " | Withdrawal | ₹" + format(amount, ".2f")
        )

        accounts[account_number]["transactions"].append(transaction)

        print("\nWithdrawal successful!")
        print("Withdrawn Amount : ₹" + format(amount, ".2f"))
        print(
            "Remaining Balance: ₹"
            + format(accounts[account_number]["balance"], ".2f")
        )

    except ValueError:
        print("Please enter a valid amount.")


# -------------------------------------------------
# 6. TRANSFER MONEY BETWEEN ACCOUNTS
# -------------------------------------------------
def transfer_money(account_number):
    print("\n================================")
    print("       TRANSFER MONEY")
    print("================================")

    receiver_account = input(
        "Enter receiver Account Number: "
    ).strip()

    # Check receiver account
    if receiver_account not in accounts:
        print("Receiver account not found.")
        return

    # Prevent transfer to same account
    if receiver_account == account_number:
        print("You cannot transfer money to your own account.")
        return

    try:
        amount = float(input("Enter amount to transfer: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        # Check sender balance
        if amount > accounts[account_number]["balance"]:
            print("Insufficient balance!")
            return

        # Deduct money from sender
        accounts[account_number]["balance"] -= amount

        # Add money to receiver
        accounts[receiver_account]["balance"] += amount

        # Record date and time
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Sender transaction
        sender_transaction = (
            time
            + " | Transfer Sent | ₹"
            + format(amount, ".2f")
            + " | To Account: "
            + receiver_account
        )

        # Receiver transaction
        receiver_transaction = (
            time
            + " | Transfer Received | ₹"
            + format(amount, ".2f")
            + " | From Account: "
            + account_number
        )

        accounts[account_number]["transactions"].append(
            sender_transaction
        )

        accounts[receiver_account]["transactions"].append(
            receiver_transaction
        )

        print("\nTransfer successful!")
        print("Transferred Amount: ₹" + format(amount, ".2f"))
        print("Receiver Account  :", receiver_account)
        print(
            "Remaining Balance : ₹"
            + format(accounts[account_number]["balance"], ".2f")
        )

    except ValueError:
        print("Please enter a valid amount.")


# -------------------------------------------------
# 7. VIEW TRANSACTION HISTORY
# -------------------------------------------------
def transaction_history(account_number):
    print("\n================================")
    print("       TRANSACTION HISTORY")
    print("================================")

    transactions = accounts[account_number]["transactions"]

    if len(transactions) == 0:
        print("No transactions available.")
        return

    for number, transaction in enumerate(transactions, start=1):
        print(str(number) + ". " + transaction)


# -------------------------------------------------
# 8. CHANGE PIN
# -------------------------------------------------
def change_pin(account_number):
    print("\n================================")
    print("           CHANGE PIN")
    print("================================")

    old_pin = input("Enter old PIN: ")

    # Check old PIN
    if old_pin != accounts[account_number]["pin"]:
        print("Incorrect old PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ")

    if not new_pin.isdigit() or len(new_pin) != 4:
        print("PIN must contain exactly 4 digits.")
        return

    confirm_pin = input("Confirm new PIN: ")

    # Confirm new PIN
    if new_pin != confirm_pin:
        print("New PINs do not match.")
        return

    # Update PIN
    accounts[account_number]["pin"] = new_pin

    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    transaction = time + " | PIN Changed"

    accounts[account_number]["transactions"].append(transaction)

    print("PIN changed successfully!")


# -------------------------------------------------
# 9. ACCOUNT MENU + LOGOUT
# -------------------------------------------------
def account_menu(account_number):

    while True:

        print("\n================================")
        print("          ACCOUNT MENU")
        print("================================")
        print("1. Check Account Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            check_balance(account_number)

        elif choice == "2":

            deposit_money(account_number)

        elif choice == "3":

            withdraw_money(account_number)

        elif choice == "4":

            transfer_money(account_number)

        elif choice == "5":

            transaction_history(account_number)

        elif choice == "6":

            change_pin(account_number)

        elif choice == "7":

            print("\nLogging out...")
            print("You have been logged out successfully.")
            print("Returning to main menu.")
            break

        else:

            print("Invalid choice!")
            print("Please select a number from 1 to 7.")


# -------------------------------------------------
# MAIN MENU
# -------------------------------------------------
def main():

    while True:

        print("\n")
        print("========================================")
        print("           BANKING SYSTEM")
        print("========================================")
        print("1. Create Bank Account")
        print("2. Login")
        print("3. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            create_account()

        elif choice == "2":

            login()

        elif choice == "3":

            print("\nThank you for using the Banking System!")
            print("Goodbye!")
            break

        else:

            print("Invalid choice!")
            print("Please select 1, 2, or 3.")


# -------------------------------------------------
# START PROGRAM
# -------------------------------------------------
if __name__ == "__main__":
    main()