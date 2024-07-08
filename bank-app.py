# Mooey Bank

def create_account():
    """Creates a new account.

        The user is prompted to enter their first name, last name, and age.
        The function ensures that the first and last names are alphabetic and that the age is a digit.
        The age must be between 18 and 99.

        Returns:
            tuple: A tuple containing the first name, last name, and age of the user.
        """
    while True:
        first_name = input("Enter your first name: ")
        if first_name.isalpha():
            break
        else:
            print("First name must be alphabetic characters only. Please try again.")

    while True:
        last_name = input("Enter your last name: ")
        if last_name.isalpha():
            break
        else:
            print("Last name must be alphabetic characters only. Please try again.")

    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            age = int(age)
            if age < 18:
                print("\nAge must be 18 or older. Please try again.\n")
            elif age > 99:
                print("\nYou are too old to be a member of Mooey Bank. BOOMER. Please try again.\n")
            else:
                break
        else:
            print("\nAge must be a number. Please try again.\n")

    print(f"\nAccount created for {first_name} {last_name}, Age: {age}")
    return first_name, last_name, age


def show_account_details(acc_details):
    """Displays the account details.

        The function prints the first name, last name, and age of the user.
        The user is then prompted to press 1 to go back to the main menu.

        Args:
            acc_details (tuple): A tuple containing the first name, last name, and age of the user.
        """
    first_name, last_name, age = acc_details
    print(f"\nAccount Details:\nFirst Name: {first_name}\nLast Name: {last_name}\nAge: {age}")
    while True:
        back_to_menu = input("\nPress 1 to go back to the main menu: ")
        if back_to_menu == '1':
            break
        else:
            print("Invalid choice. Please press 1 to go back to the main menu.")


