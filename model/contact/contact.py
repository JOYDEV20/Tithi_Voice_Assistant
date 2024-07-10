import json
import os

CONTACTS_FILE = 'contacts.json'

def save_contact(name, number):
    contacts = load_contacts()
    contacts[name] = number
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f)
    return f"Contact {name} saved successfully."

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, 'r') as f:
        return json.load(f)

def get_contact(name):
    contacts = load_contacts()
    return contacts.get(name, f"Contact {name} not found.")