import json
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

def print_contact_from_name(full_name):
    all_contact = read_contacts(CONTACT_FILE_PATH)

    target_contact = all_contact[full_name]

    first_name = target_contact['First name']
    last_name = target_contact['Last name']
    cell_phone = target_contact['Cellphone']
    work_phone = target_contact['Workphone']
    email = target_contact['Email']

    print(f'First name: {first_name}')
    print(f'Last name: {last_name}')
    if len(cell_phone) > 0:
        print(f'Cellphone: {cell_phone}')
    if len(work_phone) > 0:
        print(f'Workphone: {work_phone}')
    if len(email) > 0:
        print(f'Email: {email}')

    return


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
    # print('Adding contact:')
    # print(contacts)
    # print('Existing contacts:')
    # print(contact_holder)
    # print('Writing new contact')
    # sleep(2)
    contact_holder[contacts.key] = contacts.dict_form
    with open(CONTACT_FILE_PATH, 'w') as f:
        json.dump(contact_holder, f)
    # print('done')


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


def get_new_contact():
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
    current_name = first_name.capitalize() + ' ' + last_name.capitalize()

    if current_name in existing_contacts:  # check if new entry is already in contact list
        print('Invalid! Contact already exist!!!')
        return None

    cellphone = take_phone_number('cell')
    workphone = take_phone_number('work')
    email = input('Enter email: ')

    while not verify_email_address(email):
        print('Invalid email adress.')
        email = input('Enter email again: ')

    # checkpoint: print out input so far
    new_contact = contact(first_name, last_name,
                          cellphone, workphone, email)
    print('\n Adding contact:')
    print(new_contact)
    return new_contact


def search_for_contact(contacts):
    for name in contacts:
        print_contact_from_name(name)
        print()


def delete_contact(contacts):
    contact_holder = read_contacts(CONTACT_FILE_PATH)
    print(f'Deleting {contacts}')

    del contact_holder[contacts]
    with open(CONTACT_FILE_PATH, 'w') as f:
        json.dump(contact_holder, f)


def get_contact_from_file():
    first_name = input('Enter first name of target contact: ')
    last_name = input('Enter last name of target contact: ')
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    full_name = first_name + ' ' + last_name

    existing_contacts = read_contacts(CONTACT_FILE_PATH).keys()

    if full_name in existing_contacts:
        return full_name
    else:
        print('Invalid! Contact not in directory! Returning to main menu...')
        return None


def list_contacts():
    all_contact = list(read_contacts(CONTACT_FILE_PATH).keys())
    all_contact.sort()

    for name in all_contact:
        print_contact_from_name(name)
        print()


def get_query():  # returns full name string based on user queries, sorted alphabetically
    first_name_query = input('First name search key: ')
    last_name_query = input('Last name search key: ')

    print()
    print('Matching contacts')

    existing_contacts = read_contacts(CONTACT_FILE_PATH).keys()

    search_result = []

    for full_name in existing_contacts:
        first_name, last_name = full_name.split()
        # print(first_name, last_name)
        if first_name_query.lower() in first_name.lower() and last_name_query.lower() in last_name.lower():
            # print(full_name)
            search_result.append(full_name)

    search_result.sort()
    return search_result


def main(contacts_path):
    print('Welcome to your contact list!\n')

    print('The following is a list of useable commands:')
    print('\"Add\" \t\tAdds a contact')
    print('\"Delete\" \tDeletes a contact')
    print('\"List\" \t\tLists all contacts.')
    print('\"Search\" \tSearches for a contact by name.')
    print('\"q\" \t\tQuits the program and saves the contact list.')

    while True:
        user_command = input('Please enter a command: ').lower()
        if user_command == 'add':
            new_contact = get_new_contact()
            if new_contact == None:
                continue
            else:
                add_contact(new_contact)

        elif user_command in ['delete', 'del']:
            target_contact = get_contact_from_file()
            if target_contact == None:
                continue
            else:
                delete_contact(target_contact)

        elif user_command in ['list', 'lst', 'ls']:
            print()
            list_contacts()

        elif user_command in ['search', 's']:
            contact_query = get_query()
            search_for_contact(contact_query)

        elif user_command == 'q':
            break
        else:
            print('Unknown command...')


if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
