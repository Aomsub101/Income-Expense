"""
Income and Expense management

Functions:
    1. account_manager() -> None
    2. category_manager() -> None
    3. add_record() -> None
    4. display_all() -> None
    5. transaction_manager() -> None
    6. load_data(json_data: dict) -> None
"""

# libraries
import os
import json
import pandas
from my_class import Account, Income, Expense
from spreadsheetAPI.sheet_management import GoogleSheet

# create a googlesheet instance
gg = GoogleSheet()

# working directory
DIR = r'G:\\My Drive\\Python2Project\\final_workspace'
os.chdir(DIR)

# for clearing the screen
CLEAR = 'cls'

# categories
categories = ['food', 'rent', 'transportation']

# username
USERNAME = ''

# for firstimer
FIRST_TIME = True

# accouts stuff
accounts = []
account_name = []

# account file path
ACCOUNT_FILE_PATH = r'database\\account.json'

def account_manager() -> None:
    """
    Managing user accounts:
        1. create a new account
        2. delete an existing account

    Parameters:
        None
    
    Returns:
        None
    """
    os.system(CLEAR)

    if FIRST_TIME:
        tmp_choice = '1'
    else:
        print('Welcome to account manager!\n')
        print('''Do you want to:
                1. Create a new account
                2. Delete an existing account
                3. Nothing and leave''')
        tmp_choice = input('\nSelect your choice: ')
        while tmp_choice not in ['1', '2', '3']:
            print('Invalid choice. Please try again.\n')
            tmp_choice = input('Select your choice: ')

    if tmp_choice == '1':
        os.system(CLEAR)

        print('Create an account!!\n')
        # Create account process
        while True:
            name_ = input("Account name: ").strip()
            if name_ == '':
                print('Invalid name. Please enter something.\n')
            elif name_ in account_name:
                print('This account already exists. Please use other name.\n')
            else:
                break
        account_name.append(name_)
        print('Your available categories:')
        for index_, category_ in enumerate(categories):
            print(f'{index_ + 1}.  {category_}')
        while True:
            try:
                category_number = int(
                    input("Select category number: ").strip()
                )

                if category_number > len(categories) or category_number <= 0:
                    print('Invalid choice. Please enter an existing categories.\n')
                else:
                    break
            except ValueError:
                print('Invalid choice. Please enter a number.\n')

        category_name = categories[category_number - 1]
        print(f'Account {name_} for {category_name} created!\n')
        category_ = categories[category_number - 1]
        new_account = Account(acc_name=name_, acc_category=category_)
        accounts.append(new_account)
    elif tmp_choice == '2':
        os.system(CLEAR)
        if not account_name:
            print('\nCannot delete. Due to no account!!')
            print('Go create an account first.\n')
            input('__Press enter to continue__')
            os.system(CLEAR)
            return
        print('Delete an account!!\n')

        # Create account process
        print('Here is your account:')
        print(f'{'':<4}name{'':<11}category{'':<7}balance')
        for index_, account_ in enumerate(accounts):
            account_.display(index_)

        while True:
            try:
                account_number = int(
                    input('Select account number you want to delete: ')
                )
                if account_number > len(accounts) or account_number <= 0:
                    print('Invalid choice. Please try again.\n')
                else:
                    break
            except ValueError:
                print('Invalid choice. Please enter a number.\n')
        print('Account deleted!\n')
        accounts.pop(account_number - 1)
        account_name.pop(account_number - 1)


