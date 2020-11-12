def validation(accounts):
    name = input("Enter your name: ")
    for account in accounts:
        # Checking account name
        if account.name.lower() == name.lower():
            pin = int(input("\nEnter 4 digits PIN: "))
            # Checking PIN length
            if len(str(pin)) != 4:
                print("\nInvalid PIN.")
                return try_again(accounts)
            # Checking PIN
            if account.pin == pin:
                print("\nWelcome! {}, your account balance is ${}".format(account.name.upper(), account.balance))
                return withdrawal(account)
            else:
                print("\nThe PIN is incorrect")
                return try_again(accounts)
    else:
        print("\nThere is no account with that name.")
        return try_again(accounts)

			
def withdrawal(account):
	amount = int(input("\nEnter amount to withdraw: "))
	if account.balance > amount:
		account.balance -= amount
		print("\nTransaction successful, your new balance is ${}".format(account.balance))
		new = input("\nNew transaction? YES/NO?: ")
		if new.lower() == "yes":
			return withdrawal(account)
		print("\nTake your card {}. Thank you for banking with us.".format(account.name.upper()))
	else:
		print("\nTransaction failed due to insufficient funds.")
					
	
def try_again(accounts):
	re_enter = input("\nEnter YES to try again or NO to exit: ")
	if re_enter.lower() == "yes":
		return validation(accounts)
	elif re_enter.lower() == "no":
		print("\nGoodbye. Take your card.")
	else:
		print("\nInvalid input. Take your card.")
	
		
class Account:
	def __init__(self, name, pin, balance):
		self.name = name
		self.pin = pin
		self.balance = balance
		

accounts = [Account("Somtochukwu", 4289, 300000), Account("Chidubem", 3329, 250000), Account("Munachi", 2200, 220000)]


validation(accounts)

