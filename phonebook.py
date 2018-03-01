print ("Hey you here to save phone numbers")

contact_list = {}

def get_name(name):

	if len(name) < 2:
		raise ValueError("The name has to be longer than that.")

def get_phone_no(no):

	to_s = str(no)

	if len(to_s) < 10:
		raise ValueError("Your phone number is too short.")

name = input("Input the name below\n>>> ")
get_name(name)


phone_number =  input("Input the phone number\n>>> ")
get_phone_no(phone_number)

contact_list[name] = phone_number
#print (contact_list)

#print ("The name is {} and the phone number is {}.".format(name, phone_number))