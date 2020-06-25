class BankAccount:
  balance = 0
  def __init__(self, name):
    self.name = name
  
  def show_balance(self):
    print("Balance: $%.2f" % (self.balance))

  def deposit(self, amount):
    if amount <= 0:
      print("Error! The amount should be greater than zero.")
    else:
      self.balance += amount
      print("Deposit: $%.2f" % (amount))
      self.show_balance()

  def withdraw(self, amount):
    if amount > self.balance:
      print("Error! The amount is not enough.")
    else:
      self.balance -= amount
      print("Withdraw: $%.2f" % (amount))
      self.show_balance()

  def __repr__(self):
    return("%s's account. Balance: $%.2f" % (self.name, self.balance))


my_account = BankAccount("Augustine")
print(my_account)
my_account.show_balance()
my_account.deposit(3000)
my_account.withdraw(1000)
print(my_account)