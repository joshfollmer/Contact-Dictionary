#Josh Follmer, dictionary assignment

contact = {}


def start_contact(name):
    '''
    Function to make a contact page
    '''
    global contact
    contact = {'name': name}
    number = input("Phone number: ")
    if number == '' or number == 'none':
        pass
    else:
        contact['Phone number'] = number
    address = input("Address: ")
    if address == '' or address == 'none':
        pass
    else:
        contact['Address'] = address
    email = input("Email address: ")
    if email == '' or email == 'none':
        pass
    else:
        contact['Email'] = email
    #prints out the result
    print(contact)
    #runs the edit function 
    edit_contact()

def edit_contact():
    '''
    Function to add or delete items from to an existing contact
    '''
    global contact
    #first asks if they want to change anything
    choice = input('Edit contact?\n')

    if choice == 'yes' or choice == 'y':
        #then asks if they want to add or delete something 
        choice = input('Add or delete information?\n')
        if choice == 'add' or choice == 'a':
            #asks if they want to add (or update if one exists) a new phone, address, email 
            choice = input('Add or update a new phone number, address, or email address?\n')
            if choice == 'phone number' or choice == 'number' or choice == 'n':
                #gets the phone number
                number = input("Phone number: ") 
                #adds the number    
                contact['Phone number'] = number
            elif choice == 'address' or choice == 'a':
                #gets the new address
                address = input("Address: ")
                #puts in the address
                contact['Address'] = address
            elif choice == 'email address' or choice == 'email' or choice == 'e':
                #gets the new email
                email = input("Email address: ")
                #adds in the new email
                contact['Email'] = email
            else:
                print("Invalid entry")
                edit_contact()
        elif choice == 'delete' or choice == 'd':
            #asks which value they want to delete
            choice = input("Delete a phone number, address, or email address?")
            if choice == 'phone number' or choice == 'number' or choice == 'n':
                #trys to delete a number, if there isnt one to delete it will run the function again. the same goes for each attribute
                try:
                    contact.pop('Phone number')
                except:
                    print('Attribute not found')
                    edit_contact()
            elif choice == 'address' or choice == 'a':
                try:
                    contact.pop('Address')
                except:
                    print('Attribute not found')
                    edit_contact()
            elif choice == 'email address' or choice == 'email' or choice == 'e':
                try:
                    contact.pop('Email')
                except:
                    print('Attribute not found')
                    edit_contact()
        print(contact)
        edit_contact()
    #prints out the result
    print(contact)
    #runs edit contact
    



#asks the user for the contacts name
user_input = input("New contact's name?\n")
#runs the make contact function
start_contact(user_input)
