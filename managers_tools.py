
import csv 
import time
from wallet import *





def withdraw_money(amount,place,purpose,extra_memo,time=time.asctime(time.localtime())):
    global wallet
    wallet.storage_checker()
    wallet.take_money(amount)
    with open('withdrawEntries','a') as file:
        wr = csv.writer(file)
        wr.writerow([amount,place,purpose,time,extra_memo])
    print('Withdraw Record stored!')



def deposit_money(amount,place,extra_memo,time=time.asctime(time.localtime())):
    global wallet
    wallet.storage_checker()
    wallet.add_money(amount)
    with open('depositEntries','a') as depositentry:
        wr = csv.writer(depositentry)
        wr.writerow([amount,place,time,extra_memo])
    print('Deposit Record stored!')


def showEntry(file,lm=10):
    import pandas as pd
    en = pd.read_csv(file)
    return en.tail(lm)


def delEntry(file,lm=1):
    with open(file,'r+') as file:
        lines = file.readlines()
        for i in range(lm):
            lines.pop()
        file.writelines(lines) 
    print('Record removed')


def balance():
    global wallet
    return wallet.fund_checker()