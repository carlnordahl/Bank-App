class Customer:
    # class representing a customer to the bank
    # __ denotes private properties
    def __init__(self, customer_id, personal_nbr, name):
        self.__customer_id = customer_id
        self.__personal_nbr = personal_nbr
        self.name = name
    
    # get customer id and personal number and name
    def get_customer_id(self):
        return self.__customer_id
    
    def get_personal_nbr(self):
        return self.__personal_nbr
    
    def get_name(self):
        return self.name
    
    # string representation of customer
    def __str__(self):
        return f"Kund: {self.__customer_id} Namn (personnummer): {self.name} ({self.__personal_nbr})"

