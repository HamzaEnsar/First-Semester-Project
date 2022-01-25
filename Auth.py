import pandas as pd


def authd_person(user, pasw):
    loop = True
    logged = False

    userData1 = pd.read_csv('Authorized.csv')

    df2 = pd.DataFrame(userData1)
    while loop:

        matching_creds1 = (len(df2[(df2.username == user) & (df2.password == pasw)]) > 0)
        if matching_creds1:
            loop = False
            logged = True

        else:
            loop = False
            logged = False

    return logged


def register():
    userData = pd.read_csv('users.csv')
    df1 = pd.DataFrame(userData)

    # print(df1)

    print('\nKayıt bilgileri giriniz')
    user = input('Username(register) : ')
    pasw = input('Password(register) : ')
    balance = "0"

    header = ['username', 'password', 'balance']
    data = [[user, pasw, balance]]
    data = pd.DataFrame(data, columns=header)

    df_merged = [df1, data]

    df1 = pd.concat(df_merged)
    df1.to_csv('users.csv', index=False)

    # print(data)
    # print(df1)


def login(user, pasw):
    loop = True
    logged = False
    userData = pd.read_csv('users.csv')
    userData1 = pd.read_csv('Authorized.csv')

    df = pd.DataFrame(userData)
    df2 = pd.DataFrame(userData1)
    while loop:

        matching_creds = (len(df[(df.username == user) & (df.password == pasw)]) > 0)
        matching_creds1 = (len(df2[(df2.username == user) & (df2.password == pasw)]) > 0)
        if matching_creds:
            print('Welocome:', user)
            loop = False
            logged = True
        elif matching_creds1:
            print('Welocome:', user)
            loop = False
            logged = True

        else:
            loop = False
            logged = False

    return logged
