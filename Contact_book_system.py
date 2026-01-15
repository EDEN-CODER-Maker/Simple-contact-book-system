contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added successfully")

def view_contacts():
    if not contacts:
        print("No contacts found")
    else:
        for contact in contacts:
            print(contact["name"], "-", contact["phone"])

def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
