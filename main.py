class ContactManager:
    def __init__(self):
        self.contacts = {}  # Store contacts in a dictionary

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact with the name '{name}' already exists. Updating details...")
        self.contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact '{name}' added/updated successfully.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact Details for '{name}':")
            print(f"  Phone: {self.contacts[name]['Phone']}")
            print(f"  Email: {self.contacts[name]['Email']}")
        else:
            print(f"Contact with the name '{name}' not found.")

    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("All Contacts:")
            for name, details in self.contacts.items():
                print(f"  Name: {name}")
                print(f"    Phone: {details['Phone']}")
                print(f"    Email: {details['Email']}")

# Main program
if __name__ == "__main__":
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()
            manager.add_contact(name, phone, email)

        elif choice == 2:
            name = input("1Enter name to search: ").strip()
            manager.search_contact(name)

        elif choice == 3:
            manager.display_all_contacts()

        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
