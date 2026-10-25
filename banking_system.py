
from datetime import datetime


class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.  ")

        self.account_holder = account_holder
        self.balance = round(initial_balance, 2)
        self.transaction_history = []

        if self.balance > 0:
            self.transaction_history.append(
                f"{self._timestamp()} | Initial deposit: "
                f"${self.balance:.2f}"
            )

    @staticmethod
    def _timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def _validate_amount(amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if round(amount, 2) != amount:
            raise ValueError("Amount cannot have more than two decimal places.")

    def deposit(self, amount):
        self._validate_amount(amount)

        self.balance = round(self.balance + amount, 2)

        self.transaction_history.append(
            f"{self._timestamp()} | Deposit: ${amount:.2f}"
        )

        print(f"Deposited: ${amount:.2f}")
        print(f"Current balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        self._validate_amount(amount)

        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")

        self.balance = round(self.balance - amount, 2)

        self.transaction_history.append(
            f"{self._timestamp()} | Withdrawal: ${amount:.2f}"
        )

        print(f"Withdrawn: ${amount:.2f}")
        print(f"Current balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ${self.balance:.2f}")

    def view_transaction_history(self):
        print("\n--- Transaction History ---")

        if not self.transaction_history:
            print("No transactions yet.")
            return

        for transaction in self.transaction_history:
            print(transaction)


def get_amount(prompt):
    amount_text = input(prompt).strip()

    try:
        amount = float(amount_text)
    except ValueError:
        raise ValueError("Please enter a valid numeric amount.")

    if not amount_text or not amount < float("inf"):
        raise ValueError("Please enter a finite amount.")

    if amount != amount or amount == float("-inf"):
        raise ValueError("Please enter a finite amount.")

    if round(amount, 2) != amount:
        raise ValueError("Please enter an amount with at most two decimal places.")

    return round(amount, 2)


def main():
    print("Welcome to the Mini Banking System!")

    name = input("Enter your name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    while True:
        try:
            initial_balance = get_amount(
                "Enter your initial deposit (enter 0 if none): $"
            )

            if initial_balance < 0:
                raise ValueError("Initial balance cannot be negative.")

            account = BankAccount(name, initial_balance)
            break

        except ValueError as error:
            print(f"Error: {error} Please try again.")

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                amount = get_amount("Enter amount to deposit: $")
                account.deposit(amount)

            elif choice == "2":
                amount = get_amount("Enter amount to withdraw: $")
                account.withdraw(amount)

            elif choice == "3":
                account.check_balance()

            elif choice == "4":
                account.view_transaction_history()

            elif choice == "5":
                print(
                    "Thank you for using the Mini Banking System. Goodbye!"
                )
                break

            else:
                print("Invalid choice. Please select an option from 1 to 5.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
