import json


CONTACT_FILE_PATH = "contacts.json"


def read_contacts(file_path):
    try:
        with open(file_path, 'r') as f:
            contacts = json.load(f)['contacts']
    except FileNotFoundError:
        contacts = []

    return contacts


def write_contacts(file_path, contacts):
    with open(file_path, 'w') as f:
        contacts = {"contacts": contacts}
        json.dump(contacts, f)


def verify_email_address(email):
    if "@" not in email:
        return False

    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True


def add_contact(contacts):
    pass


def search_for_contact(contacts):
    pass


def delete_contact(contacts):
    pass


def list_contacts(contacts):
    pass


def main(contacts_path):
    print('Welcome to your contact list!\n')

    print('The following is a list of useable commands:')
    print('\"add\" \t\tAdds a contact')
    print('\"delete\" \tDeletes a contacnt')
    print('\"list\" \t\tLists all contacts.')
    print('\"search\" \tSearches for a contact by name.')
    print('\"q\" \t\tQuits the program and saves the contact list.')

    while True:
        user_command = input('Please enter a command: ').lower()
        if user_command == 'add':
            print(user_command)
        elif user_command in ['delete', 'del']:
            print(user_command)
        elif user_command in ['list', 'lst', 'ls']:
            print(user_command)
        elif user_command in ['search', 's']:
            print(user_command)
        elif user_command == 'q':
            break
        else:
            print('Unknown command...')


if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
