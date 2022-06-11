import json
from time import sleep

sample_entry_1 = {'First name': 'Tony', 'Last name': 'Stark',
                  'Cellphone': '69', 'Workphone': '', 'Email': 'stanleefav@marvel.com'}

sample_entry_2 = {"First name": "Bruce", "Last name": "Wayne",
                  "Cellphone": "42", "Workphone": "0973033324", "Email": "bestdetective@dc.com"}

sample_entry_3 = {"First name": "Dead", "Last name": "Pool",
                  "Cellphone": "999", "Workphone": "", "Email": "FuckDeath@marvel.com"}


contacts = [sample_entry_1, sample_entry_2, sample_entry_3]
# contacts = str(sample_entry_1) + str(sample_entry_2) + str(sample_entry_3)

with open('contacts.json', 'w') as f:
    json.dump(contacts, f)  # writes a Python dictionary as a json file

with open('contacts.json', 'r') as f:
    saved_contacts = json.load(f)  # loads the file as a Python list

for _ in range(15):
    try:
        # {'contacts': [{'first_name': 'Tim', ...}]}
        print(saved_contacts[_])
    except:
        print('Out of entries!')
        sleep(2)
        break

sample_entry_4 = {"First name": "Vic", "Last name": "Savage",
                  "Cellphone": "666", "Workphone": "999", "Email": "whowhatwhenwherewhy@hellskitchen.com"}

saved_contacts.append(sample_entry_4)

with open('contacts.json', 'w') as f:
    json.dump(saved_contacts, f)  # writes a Python dictionary as a json file
