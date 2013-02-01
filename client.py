#!/user/bin/python
# Python based IRC
#client end
from sys import argv

file, choice = argv

address_file = "./recentConnection.con"
address = ""
#Functions
def load():
    try:
        address = open(address_file, 'r').read()
    except:
        new_file = open(address_file, 'w')
        address = raw_input("Please enter the URL for the server: ")
        new_file.write(address)
        new_file.close()
    return address
    
def create_new():
    address = raw_input("Where would you like to connect? ")
    new_file = open(address_file, 'w')
    new_file.write(address)
    new_file.close()
    return address
def unusable_input():
    action = raw_input("Would you like to 'load' a connection or create a 'new' one?")
    if action == "load":
        return load()
    elif action == "new":
        return create_new()
    else:
        return unusable_input()

#start of code

#User launches application
if choice == "yes":
    address = load()
elif choice == "no":
    address = create_new()
else:
    address = unusable_input()
        
print "Connecting to: ", address