def category_manager() -> None:
    """
    Managing categories:
        1. create a new category
        2. delete an existing category

    Parameters:
        None
    
    Returns:
        None
    """
    os.system(CLEAR)

    print('Welcome to category manager!\n')
    print('''Do you want to:
            1. Add a new category
            2. Delete an existing category
            3. Nothing and leave''')
    tmp_choice = input('\nSelect your choice: ')
    while tmp_choice not in ['1', '2', '3']:
        print('Invalid choice. Please try again.\n')
        tmp_choice = input('Select your choice: ')

    if tmp_choice == '1':
        os.system(CLEAR)

        print('Adding category!!!\n')
        while True:
            print('Current categories:')
            for index_, category_ in enumerate(categories):
                print(f'{index_ + 1}.  {category_}')

            new_category = input('\nCategory you want to add: ')
            while True:
                if new_category == '':
                    print('Invalid name. Please enter something.\n')
                    new_category = input(
                        '\nCategory you want to add: '
                    ).strip().lower()
                elif new_category in categories:
                    print('Invalid name. Category already exist.\n')
                    new_category = input(
                        '\nCategory you want to add: '
                    ).strip().lower()
                else:
                    break

            categories.append(new_category)
            print(f'Category {new_category} added!\n')

            print('Add more? (Y)es/(N)o')
            tmp_choice = input('Select your choice: ').strip().lower()
            while tmp_choice not in ['y', 'n']:
                print('\nInvalid choice. Please try again\n')
                print('Add more? (Y)es/(N)o')
                tmp_choice = input('Select your choice: ').strip().lower()

            if tmp_choice == 'n':
                break
    elif tmp_choice == '2':
        os.system(CLEAR)

        if not categories:
            print('\nCannot proceed due to no category.')
            print('Add a new categories and try again.')
            input('\n__Press enter to continue__')
            return

        print('Delete a category!!\n')
        print('Your categories:')
        pos = 1
        for index_, category in enumerate(categories):
            print(f'{index_ + 1}.  {category}')
            pos += 1
        print(f'{pos}.  Don\'t want to delete it now.')
        while True:
            try:
                category_number = int(
                    input('Select category number you want to delete: ')
                )
                if category_number > len(categories) + 1 or category_number <= 0:
                    print('Invalid choice. Please try again.\n')
                else:
                    break
            except ValueError:
                print('Invalid choice. Please enter a number.\n')

        if category_number == len(categories) + 1:
            return

        print('Category deleted!\n')
        categories.pop(category_number - 1)


def add_record() -> None:
    """
    Adding a record to an account

    Record type:
        1. Income record
        2. Expense record
    
    Parameters:
        None
    
    Returns:
        None
    """
    # to see if user cancle the process
    cancle = False

    # Body
    while True:
        os.system(CLEAR)

        print('Add record!!')
        print('''
                1. Income Record
                2. Expense Record
                3. Do nothing
            ''')
        tmp_choice = input('Select choice number: ').strip()
        while tmp_choice not in ['1', '2', '3']:
            print('\nInvalid Choice. Please try again')
            tmp_choice = input('Select choice number: ').strip()

        if tmp_choice == '3':
            print('Do nothing\n')
            break

        # Show all the account we have
        print(f'You have {len(accounts)} account(s).\n')
        print(f'{'':<4}name{'':<11}category{'':<7}balance')
        for index_, account_ in enumerate(accounts):
            account_.display(index_)

        # Let user select the account
        record_name = 'income' if tmp_choice == '1' else 'expense'
        print(f'\nSelect account number you want to add {record_name} record.')

        while True:
            try:
                account_number = int(input('Account number: '))
                if account_number > len(accounts) or account_number <= 0:
                    print('Invalid choice. Please enter an existing number\n')
                else:
                    break
            except ValueError:
                print('Invalid choice. Please enter a number\n')

        if tmp_choice == '1':
            print(f'\nAccount {account_name[account_number - 1]} selected.')
            name_ = input('Sender name: ')
            while name_ == '':
                print('Invalid name. Please enter something.\n')
                name_ = input('Sender name: ')

            while True:
                try:
                    amount_ = float(input('Amount of money: '))
                    if amount_ <= 0:
                        print('Invalid amount. Please enter positive amount.\n')
                    else:
                        break
                except ValueError:
                    print('Invalid amount. Please enter positive amount.\n')

            income_instance = Income(amount=amount_, sender=name_)
            accounts[account_number - 1].add_income_record(income_instance)
        elif tmp_choice == '2':
            name_ = input('Recievepant name: ')
            while name_ == '':
                print('Invalid name. Please enter something.\n')
                name_ = input('Recievepant name: ')

            while True:
                try:
                    amount_ = float(input('Amount of money: '))
                    if amount_ <= 0:
                        print('Invalid amount. Please enter positive amount.\n')
                    elif amount_ > accounts[account_number - 1].balance:
                        print('\nYou need more money!!')
                        print('Do you want to add more money? (Y)es/(N)o')
                        choice_ = input('Select your choice: ').strip().lower()
                        while choice_ not in ['y', 'n']:
                            print('Invalid choice. Please try again\n')
                            choice_ = input('Select your choice: ')\
                            .strip().lower()

                        if choice_ == 'y':
                            require_money = amount_ -\
                                accounts[account_number - 1].balance
                            print(f'\nYou will need {require_money}THB')
                            print('Please repeat the process after this.\n')
                            input('__Press enter to do a transaction__')
                            transaction_manager()
                            cancle = True
                            break

                        if choice_ == 'n':
                            cancle = True
                            break
                    else:
                        break
                except ValueError:
                    print('Invalid amount. Please enter a positive number\n')

            if not cancle:
                expense_instance = Expense(amount=amount_,
                                           recipient=name_
                )
                accounts[account_number - 1].\
                    add_expense_record(expense_instance)

        if cancle:
            cancle = False
            break

        print('Income record added!'\
                if tmp_choice == '1' else 'Expense record added!')

        tmp_choice = input('Add more record? (Y)es/(N)o: ').strip().lower()
        while tmp_choice not in ['y', 'n']:
            print('Invalid choice. Please try again.\n')
            tmp_choice = input('Add more record? (Y)es/(N)o: ').strip().lower()

        # stop adding
        if tmp_choice == 'n':
            break


