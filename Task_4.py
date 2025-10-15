class BankAccount:
    account: int = 0
    username: str

    def __init__(self, initial_account: int, name: str) -> None:
        self.account = initial_account
        self.username = name
        print(f"{self.username}, вы успешно создали счет!")
        
    def top_up(self, amount: int) -> None:
        self.account += amount
        print(f"Вы пополнили счет на {amount} рублей.")

    def write_off(self, amount: int) -> None:
        self.account -= amount
        print(f"Вы списали {amount} рублей.")
        if self.account < amount:
            print("Невозможно произвести списание, недостаточно средств на счете.")

    def check_balance(self) -> None:
        print(f"На вашем счете {self.account} рублей.")
    
    def transfer(self, amount: int, usr: str) -> int:
        print(f"Вы перевели {usr} {amount} рублей.")
        self.account -= amount
        return amount
    

acc = str(input("Введите ваше имя: "))
acc_v = int(input("Напишите, сколько денег вы хотите положить на счет: "))

self_acc = BankAccount(initial_account=acc_v, name=acc)

top = int(input("\nНапшите, на какую сумму пополнить счет: "))
self_acc.top_up(amount=top)

write = int(input("\nНапшите, на какую сумму списать со счета: "))
self_acc.write_off(amount=top)

self_acc.check_balance()

transfer_to_user = str(input("\nВведите имя, которому вы хотите осуществить перевод: "))
transfer_money = int(input(f"Напшите, какую сумму вы хотите перевести {transfer_to_user}: "))
self_acc.transfer(amount=transfer_money, usr=transfer_to_user)

