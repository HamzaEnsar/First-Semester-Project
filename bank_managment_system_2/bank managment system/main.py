import Auth
import Bank
import pandas as pd

print("----------------------")
print("BANK OF POLAND")
while True:
    print('Log In or Register')

    print("1: Log In: ")
    print("2: Register: ")
    option2 = input("Please choose an option: ")

    if option2 == "2":
        Auth.register()

    if option2 == "1":
        print('Log In')
        user = input('Username : ')
        pasw = input('Password : ')
        print("----------------------")

        loop = True
        while loop:

            if Auth.login(user, pasw) == True:
                print("1: Deposit money: ")
                print("2: Withdraw money: ")
                print("3: Show balance: ")
                print("4: Delete an account: ")
                print("5: Money transfer: ")
                print("6: Exit: ")

                option = input("Please choose an option ")
                print("----------------------")

                if option == "1":
                    Bank.BankDeposit(user)
                    loop = True
                    print("----------------------")


                elif option == "2":
                    Bank.BankWithdraw(user)
                    loop = True
                    print("----------------------")

                elif option == "3":
                    Bank.BankInfo(user)
                    loop = True
                    print("----------------------")

                elif option == "4":
                    if Auth.authd_person(user, pasw):
                        print("----------------------")
                        print("List of persons,You can delete by usernames !")
                        Bank.DeleteUser(user)
                        print("----------------------")
                    else:
                        print("----------------------")
                        print("You are not authorized for this action, please select another action !")
                        print("----------------------")
                elif option == "5":

                    Bank.BankTransfer(user)
                    print("----------------------")
                    loop = True

                elif option == "6":
                    print("Goodbye !", user)
                    loop = False
                    print("----------------------")


            else:
                print("----------------------")
                print("BANK OF POLAND")
                user = input('Username : ')
                pasw = input('Password : ')
                print("Login information is incorrect, please try again.")
                print("----------------------")
                loop = True
                print("----------------------")

    else:
        print("Goodbye !")