def display_all() -> None:
    """
    Displaying all accounts and categories user has.

    Parameters:
        None
    
    Returns:
        None
    """
    os.system(CLEAR)
    print('All accounts:')
    print(f'{'':<4}name{'':<11}category{'':<7}balance')
    for index_, account_ in enumerate(accounts):
        account_.display(index_)

    print('\nAll categories:')
    print(f'{'':<4}category_name')
    for index_, category_ in enumerate(categories):
        print(f'{index_ + 1}.  {category_}')


def transaction_manager() -> None:
    """
    Managing all the transactions:
        1. Deposit
        2. Move money between account
        3. Withdraw the money
    
    Notes:
        1. Sender name for deposit option is username
        2. Recipient name for withdraw option is username
    
    Parameters:
        None
    
    Returns:
        None
    """
    if not account_name:
        print('\nCannot preceed dut to no account!')
        print('You need atleast 1 account.')
        input('\n__Press enter to create an account__')
        account_manager()
        return

    has_money = False
    for account_ in accounts:
        if account_.balance > 0:
            has_money = True
            break

    while True:
        os.system(CLEAR)

        print('Welcome to transaction manager!!\n')
        print('''Do you want to:
                1. Deposit
                2. Move money between account
                3. Withdraw
                4. Nothing and leave
        ''')
        transaction_type = input('\nSelect your choice: ').strip()
        while transaction_type not in ['1', '2', '3', '4']:
            print('Invalid choice. Please try again\n')
            transaction_type = input('Select your choice: ').strip()

        if transaction_type == '1':
            has_money = True
            print(f'{'':<4}name{'':<11}category{'':<7}balance')
            for index_, account_ in enumerate(accounts):
                account_.display(index_)

            print('\nWhich account you want to move the money to?')
            while True:
                try:
                    recieve_account_number = int(input('Select account: ').strip())
                    if recieve_account_number > len(accounts):
                        print('Invalid choice. Please select an existing account.\n')
                    else:
                        break
                except ValueError:
                    print('Invalid choice. Please enter an account number\n')

            while True:
                try:
                    amount_ = float(input('How much?: '))
                    if amount_ <= 0:
                        print('Invalid amount. Please enter positive amount\n')
                    break
                except ValueError:
                    print('Invalid amount. Please enter positive amount\n')

            print('Money added!!\n')
            print(f'From: {USERNAME}.')
            print(f'To: {accounts[recieve_account_number - 1].name} account.')

            income_instance = Income(
                sender=USERNAME,
                amount=amount_
            )
            accounts[recieve_account_number - 1].\
                add_income_record(income_instance)
        elif transaction_type == '2':
            if not has_money:
                print('Cannot proceed. You have to deposit the money first.\n')
                input('\n__Press enter to repeat the process__')
                continue

            if len(account_name) == 1:
                print('\nCannot proceed. You have only 1 account.\n')
                input('\n__Press enter to repeat the process__')
                continue

            print(f'{'':<4}name{'':<11}category{'':<7}balance')
            for index_, account_ in enumerate(accounts):
                account_.display(index_)

            print('\nWhich account you want to move the money from?')
            while True:
                try:
                    sender_account_number = int(
                        input('Select account: ').strip()
                    )
                    if sender_account_number > len(accounts):
                        print('Invalid choice. Please select an existing account.\n')
                    elif accounts[sender_account_number - 1].balance == 0:
                        print('Cannot select this account due to no money\n')
                    else:
                        break
                except ValueError:
                    print('Invalid choice. Please enter an account number\n')

            name = accounts[sender_account_number - 1].name
            account_balance = accounts[sender_account_number - 1].balance
            print(f'{name} has {account_balance} THB')

            print('\nWhich account you want to move the money to?')
            while True:
                try:
                    recieve_account_number = int(
                        input('Select account: ').strip()
                    )
                    if recieve_account_number > len(accounts):
                        print('Invalid choice. Please select an existing account.\n')
                    elif recieve_account_number == sender_account_number:
                        print('Cannot move the money to the same account.\n')
                    else:
                        break
                except ValueError:
                    print('Invalid choice. Please enter an account number\n')

            print(f'From: {accounts[sender_account_number - 1].name} account.')
            print(f'To: {accounts[recieve_account_number - 1].name} account.')

            while True:
                try:
                    amount_ = float(input('How much?: '))
                    if amount_ <= 0:
                        print('Invalid amount. Please enter a positive amount\n')
                    elif amount_ > accounts[sender_account_number - 1].balance:
                        print('Invalid amount. You dont have that much money.\n')
                    else:
                        break
                except ValueError:
                    print('Invalid amount. Please enter a positive number\n')

            income_instance = Income(
                sender=accounts[sender_account_number - 1].name,
                amount=amount_
            )
            expense_instance = Expense(
                recipient=accounts[recieve_account_number - 1].name,
                amount=amount_
            )
            accounts[recieve_account_number - 1].\
                add_income_record(income_instance)
            accounts[sender_account_number - 1].\
                add_expense_record(expense_instance)
        elif transaction_type == '3':
            if not has_money:
                print('Have no money in the account!\n')
                print('Please deposit the money then come back\n')
                input('__Press enter to continue__')
                continue

            print(f'{'':<4}name{'':<11}category{'':<7}balance')
            for index_, account_ in enumerate(accounts):
                account_.display(index_)

            print('\nWhich account you want to move the money from?')
            while True:
                try:
                    sender_account_number = int(
                        input('Select account: ').strip()
                    )
                    if sender_account_number > len(accounts):
                        print('Invalid choice. Please select an existing account.\n')
                    elif accounts[sender_account_number - 1].balance == 0:
                        print('Cannot select this account due to no money')
                    else:
                        break
                except ValueError:
                    print('Invalid choice. Please enter an account number\n')

            print(f'From: {accounts[sender_account_number - 1].name} account.')
            print(f'To: {USERNAME}.')

            while True:
                try:
                    amount_ = float(input('How much?: '))
                    if amount_ <= 0:
                        print('Invalid amount. Please enter a positive amount\n')
                    elif amount_ > accounts[sender_account_number - 1].balance:
                        print('Invalid amount. You dont have that much money.\n')
                    else:
                        break
                except ValueError:
                    print('Invalid amount. Please enter a positive number\n')

            expense_instance = Expense(
                recipient=USERNAME,
                amount=amount_
            )
            accounts[sender_account_number - 1].\
                add_expense_record(expense_instance)
        elif transaction_type == '4':
            print('Ok then. C ya.\n')
            break

        print('\nDo you want to do another transaction? (Y)es/(N)o')
        tmp_choice = input('Select your choice: ').strip().lower()
        while tmp_choice not in ['y', 'n']:
            print('Invalid choice. Please try again.\n')
            tmp_choice = input('Select your choice: ').strip().lower()

        if tmp_choice == 'n':
            print()
            break


