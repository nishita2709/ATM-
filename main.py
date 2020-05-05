  class atm:


    def __init__(self, name):

        self.name = name



    def information(self):

        print("\n ACCOUNT DETAILS:")

        print("\nName:", name)

        print("Account Number:", info[name][0])

        print("Mobile Number:", info[name][1])

        print("Balance:", info[name][2])



    def pinchange(self):

        c = 3

        while True:

            x = int(input("\nEnter the PIN: "))

            y = int(input("Enter the PIN one more time: "))

            if x == y:

                print("PIN changed: ", x)

                info[name][3] = x

                break

            else:

                c = c - 1

                print("Sorry, PINS didin't matched.")
                print("Try again")

                if c == 0:
                    print("Blocked!!")
                else:
                    print(c, "attempts are remaining")

                continue



    def balance_info(self):

        print("Account Number is:", info[name][0])

        print("Account Balance is:", info[name][2])


    def deposit(self):

        a = int(input("\nEnter the Amount to be Deposited: "))

        info[name][2]+=a

        print("Amount is successfully deposited.")

        print("Balance of your account is: ", info[name][2])


    def withdraw(self):

        m = int(input("\nEnter the Amount to withdraw: "))

        n = info[name][2]

        if m > n:
            print("Balance is not sufficient.")

        else:

            info[name][2]-=m

            print("Your balance is: ", info[name][2])

        

info = {"john": [1802, 9821524471, 20000, 1201],
        "alex": [1954, 8674512997, 40000, 9654],
        "james": [3654, 7458214500, 60000, 4478],
        "chris": [4178, 9766444147, 80000, 2589],
        "robert":[6657, 8102457896, 30000, 1045]}

name = input("Enter name: ")

if name in info:

    m = atm(name)

    ch = 0

    i=3

    while ch < 3:

        p = int(input("Enter PIN: "))

        if p == info[name][3]:

            while True:

                a = int(input('''
1.Account Information
2.Change PIN
3.Balance Inquiry 
4.Withdraw 
5.Deposit 
6.EXIT 
Enter Your Choice: '''))

                if a == 1:

                    m.information()

                elif a == 2:

                    m.pinchange()

                elif a == 3:

                    m.balance_info()

                elif a == 4:

                    m.withdraw()

                elif a == 5:

                    m.deposit()

                elif a == 6:

                    print("Exit")

                    quit()

                else:

                    print("Wrong input,please select valid option")

        else:

            if ch == 3:

                print("Account Blocked!")

            else:

                print("Wrong pin entered, Enter Again")

                ch = ch + 1

else:

    print("Not Found")
