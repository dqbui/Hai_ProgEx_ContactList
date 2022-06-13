import json

# from more_itertools import first
from contact import contact
from time import sleep

CONTACT_FILE_PATH = "contacts.json"


def read_contacts(file_path):
    try:
        with open(file_path, 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []

    return contacts


# def write_contacts(file_path, contacts):
#     with open(file_path, 'w') as f:
#         contacts = {"contacts": contacts}
#         json.dump(contacts, f)


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
    contact_holder = read_contacts(CONTACT_FILE_PATH)
    # print('Existing contacts:')
    # print(contact_holder)
    # print('Writing new contact')
    # sleep(2)
    contact_holder[contacts.key] = contacts.dict_form
    with open(CONTACT_FILE_PATH, 'w') as f:
        json.dump(contact_holder, f)
    # print('done')


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
    print('Welcome to your contact list!\n')

    print('The following is a list of useable commands:')
    print('\"add\" \t\tAdds a contact')
    print('\"delete\" \tDeletes a contact')
    print('\"list\" \t\tLists all contacts.')
    print('\"search\" \tSearches for a contact by name.')
    print('\"q\" \t\tQuits the program and saves the contact list.')

    while True:
        user_command = input('Please enter a command: ').lower()
        if user_command == 'add':

            # uncomment this section to get user input
            first_name = input('Enter first name: ')
            while len(first_name) < 1:
                print('First name is mandatory!')
                first_name = input('Enter first name again: ')

            last_name = input('Enter last name: ')
            while len(last_name) < 1:
                print('Last name is mandatory')
                last_name = input('Enter last name again: ')

            existing_contacts = read_contacts(CONTACT_FILE_PATH).keys()
            # print(existing_contacts)
            current_name = first_name.capitalize() + ' ' + last_name.capitalize()

            if current_name in existing_contacts:  # check if new entry is already in contact list
                print('Invalid! Contact already exist!!!')
                continue

            cellphone = take_phone_number('cell')
            workphone = take_phone_number('work')
            email = input('Enter email: ')

            while not verify_email_address(email):
                print('Invalid email adress.')
                email = input('Enter email again: ')

            # boogey input
            # first_name = 'James'
            # last_name = 'Bond'
            # cellphone = '0944916475'
            # workphone = '0973033324'
            # email = 'batman@dc.com'

            # checkpoint: print out input so far
            new_contact = contact(first_name, last_name,
                                  cellphone, workphone, email)
            print(new_contact)

            add_contact(new_contact)

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
