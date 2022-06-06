import json
from contact import contact


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
    write_contacts(CONTACT_FILE_PATH, contacts.dict_form)


def search_for_contact(contacts):
    pass


def delete_contact(contacts):
    pass


def list_contacts(contacts):
    pass


def take_phone_number(phone_type):
    if phone_type == 'cell':
        phone_number = input('Enter cellphone number: ')
    elif phone_type == 'work':
        phone_number = input('Enter work phone number: ')
    else:
        print('invalid phone choice')
        return 0

    # clean up phone number, get rid of special characters
    phone_clean = ''
    for char in phone_number:
        if char in '0123456789':
            phone_clean += char

    return phone_clean


def main(contacts_path):
    print(read_contacts(CONTACT_FILE_PATH))


if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