def load_data(json_data: dict) -> None:
    """
    Loading data from a .json file and store that data in both:
        1. Income instances for income list
        2. Expense instances for expense list
    
    Parameters:
        json_data (dict): account data in json format
    
    Returns:
        None
    """
    global USERNAME # pylint: disable=W0603
    USERNAME = json_data['USERNAME']
    tmp_accounts = []

    for data in json_data['accounts'].values():
        tmp_account = Account(data['name'], data['category'])
        tmp_account.balance = data['balance']

        for income_data in data['income_records'].values():
            income = Income(income_data['amount'], income_data['sender'])
            income.date = income_data['date']
            tmp_account.add_income_record(income)

        for expense_data in data['expense_records'].values():
            expense = Expense(expense_data['amount'], expense_data['recipient'])
            expense.date = expense_data['date']
            tmp_account.add_expense_record(expense)
        tmp_accounts.append(tmp_account)

    return tmp_accounts

# *************************  GAMEPLAY PART  *************************

os.system(CLEAR)

if not os.path.exists(ACCOUNT_FILE_PATH):
    print('\nHi!! It\'s look like your first time here!')
    input()
    print('Welcome to the income and expense record app!')
    input()
    print('Let\'s start by creating your account!')
    print('But before we start, may I know your name first?')

    USERNAME = input('Your name: ')
    while USERNAME == '':
        print('Mr. \" \"? Don\'t be shy. Tell me your name~~ \n')
        USERNAME = input("Your name: ")
    print(f'\nHi! {USERNAME}. Let\'s start for real this time!\n')

    # creating the first account before we start
    input('__Press enter to create your first account!!__')
    account_manager()
    input('\n__Press enter to continue!__')

    os.system(CLEAR)

    FIRST_TIME = False

    print("Let's start a record journey!")
