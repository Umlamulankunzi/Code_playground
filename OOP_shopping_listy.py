# shopping app 
import os
import datetime

class ShopApp(object):
	
	dat = datetime.datetime.now()
	dtg = datetime.datetime.strftime(dat, '%a %d %b %y [%H:%M]')

	def __init__(self):
		print("Welcome to the Shopping List App \nPlease enter your name to continue")
		self.name = input("What is your name? ")
		self.shop_lst = []
		self.show_help()
		self.main()	

	def show_help(self):
		self.clear()
		if len(self.shop_lst) ==0:
			print ("Welcome to the Shopping list app\n")
		print("""Enter  items to shopping list 
Enter "show" to show list 
Enter "help" to show this help
Enter "done" or "quit"  to quit app
Enter "save" to save list to file    

By default the app will save your list 
to file when you exit the app
""")

	def clear(self):
		os.system("clear")

	def show_lst(self):
		self.clear()
		if len(self.shop_lst) != 0:
			print(self.dtg + "\n")
			print("{} Shopping list contains:".format(self.name))
			index = 1
			for item in self.shop_lst:
				print ("{}. {}".format(index, item))
				index += 1
				
			print("-"*10)
			index = 1
		else:
			print("Your list is currently empty")
			print("Please enter items to your list")

	def add_item(self):
		self.clear()
		index = 1
		
		if self.usr_in in self.shop_lst:
			print("{} Shopping List: \n".format(self.name))
			for item in self.shop_lst:
				print("{}. {}".format(index, item))
				index += 1
			print("\n" + "-"*10)
			print("{} already in list".format(self.usr_in))
			
		else:	
			self.shop_lst.append(self.usr_in)
			print("{}'s Shopping list:\n".format(self.name))
			for item in self.shop_lst:
				print("{}. {}".format(index, item))
				index += 1
			
			print("\n" + "-"*10)
			print ("{} added to list".format(self.usr_in))
							
	def save_lst(self, user_cmd):
		
		#using input from user if input is save print further items else if cmd is quit print only list saved]
		self.user_cmd = user_cmd
		self.clear()
		
		if len(self.shop_lst) != 0:
			
			self.file_name = self.name +".txt"
		
			with open(self.file_name, "w+") as F:
				F.write(self.dtg +"\n")
				F.write("{}'s Shopping list\n".format(self.name))
				F.write("-"*10 +"\n")
				
				index = 1
				for item in self.shop_lst:
					F.write("{}. {}\n".format(index, item))
					index += 1
				F.write("-"*10)
				
			if self.user_cmd =='save':	
				print("Your shopping list has been saved")
				print("Continue adding more items or",
				"\nEnter done to quit app")
				
			else:
				print("Your Shopping list has been saved \nGoodbye")
				
		else:
			print("Your list is currently empty",
			"\nPlease enter items to your list to save it.")
						
	def remv_itm(self):
		self.clear()
		self.show_lst()
		print ("Which item do you want to remove")
		self.user_item = input(":>> ").lower()
		
		if self.user_item in self.shop_lst:
			self.shop_lst.remove(self.user_item)	
			self.show_lst()
			print ("{} removed from list".format(self.user_item))
		else:
			print("Sorry cant find {} in your list".format(self.user_item))
				
	def main(self):
		while True:
			self.usr_in = input(":> ").lower()
			
			if self.usr_in == 'show':
				self.show_lst()
			elif self.usr_in == 'help':
				self.show_help()
			elif self.usr_in == 'save':
				self.save_lst(self.usr_in)
			elif self.usr_in == 'done' or self.usr_in== "quit":
				self.show_lst()
				self.save_lst(self.usr_in)
				break
			elif self.usr_in == 'remove':
				self.remv_itm()
			else:
				self.add_item()
				

my_list = ShopApp()