class BankAccount:

    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, add):
        self.balance += add

    def withdraw(self, reduce):
        if reduce <= self.balance:
            self.balance -= reduce

        else:
            print('Saldo insuficiente')

    def print_balance(self):
        print(f"Saldo atual: R${self.balance:.2f}")

    def __str__(self):
        return f'BankAccount: {self.holder}; R${self.balance:2f}'


def main():

    person1 = BankAccount("João", 1000)

    person1.deposit(500)
    person1.print_balance()

    person1.withdraw(2000)

    person1.withdraw(800)
    person1.print_balance()  #

    print(person1)

if __name__ == '__main__':
    main()
