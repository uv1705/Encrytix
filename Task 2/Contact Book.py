# contact_book.py

contact_book = []

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone_number": phone_number, "email": email, "address": address}
    contact_book.append(contact)
    print(f"Contact '{name}' added!")

def view_contacts():
    print("Contact List:")
    for i, contact in enumerate(contact_book, 1):
        print(f"{i}. {contact['name']} - {contact['phone_number']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contact_book if search_term in contact["name"] or search_term in contact["phone_number"]]
    if found_contacts:
        print("Search results:")
        for contact in found_contacts:
            print(f"{contact['name']} - {contact['phone_number']}")
    else:
        print("No contacts found.")

def update_contact():
    name = input("Enter contact name to update: ")
    for contact in contact_book:
        if contact["name"] == name:
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact["phone_number"] = phone_number
            contact["email"] = email
            contact["address"] = address
            print(f"Contact '{name}' updated!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    for contact in contact_book:
        if contact["name"] == name:
            contact_book.remove(contact)
            print(f"Contact '{name}' deleted!")
            return
    print("Contact not found.")

while True:
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")