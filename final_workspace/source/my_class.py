"""
This file is for storing my class
so that my code will look a bit better
"""

import datetime

class Record:
    """
    Record class
    Attributes:
        amount (float): balance amount in an account
        date (str): date when the record was created, in `YYYY-MM-DD` format

    Methods:
        to_dict() -> dict:
            Converts the record data into a dictionary with 'date' and 'amount' as keys.
            Use when upload a data in a JSON format

        to_list() -> list:
            Converts the record data into a list containing 'date' and 'amount'.
            Use when uploading a data to Google Spreadsheet using Google API.
    """
    def __init__(self, amount: float) -> None:
        self.amount = amount
        self.date = str(datetime.date.today())

    def to_dict(self) -> dict:
        """
        Converts the record data into a dictionary format.

        Parameters:
            None

        Returns:
            dict: with keys 'date' and 'amount'.
        """
        record_dict = {
            'date': self.date,
            'amount': self.amount
        }
        return record_dict

    def to_list(self) -> list:
        """
        Converts the record data into a list format.

        Parameters:
            None

        Returns:
            list: list containing 'date' and 'amount'
        """
        record_list = [self.date, self.amount]
        return record_list

class Income(Record):
    """
    Income class, extending from Record class
    
    Attributes:
        amount (float): balance amount in an account (inherited from `Record`)
        date (str): date when the record was created (inherited from `Record`)
        sender (str): name of a person/account that sent the money
    
    Methods:
        to_dict() -> dict:
            Converts the record data into a dictionary with 'date', 'amount', and 'sender' as keys.
            Use when upload a data in a JSON format

        to_list() -> list:
            Converts the record data into a list containing 'date', 'amount', and 'sender'.
            Use when uploading a data to Google Spreadsheet using Google API.
    """
    def __init__(self, amount: float, sender: str) -> None:
        super().__init__(amount)
        self.sender = sender

    def to_dict(self) -> dict:
        """
        Converts the record data into a dictionary format.
        
        Parameters:
            None

        Returns:
            dict: with keys 'date', 'amount', and 'sender'.
        """
        record_dict = super().to_dict()
        record_dict.update({
            'sender': self.sender
        })
        return record_dict

    def to_list(self) -> list:
        """
        Converts the record data into a list format.

        Parameters:
            None

        Returns:
            list: list containing 'date', 'amount', and 'sender'.
        """
        record_list = super().to_list()
        record_list.append(self.sender)
        return record_list


class Expense(Record):
    """
    Expense class, extending from Record class
    
    Attributes:
        amount (float): balance amount in an account (inherited from `Record`)
        date (str): date when the record was created (inherited from `Record`)
        recipient (str): name of a person/account who receive the money
    
    Methods:
        to_dict() -> dict:
            Converts the record data into a dictionary with 'date', 'amount',\
and 'recipient' as keys.
            Use when upload a data in a JSON format

        to_list() -> list:
            Converts the record data into a list containing 'date', 'amount', and 'recipient'.
            Use when uploading a data to Google Spreadsheet using Google API.
    """
    def __init__(self, amount: float, recipient: str) -> None:
        super().__init__(amount)
        self.recipient = recipient

    def to_dict(self) -> dict:
        """
        Converts the record data into a list format.
        
        Parameters:
            None

        Returns:
            dict: dict with keys 'date', 'amount', and 'recipient'.

        """
        record_dict = super().to_dict()
        record_dict.update({
            'recipient': self.recipient
        })
        return record_dict

    def to_list(self) -> list:
        """
        Converts the record data into a list format.

        Parameters:
            None

        Returns:
            list: list containing 'date', 'amount', and 'recipient'.
        """
        record_list = super().to_list()
        record_list.append(self.recipient)
        return record_list


class Account:
    """
    Account class

    Attributes:
        name (str): account name
        category (str): category of an account (e.g., 'saving', 'business')
        balance (float): amount of balance in the account
        income_records (list): list of Income instances
        expense_records (list): list of Expense instances

    Methods:
        add_income_record(income: Income) -> None:
            Adds an income record to the income_records list and updates the balance.

        add_expense_record(expense: Expense) -> None:
            Adds an expense record to the expense_records list and updates the balance.

        display(index_: int) -> None:
            Displays the account's details including index_, name, category, and balance.

        to_dict() -> dict:
            Converts the account data to a dictionary format, including income and 
            expense records.

        to_list() -> list:
            Converts the account data to a nested list format, containing income 
            and expense records in separate lists.

    """

    def __init__(self, acc_name: str, acc_category: str) -> None:
        """
        Initilize an account instance

        Parameters:
            acc_name (str): an account name
            acc_category (str): an account category
        
        Returns:
            None
        """
        self.name = acc_name
        self.category = acc_category
        self.balance = 0
        self.income_records = []
        self.expense_records = []

    def add_income_record(self, income: Income) -> None:
        """
        Adding an income record to the income_records list.

        Parameters:
            income (Income): an instance of an Income class.
        
        Returns:
            None
        """
        self.income_records.append(income)
        self.balance += income.amount

    def add_expense_record(self, expense: Expense) -> None:
        """
        Adding an expense record to the expense_records list.

        Parameters:
            expense (Expense): an instanc of an Expense class.
        
        Returns:
            None
        """
        self.expense_records.append(expense)
        self.balance -= expense.amount

    def display(self, index_: int) -> None:
        """
        Displaying the account's details.

        Parameters:
            index_ (int): index of the account for displaying
        
        Returns:
            None
        """
        print(f"{index_ + 1}.{'':<2}{self.name:<15}"
                      f"{self.category:<15}{self.balance:<7}THB"
        )

    def to_dict(self) -> dict:
        """
        Converts the account data to a dictionary format.

        Parameters:
            None

        Returns:
            dict: a dictionary containing account details and lists of income 
            and expense records, with each record in dictionary format.
        """
        record_dict = {
            'name': self.name,
            'category': self.category,
            'balance': self.balance,
            'income_records': {f"record{index+1}": record.to_dict() \
                               for index, record in \
                               enumerate(self.income_records)},
            'expense_records': {f"record{index+1}": record.to_dict() \
                                for index, record in \
                                enumerate(self.expense_records)}
        }
        return record_dict

    def to_list(self) -> list:
        """
        Converts the account data to a list format.

        Parameters:
            None

        Returns:
            list: list 2 lists:
                1. income_records list
                2. expense_records list
        """

        inc_list = [['date', 'amount', 'sender']]
        exp_list = [['date', 'amount', 'recipient']]
        for inc_rec in self.income_records:
            inc_list.append(inc_rec.to_list())
        for exp_rec in self.expense_records:
            exp_list.append(exp_rec.to_list())

        return [inc_list, exp_list]

# End of file
