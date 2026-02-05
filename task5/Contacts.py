contacts = {}

def pause():
    input("\nPress Enter to continue...")

def add_contact():
    print("\n➕ Add New Contact")
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("\nContact added successfully")
    pause()

def view_contacts():
    print("\n📒 Contact List")

    if not contacts:
        print("No contacts available")
        pause()
        return

    for i, (name, details) in enumerate(contacts.items(), start=1):
        print(f"{i}. {name}  |  {details['phone']}")

    pause()

def search_contact():
    print("\n🔍 Search Contact")
    key = input("Enter name or phone: ").strip()

    for name, details in contacts.items():
        if key.lower() in name.lower() or key == details["phone"]:
            print("\nContact Found")
            print("Name   :", name)
            print("Phone  :", details["phone"])
            print("Email  :", details["email"])
            print("Address:", details["address"])
            pause()
            return

    print("Contact not found")
    pause()

def update_contact():
    print("\n✏️ Update Contact")
    name = input("Enter contact name: ").strip()

    if name not in contacts:
        print("Contact not found")
        pause()
        return

    print("Leave blank to keep existing value")

    phone = input("New Phone: ")
    email = input("New Email: ")
    address = input("New Address: ")

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    if address:
        contacts[name]["address"] = address

    print("\nContact updated successfully")
    pause()

def delete_contact():
    print("\n🗑 Delete Contact")
    name = input("Enter contact name: ").strip()

    if name in contacts:
        confirm = input(f"Are you sure you want to delete {name}? (y/n): ")
        if confirm.lower() == "y":
            del contacts[name]
            print("Contact deleted")
        else:
            print("Deletion cancelled")
    else:
        print("Contact not found")

    pause()

def main():
    print("===================================")
    print("   📱 CONTACT MANAGEMENT SYSTEM")
    print("===================================")

    while True:
        print("\nMain Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

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
            print("\nThank you for using Contact Management System")
            break
        else:
            print("Invalid choice, please try again")

main()
