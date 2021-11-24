#A Programmer can Create His Own Exception is called User Define of Custom Exception
class BalanceException(Exception):
    pass
def checkbalance():
    money = 15000
    withdraw = 14000
    balance = money-withdraw
    if(balance<=3000):
        raise BalanceException('Insufficient Balance')
    print(balance)
try:
    checkbalance()
except BalanceException as be:
    print(be)