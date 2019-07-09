#burrow's creation

#Python 3.7.3

#use of functions and dict


#list of player / store equipment
playerinventory = {
		"Gold" : 1000,
		"Sword": 0,
		"HP Potion": 0,
		"Mana Potion": 0
}

storeinventory = {
		"Gold" : 666,
		"Sword" : 20,
		"HP Potion" : 10,
		"Mana Potion" : 10
}
print('\n'*100)
print('This is a test for a very simple shop menu..')
#The main menu
def Items():

	print("ψ Welcome To My Shop ψ")
	print("-" * 15)
	for x, y in storeinventory.items():
		print(x, y)
	print("-" * 15)
	print("Player Inventory")
	print("-" * 15)
	for x, y in playerinventory.items():
		print(x, y)

	choice = input("""
[1] Buy
[2] Sell
[3] Leave
>? """)
#choices you are able to make initailly
	if choice == "1":
		buy()
	elif choice == "2":
		sell()
	elif choice == "3":
		quit()
	else:
		Items()
#buy function
def buy():
	choice = input("""
[1] Sword for 20 Gold
[2] HP Potion for 15 Gold
[3] Mana Potion for 15 Gold
>? """)
	if choice == "1":
		if playerinventory["Gold"] >= 20 :
			playerinventory["Gold"] -= 20
			storeinventory["Gold"] += 10
			storeinventory["Sword"]-= 1
			if "Sword" in playerinventory:
				playerinventory["Sword"] += 1
				print("\n"*100)
				print("You have purchased Another Sword")
				Items()
			else:
				playerinventory["Sword"] = 1
				print("\n"*100)
				print("You have purchased a Sword")
				Items()
		else:
			print("\n"*100)
			print("Not Enough Coin")
			Items()
	if choice == "2":
		if playerinventory["Gold"] >= 15:
			playerinventory["Gold"] -= 15
			storeinventory["Gold"] += 15
			storeinventory["HP Potion"] -= 1
			if "HP Potion" in playerinventory:
				playerinventory["HP Potion"] += 1
				print("\n"*100)
				print("You Have Purchased Another HP Potion")
				Items()
			else:
				playerinventory["HP Potion"] = 1
				print("\n"*100)
				print("you have Purchased an HP Potion")
				Items()
		else:
			print("\n"*100)
			print("Not Enough Coin")
			Items()
	if choice == "3":
		if playerinventory["Gold"] >= 15:
			playerinventory["Gold"] -= 15
			storeinventory["Gold"] += 15
			storeinventory["Mana Potion"] -= 1
			if "Mana Potion" in playerinventory:
				playerinventory["Mana Potion"] += 1
				print("\n"*100)
				print("You Have Purchased Another Mana Potion")
				Items()
			else:
				playerinventory["Mana Potion"] = 1
				print("\n"*100)
				print("you have Purchased an Mana Potion")
				Items()
		else:
			print("\n"*100)
			print("Not Enough Coin")
			Items()
	else:
		print("Enter Valid Choice")
		buy()
#sell Function
def sell():
	print('\n'*100)
	print("Your Inventory Contains")
	for x, y in playerinventory.items():
		print(x, y)
	choice = input("""
[1] Sword
[2] HP Potion
[3] Mana Potion
>? """)

	if choice == "1" :
		if playerinventory["Sword"] >= 1:
			storeinventory["Gold"] -= 10
			storeinventory["Sword"] += 1
			playerinventory["Sword"] -= 1
			playerinventory["Gold"] += 10
			Items()
		elif playerinventory["Sword"] == 0:
			print('\n'*100)
			input("You dont have a Sword [ENTER]")
			print('\n'*100)
			Items()
	if choice == "2" :
		if playerinventory["HP Potion"] >= 1:
			storeinventory["Gold"] -= 5
			storeinventory["HP Potion"] += 1
			playerinventory["HP Potion"] -= 1
			playerinventory["Gold"] += 5
			Items()
		elif playerinventory["HP Potion"] == 0:
			print('\n'*100)
			input("You dont have an HP Potion [ENTER]")
			print('\n'*100)
			Items()
	if choice == "3" :
		if playerinventory["Mana Potion"] >= 1:
			storeinventory["Gold"] -= 5
			storeinventory["Mana Potion"] += 1
			playerinventory["Mana Potion"] -= 1
			playerinventory["Gold"] += 5
			Items()
		elif playerinventory["Mana Potion"] == 0:
			print('\n'*100)
			input("You dont have a Mana Potion [ENTER]")
			print('\n'*100)
			Items()
	else:
		print("\n"*100)
		input("you Dont have the required item[ENTER]")
		print("\n"*100)

		Items()







Items()#initiates the script
