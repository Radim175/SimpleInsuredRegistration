import re
from insured import Insured


# managing the list of insured persons
class InsuredManager:

    def __init__(self):
        self.insured_list = []

    # create a new insured and add to the list, includes validation of name, surname, age and telephone number
    def create_insured(self, first_name, last_name, age, phone_number):
        if not first_name or not last_name:
            print("Jméno a příjmení nemohou být prázdné.")
            return
        if not age.isdigit() or not 0 < int(age) < 99:
            print("Věk musí být celé kladné číslo v rozmezí 1 až 99.")
            return
        if not re.match(r'^\d{9}$', phone_number):
            print("Telefonní číslo musí mít 9 číslic a musí být bez mezer. Příklad: 777222888")
            return
        insured = Insured(first_name, last_name, age, phone_number)
        self.insured_list.append(insured)
        print(f"Pojištěný '{insured.first_name} {insured.last_name}' úspěšně vytvořen.")

    # prints all insured persons in the list
    def list_all_insured(self):
        if not self.insured_list:
            return ("Nebyly nalezeny žádné pojištěné osoby.")
        return [str(insured) for insured in self.insured_list]

    # search for insured persons by name or surname
    def search_insured(self, search_name):
        if not self.insured_list:
            return ("Nebyly nalezeny žádné pojištěné osoby.")
        # create new list contains only insureds that match the search, using list comprehension to browse through each insured
        matching_insured = [insured for insured in self.insured_list if search_name.lower() in (insured.first_name.lower(), insured.last_name.lower())]
        # processes the search result
        if not matching_insured:
            return ("Nebyly nalezeny žádné odpovídající pojištěné osoby.")
        return [str(insured) for insured in matching_insured]