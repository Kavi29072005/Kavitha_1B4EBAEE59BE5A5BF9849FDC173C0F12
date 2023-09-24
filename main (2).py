class BankAccount:
  def __init__(self,acno,acname,acbal=0.0):
    self.__acno = acno
    self.__acname=acname
    self.__acbal=acbal

  def deposit(self,amt):
    if amt > 0:
      self.__acbal +=amt
      print("Deposited Rs.{}. Your Current Balance is : Rs.{}".format(amt,self.__acbal))
    else:
      print("Invalid Data")

  def withdraw(self,amt):
    if amt > 0 and amt <= self.__acbal:
      self.__acbal -= amt
      print("Withdrew Rs.{}. YourCurrent Balance is Rs.{}".format(amt,self.__acbal))
    else:
      print("Invalid Transactions")

  def display(self):
    a=float(self.__acbal)
    b=int(self.__acno)
    print("Hai {} Balance for your Account No. {} is Rs.{}".format(self.__acname,b,a))


acc = BankAccount(636377,"kavitha",2000)
acc.display()
acc.deposit(500)
acc.withdraw(1000)