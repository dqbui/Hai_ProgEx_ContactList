class contact:
    def __init__(self, first, last, cell, work, email):
        self.first_name = first.capitalize()
        self.last_name = last.capitalize()
        self.cellphone = cell
        self.workphone = work
        self.email = email
        self.dict_form = self._create_dictionary_form()

    def __str__(self):
        first_line = f'Full name: {self.first_name} {self.last_name}\n'
        second_line = f'Cellphone: \t{self.cellphone}\n'
        third_line = f'Workphone: \t{self.workphone}\n'
        fourth_line = f'Email: \t{self.email}\n'

        output_string = first_line+second_line+third_line+fourth_line

        return output_string

    def _create_dictionary_form(self):
        output_dict = {}
        output_dict['First name'] = self.first_name
        output_dict['Last name'] = self.last_name
        output_dict['Cellphone'] = self.cellphone
        output_dict['Workphone'] = self.workphone
        output_dict['Email'] = self.email

        return output_dict
