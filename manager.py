import managers_tools as manager


print('Welcome to Wallet Manager')
task = input('''
What would you like to do?
0.Balance
1.Deposit Money
2.Withdraw Money
3.Show Records
4.Delete Last Entry
    ''')


if task == '0':
    print(manager.balance())

elif task == '1':
    amount = input('''
How much money would you like to deposit?
    ''')
    place = input('''
What is the source of this money?    
    ''')
    extra_memo = input('''
Anything you would like to add?
''')
    manager.deposit_money(amount,place,extra_memo)
    
elif task == '2':
    amount = input('''
How much money would you like to withdraw?
    ''')
    purpose = input('''
What is the purpose for this money?
    ''')
    place = input('''
Where will this money be spend ie place?
    ''')
    extra_memo = input('''
Anything you would like to add?
    ''')
    manager.withdraw_money(amount,place,purpose,extra_memo)
    
elif task =='3':
    sub_task = input('''
From which entry?
1.Deposits
2.Withdraws
    ''')
    if sub_task == '1':
        print('\n\n',manager.showEntry('depositEntries'))
    elif sub_task == '2':
        print('\n\n',manager.showEntry('withdrawEntries'))
    print('Done!')
elif task =='4':
    sub_task = input('''
From which entry?
1.Deposits
2.Withdraws
    ''')
    if sub_task == '1':
        manager.delEntry('depositEntries')
    elif sub_task == '2':
        manager.delEntry('withdrawEntries')

else:
    print('No vaild input found!')