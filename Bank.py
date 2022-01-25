import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

import Auth


def BankDeposit(username):
    bankData = pd.read_csv('users.csv')
    df = pd.DataFrame(bankData)
    index1 = df[df['username'] == username].index.values
    dict1 = df.set_index('username').to_dict(orient='index')

    selected_user = dict1.__getitem__(username)
    selected_user_balance = selected_user["balance"]
    change = input("Enter the amount you wanna deposit: ")
    change = int(change)

    print("Your old balance: ", selected_user_balance)

    selected_user_balance = selected_user_balance + change

    df.balance[index1] = selected_user_balance

    df.to_csv('users.csv', index=False)

    print("Your new balance: ", selected_user_balance)


def BankWithdraw(username):
    bankData = pd.read_csv('users.csv')
    df = pd.DataFrame(bankData)

    index1 = df[df['username'] == username].index.values

    dict1 = df.set_index('username').to_dict(orient='index')

    selected_user = dict1.__getitem__(username)
    selected_user_balance = selected_user["balance"]
    change = input("Enter the amount you wanna withdraw: ")
    change = int(change)
    if selected_user_balance <= 0 or selected_user_balance < change:
        print("There is not enough balance in your account !")

    else:
        print("Your old balance: ", selected_user_balance)
        selected_user_balance = selected_user_balance - change
        print("Your new balance: ", selected_user_balance)

        df.balance[index1] = selected_user_balance

        df.to_csv('users.csv', index=False)


def BankInfo(username):
    bankData = pd.read_csv('users.csv')
    df = pd.DataFrame(bankData)
    dict1 = df.set_index('username').to_dict(orient='index')

    selected_user = dict1.__getitem__(username)
    selected_user_balance = selected_user.__getitem__("balance")

    print("Your balance: ", selected_user_balance)


def DeleteUser(username):
    userData = pd.read_csv('users.csv')
    df1 = pd.DataFrame(userData)

    print(df1)

    print('\nSilmek istediğiniz kişi bilgisi giriniz')
    user = input('Username(for delete) : ')

    df1.drop(df1[df1['username'] == user].index, inplace=True)
    df1.to_csv('users.csv', index=False)


def BankTransfer(username):
    bankData = pd.read_csv('users.csv')
    df = pd.DataFrame(bankData)
    person = input("Enter the name of the person you want to transfer money to: ")
    matching_creds = (len(df[(df.username == person)]) > 0)
    if matching_creds:

        index1 = df[df['username'] == person].index.values
        index2 = df[df['username'] == username].index.values
        dict1 = df.set_index('username').to_dict(orient='index')

        selected_user1 = dict1.__getitem__(username)
        selected_user_balance1 = selected_user1["balance"]
        change = input("Enter the amount you wanna transfer: ")
        change = int(change)
        if selected_user_balance1 >= change:

            selected_user2 = dict1.__getitem__(person)
            selected_user_balance2 = selected_user2["balance"]

            selected_user_balance2 = selected_user_balance2 + change
            print("The money transfer was successful !")
            # print("Person new balance: ", selected_user_balance2)

            df.balance[index1] = selected_user_balance2

            selected_user_balance1 = selected_user_balance1 - change

            df.balance[index2] = selected_user_balance1

            df.to_csv('users.csv', index=False)

            print("Your new balance: ", selected_user_balance1)

        else:
            print("Insufficient balance for transfer '")

    else:
        print("There is no person with this username !")
