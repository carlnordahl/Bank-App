# text based application which lets a user do administrative bank work

from bank import Bank

# create bank object
bank = Bank()

# initiate bank from a file
bank.from_file('customers.txt', 'accounts.txt')


close_app = False

while not close_app:
    print("""
          Välj ett av följande alternativ:
            1. Skapa en ny kund
            2. Skapa ett nytt konto
            3. Ta bort konto
            4. Sätta in pengar
            5. Ta ut pengar
            6. Överför pengar
            7. Skriv ut alla konton
            8. Sök på kund på del av namn
            9. Skriv ut samtliga kunder (bokstavsordning) och dess konton
            10. Avsluta programmet
          """)
    choice = input()

    if choice == '1':
        # create a new customer
        # any name is allowed, but personal numbers must be unique
        print('Du har valt att skapa en ny kund')
        customer_name = input('Skriv in kundens namn ')
        personal_nbr = input('Skriv in kundens personnummer ')

        customer_id = bank.add_customer(customer_name, personal_nbr)
        
        if customer_id != None:
            # success
            print(f"Kunden tillagd med kundnummer {customer_id}")
        else:
            print(f"Kund med det personnumret finns redan")
    
    elif choice == '2':
        # create a new account
        print('Du har valt att skapa ett nytt konto')
        customer_id = input('Ange kundnummer för kunden som ska ha kontot ')

        account_nbr = bank.create_account(customer_id)

        if account_nbr != -1:
            #success
            print(f"Kontot skapades med kontonummer {account_nbr}")
        else:
            # fail
            print('Ingen kund med det kundnumret är registrerad')
    
    elif choice == '3':
        # remove account, don't remove customer
        # if account has money left it cannot be removed, but this is
        # handled by the Bank class
        print('Du har valt att ta bort ett konto')
        account_nbr = int(input('Ange kontonummer för kontot som ska tas bort '))

        if bank.remove_account(account_nbr) == True:
            # success
            print('Kontot togs bort')
        else:
            # fail
            print('Kontot kunde inte tas bort')
    
    elif choice == '4':
        print('Du har valt att sätta in pengar')
        account_nbr = int(input('Ange kontonummer '))
        amount = int(input('Ange belopp '))

        account = bank.get_account(account_nbr)
        if account == None:
            # account not found
            print('Kontot hittades inte')
        
        elif account.deposit(amount):
            # account found and balance sufficient
            print(f"Insättning lyckades, saldot på kontot är nu {account.get_balance()}")
        else:
            # balance not sufficient
            print('Insättning misslyckades, negativt belopp')
    
    elif choice == '5':
        print('Du har valt att ta ut pengar')
        account_nbr = int(input('Ange kontonummer '))
        amount = int(input('Ange belopp '))

        account = bank.get_account(account_nbr)

        if account == None:
            print('Kontot hittades inte')

        elif account.withdraw(amount):
            # success
            print(f"Uttag lyckades, saldot på kontot är nu {account.get_balance()}")
        else: 
            print(f"Uttag misslyckades, saldot på kontot är {account.get_balance()}")

    elif choice == '6':
        # transfer money between accounts
        print('Du har valt att överföra pengar')
        from_account_nbr = int(input('Ange kontonummer att överföra från '))
        to_account_nbr = int(input('Ange kontonummer att överföra till '))
        amount = int(input('Ange belopp '))

        if bank.transfer(from_account_nbr, to_account_nbr, amount):
            # success
            print('Överföring lyckades')
        
        else:
            # fail
            print('Överföring misslyckades')
    
    elif choice == '7':
        # print all accounts
        print('Du har valt att skriva ut alla konton')
        accounts = bank.all_accounts()

        if len(accounts) == 0:
            print('Inga konton hittades')
        
        else:
            for acc in accounts:
                print(acc)

    # left to implement: choice 8 and 9
    elif choice == '8':
        # search customers by part of name, case insensitive 
        print('Du har valt att söka på (del av) kundnamn')
        name_part = input('Skriv in (del av) kundnamn att söka på ').lower()
        
        customer_list = bank.find_customer(name_part)

        if len(customer_list) == 0:
            # no matches
            print('Inga kunder hittades')
        else:
            # print matches
            print('Följande kunder hittades: ')
            for customer in customer_list:
                print(customer)
    
    elif choice == '9':
        # print all customers and their accounts
        print('Du har valt att skriva ut alla kunder tillsammans med deras konton')
        
        # retrieve customers
        customers = bank.all_customers_sorted_by_name()

        if len(customers) == 0:
            print('Inga kunder hittades')
        else:   
            for customer in customers:
                print(customer)
                # get customer´s accounts and print them
                accounts = bank.accounts_by_customer(customer.get_customer_id())

                if accounts != None:
                    for i in range(len(accounts)):
                        print(f"\t{i}: {accounts[i]}")

    elif choice == '10':
        # close application
        print('Du har valt att avsluta programmet, välkommen tillbaka')
        # write customers to file
        bank.to_file('customers.txt', 'accounts.txt')

        close_app = True
        break

    else:
        # wrong option
        print('Felaktigt val, välj ett alternativ mellan 1 och 10')





        

