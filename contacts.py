contacts = {
    "gana": 67890,
    "sweksha": 76890,
    "shreya": 89054
}

print("Contacts:")
for n, num in contacts.items():
    print(f"Contact: {n} | Phone: {num}")
contacts["syra"] = 90876
print("\nAfter Adding a contact 'syra':")
for n, num in contacts.items():
    print(f"Contact: {n} | Phone: {num}")
contacts["sweksha"] = 98076
print("\nAfter changing an existing contact's number:")
for n, num in contacts.items():
    print(f"Contact: {n} | Phone: {num}")
name = input("\nEnter the contact name : ").lower()
print(contacts.get(name, "Contact not found"))

