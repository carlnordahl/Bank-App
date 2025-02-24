from customer import Customer
from account import Account

class Bank():
    # class representing a bank
    def __init__(self):
        # create two empty key-value tables with customers and accounts
        # customers: keys: customer_id, value: Customer object
        # accounts: keys: account_nbr, value: Account object
        self.__customers = {}
        self.__accounts = {}

    def add_customer(self, name, personal_nbr):
        # check if personal number is already a customer
        for customer in self.__customers.values():
            if customer.get_personal_nbr() == personal_nbr:
                # customer with given personal number already exists
                return None
            
        # create a new customer_id. form: C10, C11, C12, ...
        customer_id = str('C' + str(10 + len(self.__customers)))
        customer = Customer(customer_id, personal_nbr, name)

        # add new pair to customers dictionary
        self.__customers.update({customer_id : customer})

        return customer_id
    
    def get_customer(self, customer_id):
        # return customer with specified customer_id, 
        # or None if customer doesn't exist
        return self.__customers.get(customer_id)
    
    def find_customer(self, name_part):
        # return list of Customer objects where name_part 
        # is included in the name string 
        customer_list = []

        for customer in self.__customers.values():
            if customer.get_name().lower().find(name_part) != -1:
                customer_list.append(customer)
        
        return customer_list
    
    def create_account(self, customer_id):
        # create an account for the customer with a specified customer id
        # return the account number or -1 if customer_id not registered
        if customer_id not in self.__customers:
            # customer id not registered in customers
            return -1
        
        # customers are allowed to have multiple account
        account_nbr = 1000 + len(self.__accounts)
        account = Account(customer_id, account_nbr)

        self.__accounts.update({account_nbr : account})

        return account_nbr
    
    def get_account(self, account_nbr):
        # return account with specified account number, otherwise None
        return self.__accounts.get(account_nbr)
    
    def remove_account(self, account_nbr):
        # only accounts with balance = 0 can be removed
        if account_nbr in self.__accounts and self.__accounts.get(account_nbr).get_balance() == 0:
            self.__accounts.pop(account_nbr)
            return True
        return False
    
    def transfer(self, from_acc_nbr, to_acc_nbr, amount):
        # check that amount is positive
        if amount <= 0:
            return False
        
        # check that both accounts exist:
        if from_acc_nbr not in self.__accounts or to_acc_nbr not in self.__accounts:
            # one or both accounts didn't exist
            return False
        
        if self.__accounts.get(from_acc_nbr).withdraw(amount):
            # money withdrawn
            self.__accounts.get(to_acc_nbr).deposit(amount)
            # tranfer successful
            return True
        
    def all_accounts(self):
        # get list of all registered accounts
        accounts = []
        for acc in self.__accounts.values():
            accounts.append(acc)
        return accounts
    
    def accounts_by_customer(self, customer_id):
        # return list with all accounts connected to specified customer id
        accounts = []
        for acc in self.__accounts.values():
            if acc.get_customer_id() == customer_id:
                accounts.append(acc)

        if len(accounts) == 0:
            # No account with specified customer id
            return None
        
        return accounts
    
    def all_customers_sorted_by_name(self):       
        # add all customers to a list
        customers = list(self.__customers.values())

        # sort the list by name using sorted() and lambda function
        customers_sorted = sorted(customers, key = lambda x : x.get_name())

        return customers_sorted
    
    # write bank information to text file
    def to_file(self, customers_filename, accounts_filename):
        with open(customers_filename, 'w') as f:
            for customer in self.__customers.values():
                f.write(f"{customer.get_customer_id()};{customer.get_personal_nbr()};{customer.get_name()}\n")

        with open(accounts_filename, 'w') as f:
            for account in self.__accounts.values():
                f.write(f"{account.get_account_nbr()};{account.get_customer_id()};{account.get_balance()}\n")
    
    # read bank information from text file
    def from_file(self, customers_filename, accounts_filename):
        # read customers
        with open(customers_filename, 'r') as f:
            for line in f:
                # separate line
                line = line.strip().split(sep=';')

                # read information
                customer_id = line[0]
                personal_nbr = line[1]
                name = line[2]

                # parse to customer object
                customer = Customer(customer_id, personal_nbr, name)
                
                # add to customer dictionary
                self.__customers.update({customer_id : customer})
        
        # read accounts
        with open(accounts_filename, 'r') as f:
            for line in f:
                # separate line
                line = line.strip().split(sep=';')

                # read information
                account_nbr = int(line[0])
                customer_id_ = line[1]
                balance = int(line[2])

                # Initiate account and deposit the balance
                account = Account(customer_id_, account_nbr)
                account.deposit(balance)

                # add to accounts dictionary
                self.__accounts.update({account_nbr : account})


