class wallet():

    '''
    This object controls the actual wallet features
    like adding money or removing money
    it also checks if the required files are available or not in case someone deletes it 

    
    '''


    def storage_checker():
        '''Checks if the following files are present or not:
        wallet -> keep track of current available funds
        withdrawEntries -> keep track of every time money was taken 
        depositEntries -> keep track of every time money was added
        '''
        import os
        if not os.path.exists('wallet'):
            wallet = open('wallet','w')
            wallet.write('0')
            wallet.close
        if not os.path.exists('withdrawEntries'):
            with open('withdrawEntries','w') as file:
                import csv
                wr = csv.writer(file)
                wr.writerow(['Amount','Venue','Purpose','Time','MEMO'])
        if not os.path.exists('depositEntries'):
            with open('depositEntries','w') as file:
                import csv
                wr = csv.writer(file)
                wr.writerow(['Amount','Source','Time','MEMO'])



    def fund_checker():
        '''Checks Current Available Funds'''
        with open('wallet') as wallet:
            balance = wallet.read()
        return balance


    def add_money(amount):
        
        with open('wallet') as wallet:
            balance = wallet.read()

        balance = int(balance) + int(amount)
        with open('wallet','w') as wallet:
            wallet.write(str(balance))



    def take_money(amount):
        with open('wallet') as wallet:
            balance = wallet.read()

        balance = int(balance) - int(amount)
        with open('wallet','w') as wallet:
            wallet.write(str(balance))



