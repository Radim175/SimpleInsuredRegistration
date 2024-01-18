class Insured:

    # initialization the properties of insured object
    def __init__(self, first_name, last_name, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number

    # object representation in text form
    def __str__(self):
        return f"{self.first_name} {self.last_name}, Věk: {self.age}, Telefon: {self.phone_number}"