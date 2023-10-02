class BalanceAndPin:
    __balance = 0
    __pin = 7899

    @classmethod
    def get_balance(cls):
        return BalanceAndPin.__balance

    @classmethod
    def set_balance(cls, balance):
        BalanceAndPin.__balance = balance

    @classmethod
    def get_pin(cls):
        return BalanceAndPin.__pin


class ATM:
    def CheckPin(self):
        try:
            input_pin = int(input("Enter your pin: "))
        except:
            self.invalid_number()
            self.CheckPin()
        else:
            if input_pin == BalanceAndPin.get_pin():
                self.Menu()
            else:
                print("*****************************")
                print("Please enter a valid pin")
                print("*****************************")
                self.CheckPin()

    def Menu(self):
        self.print_options()
        try:
            input_choice = int(input("Enter your choice: "))
        except:
            self.invalid_number()
            self.Menu()
        else:
            if input_choice == 1:
                self.CheckBalance()
            elif input_choice == 2:
                self.WithdrawMoney()
            elif input_choice == 3:
                self.DepositMoney()
            elif input_choice == 4:
                return
            else:
                print("*****************************")
                print("Please enter a valid choice")
                print("*****************************")
                self.Menu()

    def CheckBalance(self):
        print("*****************************")
        print("Your balance is: ${}".format(BalanceAndPin.get_balance()))
        print("*****************************")
        self.Menu()

    def WithdrawMoney(self):
        try:
            input_money = float(input("Enter the amount to withdraw: "))
        except:
            self.invalid_number()
            self.WithdrawMoney()
        else:
            if input_money > BalanceAndPin.get_balance():
                print("*****************************")
                print("Insufficent funds")
                print("*****************************")
                self.Menu()
            else:
                BalanceAndPin.set_balance(BalanceAndPin.get_balance() - input_money)
                print("*****************************")
                print("${} is withdrawn successfully".format(input_money))
                print("*****************************")
                self.CheckBalance()

    def DepositMoney(self):
        try:
            input_money = float(input("Enter the amount to deposit: "))
        except:
            self.invalid_number()
            self.DepositMoney()
        else:
            BalanceAndPin.set_balance(BalanceAndPin.get_balance() + input_money)
            print("*****************************")
            print("${} is deposited successfully".format(input_money))
            print("*****************************")
            self.CheckBalance()

    def invalid_number(self):
        print("*****************************")
        print("Please enter a valid number")
        print("*****************************")

    def print_options(self):
        print("For checking the balance press 1")
        print("For withdrawing money press 2")
        print("For depositing money press 3")
        print("To exit press 4")


object = ATM()
object.CheckPin()
