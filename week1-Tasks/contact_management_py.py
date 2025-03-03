import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as file:
        return json.load(file)

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone or not email:
        print("Error: All fields are required.")
        return

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Error: Contact with this name already exists.")
            return

    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("✅ Contact added successfully.")

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"\n Contact Found:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n")
            return
    print("Contact not found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Current Phone: {contact['phone']}")
            print(f"Current Email: {contact['email']}")
            new_phone = input("Enter new phone number (leave blank to keep current): ").strip()
            new_email = input("Enter new email (leave blank to keep current): ").strip()

            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email

            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n Contact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()

