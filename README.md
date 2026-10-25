# Mini Banking System Using Python

## Project Overview

The Mini Banking System is a beginner-friendly, menu-driven console application developed using Python. It simulates basic banking operations, allowing users to deposit money, withdraw money, check their account balance, and view transaction history.

The project demonstrates object-oriented programming, input validation, exception handling, and transaction tracking.

## Features

- Create an account using the account holder's name.
- Set an initial account balance.
- Deposit money into the account.
- Withdraw money with insufficient-balance validation.
- Check the current account balance.
- View timestamped transaction history.
- Handle invalid inputs and menu choices.
- Display monetary values to two decimal places.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Classes and Objects
- Exception Handling
- Lists
- Date and Time Handling
- Input Validation

## Project Structure

```text
mini-banking-system/
│
├── banking_system.py
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Install Python

Install Python 3 from:

https://www.python.org/downloads/

Verify your installation:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/shashisoppin/mini-banking-system.git
```

### 3. Navigate to the Project Directory

```bash
cd mini-banking-system
```

### 4. Run the Application

```bash
python banking_system.py
```

No third-party Python packages are required.

## How to Use

1. Enter the account holder's name.
2. Enter the initial deposit, or enter `0` to start without a balance.
3. Select an operation from the displayed menu.
4. Enter the amount when depositing or withdrawing.
5. Check your balance or view your transaction history.
6. Select option 5 to exit the application.

## Example Output

```text
Welcome to the Mini Banking System!
Enter your name: Alex
Enter your initial deposit (enter 0 if none): $100

--- Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. View Transaction History
5. Exit

Enter your choice: 1
Enter amount to deposit: $50
Deposited: $50.00
Current balance: $150.00
```

## Validation and Error Handling

The application validates user input to help prevent common errors:

- Negative initial balances are rejected.
- Deposits and withdrawals must be greater than zero.
- Withdrawals cannot exceed the available balance.
- Invalid numeric inputs are handled with error messages.
- Amounts with more than two decimal places are rejected.
- Invalid menu selections do not terminate the application.

## Learning Outcomes

Through this project, I practiced:

- Designing classes and objects in Python.
- Using constructors and instance attributes.
- Implementing methods to manage account operations.
- Applying conditional statements and loops.
- Handling exceptions using `try` and `except`.
- Maintaining transaction history with lists.
- Formatting monetary values and timestamps.

## Future Improvements

- Store account information in an SQLite database.
- Add multiple accounts.
- Implement secure authentication.
- Add automated unit tests.
- Build a graphical user interface or web application.

## Disclaimer

This project is for educational purposes only. It is a console-based simulation and is not connected to real banking services. Account information and transactions are not persisted between program executions.

---

**Project Type:** Python Beginner Project  
**Author:** YOUR NAME