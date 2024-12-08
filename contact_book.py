def add_contact(contacts):
    while True:
        name = input("Enter contact name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()
        if not phone or not email:
            print("Phone number and email cannot be empty. Please try again.")
            continue
        contacts.append({"name": name, "phone": phone, "email": email})
        print("Contact added successfully!")
        break

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

def search_contact(contacts):
    search_name = input("Enter the name to search for: ").strip().lower()
    results = [c for c in contacts if c["name"].lower() == search_name]   
    if not results:
        print("No contact found with that name.")
    else:
        for contact in results:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']}")


def delete_contact(contacts):
    delete_name = input("Enter the name of the contact to delete: ").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == delete_name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("No contact found with that name.")

def main():
    contacts = []
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()