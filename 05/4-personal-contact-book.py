# Write a program for personal contact book using Object Oriented Programming approach.
# Menu based interface for creating, updating, searching and removing records.
# The information need to be stored in comma separated text file. 

#Following fields need to be used: 

#Name

#Address

#Birth day 

#Phone number 

#Email

#Profession

#Interests

import json
import functools



class ContactModel:
    def __init__(self,name,address,birthDay,phoneNumber,email,profession,interests):
        self.name = name
        self.address = address
        self.birthDay = birthDay
        self.phoneNumber = phoneNumber
        self.email = email,
        self.profession = profession,
        self.interests = interests


        pass
  
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    # identification
    name: str
    address: str
    birthDay: str
    phoneNumber: int
    email: str
    profession: str
    interests: str
    



# loading all contacts from the file.



file = open("personal-book.json", "r+")


parsedJson = json.loads(file.read())
allContacts = []
for contact in parsedJson:
    def _json_object_hook(d): return ContactModel('X', d.keys())(*d.values())
    def json2obj(data): return json.loads(data, object_hook=_json_object_hook)
    contact = json.loads(contact)
    bindedModel = ContactModel(contact["name"],contact["address"],contact["birthDay"],contact["phoneNumber"],contact["email"],contact["profession"],contact["interests"])
    
    print(bindedModel.name)
    allContacts.append(bindedModel)

def createContact():
        nameInput = input("Type the name of the contact or \"exit\" ")
        if nameInput == "exit":
            return

        addressInput = input("Type the address of the contact or \"exit\" ")
        if addressInput == "exit":
            return


        birthDayInput = input("Type the birtday of the contact or \"exit\" ")
        if birthDayInput == "exit":
            return
        
        phoneNumberInput = int(input("Type the phone number of the contact or \"exit\" "))
        if phoneNumberInput == "exit":
            return

        emailInput = input("Type the email of the contact or \"exit\" ")
        if emailInput == "exit":
            return

        professionInput = input("Type the profession of the contact or \"exit\" ")
        if professionInput == "exit":
            return

        interestsInput = input("Type the interests of the contact or \"exit\" ")
        if interestsInput == "exit":
            return
        
        contact = ContactModel(name=nameInput,address=addressInput,birthDay=birthDayInput,phoneNumber=phoneNumberInput,email=emailInput,profession=professionInput,interests=interestsInput)
        return contact
class Commands:
    
    def availableCommands():
        print("Available commands:\nfind\nedit\nadd\ndelete")
    def add():
        contact = createContact()
        allContacts.append(contact)
        saveToFile()
        print("Successfully saved")
    def edit():
        while True:
            nameInput = input("Enter the name of the contact that you want to edit or \"exit\": ")
            if nameInput == "exit":
                break

            shouldBreak = False
            for contact in allContacts:
                if contact.name == nameInput:
                    editedContact = createContact()
                    contact = editedContact
                    saveToFile()
                    shouldBreak = True
                    break;
            if shouldBreak:
                break
            print("Cannot find account with that name")

    def find():
        while True:
            nameInput = input("Enter the name of the contact that you want to search for or \"exit\": ")
            if nameInput == "exit":
                break

            shouldBreak = False

            for contact in allContacts:
                if contact.name == nameInput:
                    print(contact)
                    shouldBreak = True
                    break
            
            if shouldBreak:
                break
            
            print("Cannot find account with that name")
    def delete():
        while True:
            nameInput = input("Enter the name of the contact that you want to delete for or \"exit\": ")
            if nameInput == "exit":
                break

            deleteFromContacts(nameInput)
            
            print("Contact have been deleted")
            saveToFile()
    
    
def saveToFile():
    serializedArray = list(map(lambda contact: contact.toJSON(), allContacts))
    file.seek(0)
    file.write(json.dumps(serializedArray))
    
    # this is not working
def deleteFromContacts(name):
    dummy = list(filter(lambda c: c.name != contact.name, allContacts))
    allContacts = dummy
        

while True:
    Commands.availableCommands()
    currentInput = input()
    if currentInput == "help":
        Commands.availableCommands()
        continue
    elif currentInput == "find":
        Commands.find()
        continue
    elif currentInput == "delete":
        Commands.delete()
        continue
    elif currentInput == "edit":
        Commands.edit()
        continue
    elif currentInput == "add":
        Commands.add()
        continue

    print("Unrecognized command")

    Commands.availableCommands()
