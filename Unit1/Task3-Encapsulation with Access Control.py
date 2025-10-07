class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

# Example usage
if __name__ == "__main__":
    account = BankAccount(1000)
    
    # Deposit money
    account.deposit(500)
    print(f"Balance after deposit: ${account.get_balance()}")
    
    # Withdraw money
    if account.withdraw(200):
        print(f"Withdrawal successful. New balance: ${account.get_balance()}")
    else:
        print("Insufficient funds!")
    
    # Try to access private attribute (won't work directly)
    # This will not access the actual private attribute
    # print(account.__balance)  # This would raise an AttributeError