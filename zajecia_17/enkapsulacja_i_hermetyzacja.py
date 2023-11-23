class BankAccount:
    def __init__(self, user_pesel, amount_on_account):
        self.__user_pesel = user_pesel
        self._amount_on_account = amount_on_account

my_account = BankAccount(user_pesel="12345453453", amount_on_account=100.00)