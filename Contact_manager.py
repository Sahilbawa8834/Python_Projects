contact_list = []
def add_contacts():
	name = input("Enter the name for contact: ")
	number = int(input("enter the new number: "))
	contact_list.append({"name": name, "phone": number})
	print("contact added successfully")
#To display all contacts
def display_contacts():
	if not contact_list:
		print("no contacts to display")
	else:
		print("contacts: ")
		for i, contact in enumerate(contact_list, start=1 ):
			print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")
#To provide menue bar for user 
def main():
	while True:
		print("\nSimple Contact Manager")
		print("1. Add Contact")
		print("2. Display Contacts")
		print("3. Exit")
		choice = input("enter you choice: ")
		if choice == '1':
			add_contacts()
		elif choice == '2':
			display_contacts()
		elif choice == '3':
			print("exiting the program")
			break
		else:
			print("invalid choice try again ")

#to run the program 
if __name__ == "__main__":
	main()




