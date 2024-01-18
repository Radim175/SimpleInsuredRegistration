from insured_manager import InsuredManager


# main logic for interaction with user
def main():
    insured_manager = InsuredManager()
    # monitoring program status
    running = True

    # cycle for user input
    while running:
        print('''____________________________
    Evidence pojištěných
____________________________''')
        print("1. Přidat nového pojištěného")
        print("2. Vypsat všechny pojištěné")
        print("3. Vyhledat pojištěného")
        print("4. Konec")

        choice = input("Zvolte (1-4): ")

        # processing the input and calling the corresponding methods
        if choice == '1':
            first_name = input("Zadejte jméno pojištěného: ")
            last_name = input("Zadejte příjmení pojištěného: ")
            age = input("Zadejte věk: ")
            phone_number = input("Zadejte telefonní číslo: ")
            insured_manager.create_insured(first_name, last_name, age, phone_number)

        elif choice == '2':
            insured_data = insured_manager.list_all_insured()
            for data in insured_data:
                print(data)

        elif choice == '3':
            search_name = input("Zadejte jméno nebo příjmení pojištěného: ")
            # converts the search name to lowercase for consistent matching
            search_name = search_name.lower()
            insured_data = insured_manager.search_insured(search_name)
            for data in insured_data:
                print(data)

        elif choice == '4':
            print("Ukončuji aplikaci. Nashledanou!")
            # end of cycle
            running = False

        else:
            print("Neplatná volba. Prosím zvolte možnost mezi 1 a 4.")


# condition to run main() only when the script is run directly
if __name__ == "__main__":
    main()