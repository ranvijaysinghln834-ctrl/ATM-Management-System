class Atm:
    # Constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
Hi, how can I help you?
1. Press 1 to create PIN
2. Press 2 to change PIN
3. Press 3 to check balance
4. Press 4 to withdraw
5. Press 5 to exit
Enter your choice: """)

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.change_pin()
            elif user_input == "3":
                self.check_balance()
            elif user_input == "4":
                self.withdraw()
            elif user_input == "5":
                print("Thank you for using our ATM!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_pin(self):
        if self.pin:
            print("PIN already exists. Please change it instead.")
            return

        user_pin = input("Enter a 4-digit PIN: ")
        if not user_pin.isdigit() or len(user_pin) != 4:
            print("PIN must contain exactly 4 digits.")
            return

        try:
            user_balance = float(input("Enter your initial balance: "))
            if user_balance < 0:
                print("Initial balance cannot be negative.")
                return
        except ValueError:
            print("Please enter a valid numeric balance.")
            return

        self.pin = user_pin
        self.balance = user_balance
        print("PIN created successfully!")

    def change_pin(self):
        if not self.pin:
            print("Please create a PIN first.")
            return

        old_pin = input("Enter your old PIN: ")
        if old_pin != self.pin:
            print("Incorrect PIN!")
            return

        new_pin = input("Enter your new 4-digit PIN: ")
        if not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must contain exactly 4 digits.")
            return

        self.pin = new_pin
        print("PIN changed successfully!")

    def check_balance(self):
        if not self.pin:
            print("Please create a PIN first.")
            return

        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            print(f"Your balance is: {self.balance:.2f}")
        else:
            print("Incorrect PIN!")

    def withdraw(self):
        if not self.pin:
            print("Please create a PIN first.")
            return

        entered_pin = input("Enter your PIN: ")
        if entered_pin != self.pin:
            print("Incorrect PIN!")
            return

        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Please enter a valid numeric amount.")
            return

        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawal successful!")
            print(f"Remaining balance: {self.balance:.2f}")


if __name__ == "__main__":
    sbi = Atm()
