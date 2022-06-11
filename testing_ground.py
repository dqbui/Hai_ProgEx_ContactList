import json
from time import sleep

# sample_entry_1 = {'First name': 'Tony', 'Last name': 'Stark',
#                   'Cellphone': '69', 'Workphone': '', 'Email': 'stanleefav@marvel.com'}

# sample_entry_2 = {"First name": "Bruce", "Last name": "Wayne",
#                   "Cellphone": "42", "Workphone": "0973033324", "Email": "bestdetective@dc.com"}

# sample_entry_3 = {"First name": "Dead", "Last name": "Pool",
#                   "Cellphone": "999", "Workphone": "", "Email": "FuckDeath@marvel.com"}


# contacts = {'contacts': [sample_entry_1, sample_entry_2, sample_entry_3]}

# with open('contacts.json', 'w') as f:
#     json.dump(contacts, f)  # writes a Python dictionary as a json file

with open('contacts.json', 'r') as f:
    contacts = json.load(f)  # loads the file as a Python dictionary

for _ in range(15):
    try:
        # {'contacts': [{'first_name': 'Tim', ...}]}
        print(contacts['contacts'][_])
    except:
        print('Out of entries!')
        sleep(2)
        break
