class BankAccount:
    """
    A simple BankAccount class to demonstrate OOP principles.
    Encapsulates banking operations like deposit, withdraw, and balance display.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float): The starting balance for the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__account_balance = initial_balance # Using __ for "private" attribute

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__account_balance += amount
        # print(f"Successfully deposited: ${amount}. New balance: ${self.__account_balance}") # For debugging/extra info

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds).
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            # print(f"Successfully withdrew: ${amount}. New balance: ${self.__account_balance}") # For debugging/extra info
            return True

    def display_balance(self):
        """
        Prints the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

    # Optional: You might want a getter method for the balance if needed for other parts of a larger system,
    # but for this assignment, display_balance() is sufficient for showing it.
    # def get_balance(self):
    #     return self.__account_balance