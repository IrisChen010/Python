class BankAccount:  
    def __init__(self, ID, PIN, checking, savings):
        self.ID = ID
        self.PIN = PIN
        self.checking = checking
        self.savings = savings

    def getID(self):
        return self.ID

    def getPIN(self):
        return self.PIN

    def getSavings(self):
        return self.savings

    def getChecking(self):
        return self.checking

    def withdraw(self, amount, type):  
        if (type == 1):
            if (self.savings < amount):
                return False
            else:  
                self.savings -= amount
        elif (type == 2):
            if (self.checking < amount):
                return False
            else:  
                self.checking -= amount
        return True

    def deposit(self, amount, type):
        if (type == 1):
            self.savings += amount
        elif (type == 2):
            self.checking += amount


def writeFile(filePath):
    while True:
        userid = input("Enter ID: ")
        userpin = input("Enter PIN: ")
        userChecking = input("Enter checking amount: ")
        userSaving = input("Enter saving amount: ")

        accoutList = []
        accoutList.append(userid)
        accoutList.append(userpin)
        accoutList.append(userChecking)
        accoutList.append(userSaving)
        accoutList.append("\n")

        writeFile = open(filePath, "a")
        writeFile.write('   '.join(accoutList))

        option = input("Do you want to enter more information? y or n: ")
        if (option == 'n'):
            break


def main():
    filePath = "/Users/fjyfly/Documents/LSI/Python/0430/write_file.txt"
    writeFile(filePath)
    account = []
    fileContent = []
    n = 0
    with open(filePath) as file: 
        for line in file: 
            li = line.split()  
            fileContent.append(li)
            account.append(
                BankAccount(li[0], li[1], float(li[2]), float(li[3])))
            n += 1 

    i = 0
    while i < n:
        userid = input("Please input ID: ")
        userpin = input("Please input PID: ")
        if (account[i].getID() == userid):
            if (account[i].getPIN() == userpin):
                option = int(
                    input(
                        'Enter: \n1 for withdraw \n2 for transfer \n3 for balance: '
                    ))
                if (option == 1):
                    type = int(
                        input('Select type \n1. Savings \n2.checking: '))
                    amount = float(input("Enter amount: "))
                    if (account[i].withdraw(amount, type)):
                        if (type == 1):
                            print(amount, 'withdrawn. Closing balance: ',
                                  account[i].getSavings())
                        else:
                            print(amount, 'withdrwan. Closing balance: ',
                                  account[i].getChecking())
                    else:
                        print('insufficient funds in your account')
                elif (option == 2):
                    option = int(
                        input(
                            'Enter: \n1 for within account transfer \n2 for other account: '
                        ))
                    if (option == 1):  
                        fromto = int(
                            input(
                                'Enter \n1. transfer from savings to checking \n2. transfer from checking to savings: '
                            ))
                        amount = float(input('Enter amount: '))
                        if (fromto == 1):
                            account[i].withdraw(amount, 1)
                            account[i].deposit(amount, 2)
                            print(
                                'Transfer successful from savings to checking')
                        else:
                            account[i].withdraw(amount, 2)
                            account[i].deposit(amount, 1)
                            print(
                                'Transfer successful from checking to savings')
                    else:  
                        accID = input('Enter account ID to transfer money: ')
                        j = 0
                        while j < n:
                            if (account[j].getID() == accID):
                                break
                            j += 1

                        if (j < n):
                            type = int(
                                input(
                                    'Select type: \n1. Savings \n2. Checking: '
                                ))
                            amount = float(input("enter amount: "))
                            account[i].withdraw(amount, type)
                            account[j].deposit(amount, type)
                            print('Transfer successful to account :',
                                  account[j].getID())
                            if (type == 1):
                                print(amount,
                                      'transferred. Your savings balance: ',
                                      account[i].getSavings())
                            else:
                                print(amount,
                                      'transferred. Your checking balance: ',
                                      account[i].getChecking())
                        else:
                            print(
                                'Invalid account ID. Transfer of funds terminated.'
                            )

                else:
                    type = int(
                        input('Select type: \n1. Savings \n2. Checking: '))
                    if (type == 1):
                        print('Your savings balance:', account[i].getSavings())
                    else:
                        print('Your checking balance:',
                              account[i].getChecking())

        i += 1

    if (i == n):  
        print('invalid login')
    else:  
        file = open(filePath, 'w')
        j = 0
        while j < n:
            file.write(account[j].getID() + ' ' + account[j].getPIN() + ' ' +
                       str(account[j].getChecking()) + ' ' +
                       str(account[j].getSavings()) + '\n')
            j += 1
    file.close()
    print('Thank you!!')

main()