#!/usr/bin/env python3.6
from user import User
from user import Account

#functions for User class

def create_user(firstname,lastname,username,password):
    '''
    function to create new user
    '''
    new_user = User(firstname,lastname,username,password)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    function to delete user
    '''
    user.delete_user()

def find_user(username):
    '''
    function to search for users by username
    '''
    return User.find_by_username(username)

def find_password(userpassword):
    '''
    function to search for users by passwords
    '''
    return User.find_by_userpassword(userpassword)

def display_user():
    '''
    function to display users
    '''
    return User.display_userInfo()

# functions for Account class

def create_account(accountname,accountusername,accountpassword):
    '''
    function to create account
    '''
    new_account = Account(accountname,accountusername,accountpassword)
    return new_account

def save_account(user):
    '''
    function to save account
    '''
    user.save_account()

def delete_account(user):
    '''
    function to delete account
    '''
    user.delete_account() 

def display_account_credentials():
    '''
    function to display account details
    '''
    return Account.display_accounts()

def find_account_credentials(accountname):
    '''
    function to search for accounts by name
    '''
    return Account.find_by_accountName(accountname)

def main():
    print("Welcome to Password Locker. What is your name?")
    name = input()
    print(f"Hello {name}! To start off please choose one of the options below:")
    print('\n')

    while True:
        print("Use these short-codes for: su - SignUp  or  lg - Login")
        user_choice = input().lower()




if __name__ == '__main__':
    main()