def manage_balance(balance, transaction_history):
    """Manages the balance of the account.

        The user is shown their current balance and given options to add money, view transaction history, or go back to
        the main menu.

        Args:
            balance (float): The current balance of the account.
            transaction_history (list): A list of all transactions.

        Returns:
            tuple: A tuple containing the updated balance and transaction history.
        """
    while True:
        print(f"\nCurrent Balance: ${balance:.2f}")
        print("\nPress 1 to add money")
        print("Press 2 to view transaction history")
        print("Press 3 to go back to the main menu")
        back_to_menu = input("\nChoose an option: ")
        if back_to_menu == '1':
            while True:
                try:
                    amount = float(input("\nEnter amount to add: $"))
                    if amount > 0:
                        balance += amount
                        transaction_history.append(f"Added ${amount:.2f} to account.")
                        print(f"\n${amount:.2f} added to your account.")
                        break
                    else:
                        print("Amount must be a positive number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif back_to_menu == '2':
            if transaction_history:
                print("\nTransaction History:")
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("\nNo transactions yet.")
        elif back_to_menu == '3':
            break
        else:
            print(
                "Invalid choice. Please press 1 to add money, 2 to view transaction history, or 3 to go back to the"
                " main menu.")
    return balance, transaction_history


def manage_beneficiaries(beneficiaries):
    """Manages the beneficiaries of the account.

        The user is shown a list of beneficiaries and given options to add a beneficiary or go back to the main menu.

        Args:
            beneficiaries (list): A list of all beneficiaries.

        Returns:
            list: The updated list of beneficiaries.
        """
    while True:
        if beneficiaries:
            print("\nBeneficiary List:")
            for i, beneficiary in enumerate(beneficiaries, start=1):
                print(f"{i}. {beneficiary}")
        else:
            print("\nNo beneficiaries added yet.")
        print("\nPress 1 to add a beneficiary")
        print("Press 2 to go back to the main menu")
        back_to_menu = input("\nChoose an option: ")
        if back_to_menu == '1':
            while True:
                beneficiary_first_name = input("\nEnter beneficiary's first name: ")
                if beneficiary_first_name.isalpha():
                    break
                else:
                    print("First name must be alphabetic characters only. Please try again.")
            while True:
                beneficiary_last_name = input("Enter beneficiary's last name: ")
                if beneficiary_last_name.isalpha():
                    break
                else:
                    print("Last name must be alphabetic characters only. Please try again.")
            beneficiary = f"{beneficiary_first_name} {beneficiary_last_name}"
            beneficiaries.append(beneficiary)
            print(f"\nBeneficiary '{beneficiary}' added.")
        elif back_to_menu == '2':
            break
        else:
            print("Invalid choice. Please press 1 to add a beneficiary or 2 to go back to the main menu.")
    return beneficiaries


def send_money(balance, beneficiaries, transaction_history):
    """Sends money to a beneficiary.

        The user is given options to add a beneficiary, add money, or go back to the main menu.
        If the user chooses to send money, they are shown a list of beneficiaries and prompted to choose one.
        The user then enters the amount to send. The function ensures that the user has sufficient balance.

        Args:
            balance (float): The current balance of the account.
            beneficiaries (list): A list of all beneficiaries.
            transaction_history (list): A list of all transactions.

        Returns:
            tuple: A tuple containing the updated balance, beneficiaries, and transaction history.
        """
    while True:
        valid_options = []
        if not beneficiaries:
            print("\nYou have no beneficiaries.")
            print("Press 1 to add a beneficiary")
            valid_options.append('1')
        if balance == 0:
            print("\nYou have no money.")
            print("Press 2 to add money")
            valid_options.append('2')
        if not valid_options:
            break
        print("Press 3 to go back to the main menu")
        valid_options.append('3')

        back_to_menu = input("\nChoose an option: ")

        if back_to_menu not in valid_options:
            print("Invalid choice. Please select a valid option.")
            continue

        if back_to_menu == '1' and '1' in valid_options:
            while True:
                beneficiary_first_name = input("\nEnter beneficiary's first name: ")
                if beneficiary_first_name.isalpha():
                    break
                else:
                    print("First name must be alphabetic characters only. Please try again.")
            while True:
                beneficiary_last_name = input("Enter beneficiary's last name: ")
                if beneficiary_last_name.isalpha():
                    break
                else:
                    print("Last name must be alphabetic characters only. Please try again.")
            beneficiary = f"{beneficiary_first_name} {beneficiary_last_name}"
            beneficiaries.append(beneficiary)
            print(f"\nBeneficiary '{beneficiary}' added.")
        elif back_to_menu == '2' and '2' in valid_options:
            while True:
                try:
                    amount = float(input("\nEnter amount to add: $"))
                    if amount > 0:
                        balance += amount
                        transaction_history.append(f"Added ${amount:.2f} to account.")
                        print(f"\n${amount:.2f} added to your account.")
                        break
                    else:
                        print("Amount must be a positive number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif back_to_menu == '3':
            return balance, beneficiaries, transaction_history

    while True:
        print("\nBeneficiary List:")
        for i, beneficiary in enumerate(beneficiaries, start=1):
            print(f"{i}. {beneficiary}")
        print(f"{len(beneficiaries) + 1}. Go back to the main menu")
        try:
            back_to_menu = int(input("\nChoose a beneficiary to send money to, or return to the main menu: "))
            if 1 <= back_to_menu <= len(beneficiaries):
                beneficiary = beneficiaries[back_to_menu - 1]
                while True:
                    try:
                        amount = float(
                            input(f"\nAvailable balance: ${balance:.2f}\nEnter amount to send to {beneficiary}: $"))
                        if 0 < amount <= balance:
                            balance -= amount
                            transaction_history.append(
                                f"Sent ${amount:.2f} to {beneficiary}. New balance: ${balance:.2f}")
                            print(f"\n${amount:.2f} sent to {beneficiary}. New balance: ${balance:.2f}")
                            break
                        else:
                            print("Insufficient funds or invalid amount. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
            elif back_to_menu == len(beneficiaries) + 1:
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return balance, beneficiaries, transaction_history


def main_menu(acc_details):
    """Displays the main menu.

        The user is shown the main menu and prompted to choose an option.
        The options include viewing account details, managing balance, managing beneficiaries, sending money, and
        exiting the bank.

        Args:
            acc_details (tuple): A tuple containing the first name, last name, and age of the user.
        """
    balance = 0.0
    beneficiaries = []
    transaction_history = []

    menu_items = [
        "1. Account Details",
        "2. Balance",
        "3. Beneficiary List",
        "4. Send Money",
        "5. Exit Mooey Bank"
    ]

    while True:
        print("\nMain Menu")
        for item in menu_items:
            print(item)
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            show_account_details(acc_details)

        elif choice == '2':
            balance, transaction_history = manage_balance(balance, transaction_history)  # Pass transaction_history

        elif choice == '3':
            beneficiaries = manage_beneficiaries(beneficiaries)

        elif choice == '4':
            balance, beneficiaries, transaction_history = send_money(balance, beneficiaries, transaction_history)

        elif choice == '5':
            first_name, last_name, age = acc_details
            print(f"\nExiting Mooey Bank. Thanks for banking with us {first_name} {last_name}. Have a great day!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


try:
    if __name__ == "__main__":
        print("Welcome to Mooey Bank, let's get started with your account sign-up!\n")
        account_details = create_account()
        main_menu(account_details)
except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting Mooey Bank. Have a great day!")
    exit()