else:
    FIRST_TIME = False

    ACCOUNT_PATH = r'database\\account.json'
    ACCOUNT_NAME_PATH = r'database\\account_name.json'
    CATEGORY_PATH = r'database\\category.json'

    with open(ACCOUNT_PATH, 'r',
            encoding='utf-8') as account_file:
        account_file_data = json.load(account_file)
        accounts = load_data(account_file_data)

    with open(ACCOUNT_NAME_PATH, 'r',
            encoding='utf-8') as account_name_file:
        account_name_data = json.load(account_name_file)
        account_name = account_name_data['account_name']

    with open(CATEGORY_PATH, 'r',
            encoding='utf-8') as category_file:
        category_data = json.load(category_file)
        categories = category_data['categories']

    os.system(CLEAR)
    print('Let\'s continue where you left off!!\n')

while True:
    print("""What do you want to do?
                (1)Create/Delete account
                (2)Add/Delete new category
                (3)Move/Deposit/Withdraw money
                (4)Add new record to your account
                (5)Leave and save the data
                (6)Display all accounts and categories
        """)
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        account_manager()
        print('Process done.\n')
        input('__Press enter to continue__')
        os.system(CLEAR)

    elif choice  == '2':
        category_manager()
        print('Process done.\n')
        input('__Press enter to continue__')
        os.system(CLEAR)

    elif choice == '3':
        transaction_manager()
        print('Process done.\n')
        input('__Press enter to continue__')
        os.system(CLEAR)

    elif choice == '4':
        add_record()
        print('Process done.\n')
        input('__Press enter to continue__')
        os.system(CLEAR)

    elif choice == '5':
        accounts_dict = {
            'USERNAME': USERNAME,
            'accounts':{
                f"Account{index + 1}": account.to_dict() \
                    for index, account in enumerate(accounts)}
        }
        with open(r'database\\account.json', 'w',
                encoding='utf-8') as account_file:
            json.dump(accounts_dict, account_file, indent=4)

        categories_dict = {
            'categories': categories
        }

        with open(r'database\\category.json', 'w',
                encoding='utf-8') as category_file:
            json.dump(categories_dict, category_file, indent=4)

        account_name_dict = {
            'USERNAME': USERNAME,
            'account_name': account_name
        }

        with open(r'database\\account_name.json', 'w',
                encoding='utf-8') as category_file:
            json.dump(account_name_dict, category_file, indent=4)
        break
    elif choice == '6':
        display_all()
        input('\n__Press enter to continue__')
        os.system(CLEAR)
    else:
        os.system(CLEAR)
        print("Invalid choice. Please try again\n")

# save data in dataframe format
income_dict = []
expense_dict = []

# delete an old sheet
gg.delete_sheet()

for index, account in enumerate(accounts):
    for income_record in account.income_records:
        income_dict.append(income_record.to_dict())

    for expense_record in account.expense_records:
        expense_dict.append(expense_record.to_dict())

    # file name
    inc_file_path = f'database\\income_acc_{index + 1}.csv'
    exp_file_path = f'database\\expense_acc_{index + 1}.csv'

    # To csv
    income_df = pandas.DataFrame(income_dict)
    income_df.to_csv(inc_file_path, index=False)
    expense_df = pandas.DataFrame(expense_dict)
    expense_df.to_csv(exp_file_path, index=False)

    # Upload csv file to google sheet
    sheet_name = account.name
    gg.upload_to_sheet(csv_file_path=inc_file_path,
                                g_sheet_name=sheet_name + '_inc'
    )
    gg.upload_to_sheet(csv_file_path=exp_file_path,
                                g_sheet_name=sheet_name + '_exp'
    )

    os.remove(inc_file_path)
    os.remove(exp_file_path)

    # reset value
    income_dict = []
    expense_dict = []

os.system(CLEAR)
print("Data saved")
print('Good bye!')

# End of file
