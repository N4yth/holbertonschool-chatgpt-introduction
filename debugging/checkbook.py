# Define the Checkbook class to manage balance, deposits, and withdrawals
class Checkbook:
    def __init__(self):
        self.balance = 0.0  # Initialize balance to zero

    # Method to deposit money into the checkbook
    def deposit(self, amount):
        self.balance += amount  # Increase balance
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    # Method to withdraw money from the checkbook
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount  # Decrease balance
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    # Method to display the current balance
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

# Function to safely get a valid positive amount from the user
def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))  # Try converting input to float
            if amount <= 0:
                print("Amount must be greater than zero.")  # Reject non-positive numbers
            else:
                return amount  # Valid amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Handle non-numeric input

# Main function to drive the program
def main():
    cb = Checkbook()  # Create an instance of Checkbook
    while True:
        # Ask the user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break  # Exit the loop and end the program
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")  # Get a valid deposit amount
            cb.deposit(amount)  # Call deposit method
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")  # Get a valid withdrawal amount
            cb.withdraw(amount)  # Call withdraw method
        elif action == 'balance':
            cb.get_balance()  # Show current balance
        else:
            print("Invalid command. Please try again.")  # Handle unknown commands

# Only run the program if this script is executed directly
if __name__ == "__main__":
    main()