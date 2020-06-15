customertransaction = []
customerNames = []
customerPins = []
customerBalances = []
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 0
i = 0

# This statement below allows the program to run continuously.
while True:
    import datetime

    date = datetime.datetime.now()
    print(" ----Welcome to PyBank GIIS----       ")
    print("--------------------------------------")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance & transactions >>=")
    print("=<< 5. close account              >>=")
    print("=<< 6. exit/quit app             >>=")
    print("=<< 7. send money to another account >>=")
    print("--------------------------------------")
    # below statement takes the choice input from user.
    choiceNumber = input("Select your choice number from the above menu : ")
    if choiceNumber == "1":
        print("Choice number 1 is selected by the customer")
        #line below will take the no: of customers from user.
        NOC = eval(input("Number of Customers : "))

        i = i + NOC
        # if condition will restrict the number of new account to 5.
        if i > 5:
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i = i - NOC
        else:
            # The while loop will run to the no: of customers.
            while counter_1 <= i:
                # These few lines will take information from customer and then append them to list.
                name = input("Input Fullname : ")
                customerNames.append(name)
                pin = str(input("Please input a pin of your choice : "))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("Please input a value to deposit to start an account : "))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print("Pin=", end=" ")
                print(customerPins[counter_2])
                print("Balance=", end=" ")
                print(customerBalances[counter_2], end=" ")
                print("$")
                customertransaction.extend([date, name, "+", deposition])
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("----New account created successfully !----")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(customerNames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")
                # statement below allows user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "2":
        j = 0
        print("Choice number 2 is selected by the customer")
        # while loop will prevent the user using the account if the username or pin is wrong.
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            # while loop will keep the function running when variable k is smaller than length of the
            # customerNames list.
            while k < len(customerNames) - 1:
                k = k + 1
                # These two if conditions find whether both the name and pin matches.
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        # These statement would show the balance taken from the list.
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("$")
                        balance = (customerBalances[k])
                        # Statement below would take the amount to withdraw from user.
                        withdrawal = eval(input("Input value to Withdraw : "))
                        # if condition below would look whether the withdraw is greater than balance.
                        if withdrawal > balance and withdrawal < 10000:
                            # statement below would take a deposition from the customer.
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            # These statements would update the value and show the balance to user.
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("$")
                            balance = balance - withdrawal
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("$")
                        elif withdrawal < balance and withdrawal < 10000:
                            # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount.
                            balance = balance - withdrawal
                            customertransaction.extend([date, name, "-", withdrawal])
                            # These statement would update the values in the list and show it to the customer.
                            print("\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("$\n\n")
                        else:
                            print("withdrwal invalid,exceed bank limit!")
                            break
            if j < 1:
                # if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
            # statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "3":
        print("Choice number 3 is selected by the customer")
        n = 0
        # while loop below would work when the pin or the username is wrong.
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            # The while loop below will keep function running to find the correct user.
            while k < len(customerNames) - 1:
                k = k + 1
                # The two if conditions below find whether both the pin and the name is correct.
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        # These statements would show the customer balance and update list values according to
                        # the deposition made.
                        print("Your Current Balance: ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("$")
                        balance = (customerBalances[k])
                        # This statement below takes the depositionn from the customer.
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        customertransaction.extend([date, name, "+", deposition])
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("$\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
            # statement allows the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "4":
        print("Choice number 4 is selected by the customer")
        print(customertransaction)
        for items in customertransaction:
            print(items, end="")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        # while loop below will keeping running until all the customers and balances are shown.
        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print("$")
            print("\n")
            k = k + 1
            # statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choiceNumber == "5":
        j = 0
        print("Choice number 5 is selected by the customer")
        # while loop will prevent the user using the account if the username or pin is wrong.
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            # while loop will keep the function running when variable k is smaller than length of the
            # customerNames list.
            while k < len(customerNames) - 1:
                k = k + 1
                # These two if conditions find where both the name and pin matches.
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        # These few statement would show the balance taken from the list.
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("$")
                        balance = (customerBalances[k])
        print("deleting account...")
        customerNames.remove(name)
        customerPins.remove(pin)
        customerBalances.remove(balance)
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "6":
        print("Choice number 6 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print("Bye bye")
        break
    elif choiceNumber == "7":
        send = 0
        print("Choice number 7 is selected by the customer")
        j = 0
        # This while loop will prevent the user using the account if the username or pin is wrong.
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            # This while loop will keep the function running when variable k is smaller than length of the
            # customerNames list.
            while k < len(customerNames) - 1:
                k = k + 1
                # These two if conditions find where both the name and pin matches.
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        # These few statement would show balance taken from the list.
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("$")
                        balance = (customerBalances[k])
                        # Statement below would take the amount to withdraw from user.
                        send = eval(input("Input value to send: "))
                        # The if condition below would look whether the withdraw is greater than the balance.
                        if send > balance:
                            # This statement below would take a deposition from the customer.
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            # These few statements would update the value and show the balance to user.
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("$")
                            balance = balance - send
                            print("-\n")
                            print("----money has been sent to bank Successfull!,please wait----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("$")
                        else:
                            # Else condition mentioned is to do withdrawal if the balance is greater than the
                            # withdraw amount.
                            balance = balance - send
                            customertransaction.extend([date, name, "-", send])
                            # These few statement would update the values in the list and show it to the customer.
                            print("\n")
                            print("----money has been sent to bank Successfull!,please wait----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("$")
                            # while loop below would work when the pin or the username is wrong.
                    n = 0
                    # while loop would work when the pin or the username is wrong.
                    while n < 1:
                        k = -1
                        name = input("Please input name you want to send money to: ")
                        # while loop will keep the function running to find the correct user.
                        while k < len(customerNames) - 1:
                            k = k + 1
                            # The two if conditions below would find whether both the pin and the name is correct.
                            if name == customerNames[k]:
                                n = n + 1
                                # These statements below would show the customer balance and update list values according to
                                # the deposition made.
                                balance = (customerBalances[k])
                                balance = balance + send
                                customerBalances[k] = balance
                                customertransaction.extend([date, name, "+", send])
                                print("\n")
                                print("----money has been sent successful!----")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
            # statement below helps the user to go back to the start of the program (main menu).
        if j < 1:
            # if condition above would work when the pin or the name is wrong.
            print("Your name and pin does not match!\n")
            break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    else:
        # else function above works when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # statement helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
