class Account:
    def __init__(self, customer_id, account_nbr):
        self.__customer_id = customer_id
        self.__account_nbr = account_nbr
        self.__balance = 0
    
    # metodhs to get properties
    def get_customer_id(self):
        return self.__customer_id
    
    def get_account_nbr(self):
        return self.__account_nbr
    
    def get_balance(self):
        return self.__balance
    
    # deposit a positive sum to the account
    def deposit(self, amount):
        if amount < 0:
            return False
        else:
            self.__balance += amount
            return True
    
    # withdraw a positive sum from account
    def withdraw(self, amount):
        if amount < 0 or amount > self.__balance:
            return False
        else:
            self.__balance -= amount
            return True
    
    # string representation of account
    def __str__(self):
        return f"kontonummer: {self.__account_nbr}, saldo: {self.__balance} ({self.__customer_id})"
    