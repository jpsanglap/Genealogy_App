from familytree import FamilyTree
import json


class Person(FamilyTree):

    FAMILY_FILE = "family_data.json"

    def __init__(self):
        super().__init__()

    def create_person(self):
        fname = input("First Name: ").strip()
        while True:
            lname = input("Last Name: ").strip()
            if lname == "":
                print("Need to input at least surname before proceeding...")
                continue
            break
        super().person_name(fname, lname)
        person_birthyear = input("Year of birth (YYYY): ")
        person_birthmonth = input("Month of birth (MMM): ")
        person_birthday = input("Day of birth (DD): ")
        super().person_birthdate(person_birthyear, person_birthmonth, person_birthday)
        person_father = input("Father's Name: ")
        person_mother = input("Mother's Name: ")
        super().create_parents(person_father, person_mother)
        self.print_data()

    def search_person(self, del_flag):

        if not del_flag:
            text = "searched"
        else:
            text = "deleted"

        while True:
            search_fname = input(f"Enter first name to be {text}: ").strip()
            if del_flag and search_fname == "":
                print("Need first name if you want to delete")
                continue

            while True:
                search_lname = input(f"Enter last name to be {text}: ").strip()
                if search_lname == "":
                    print("Need to input last name before proceeding...")
                    continue
                break

            break

        try:
            with open("family_data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("File not available to search.")
        else:
            results = [p for p in data if p["lastname"].lower() == search_lname.lower()]
            if search_fname != "":
                results = [p for p in results if p["firstname"].lower() == search_fname.lower()]

            if len(results) > 0:
                super().person_name(search_fname, search_lname)
                for person in results:
                    print(f"First name: {person['firstname']}")
                    print(f"Last name: {person['lastname']}")
                    print(f"Birthdate: {person['birthdate']}")
                    print("Parents are:")
                    print(f"Father: {person['parents']['father']}")
                    print(f"Mother: {person['parents']['mother']}")
                return True
            else:
                print(f"{search_fname} {search_lname} not found in file.")
                return False

    def save_data(self):

        data_file = {
                "firstname" : self.first_name,
                "lastname" : self.last_name,
                "birthdate" : self.birthdate,
                "parents" : {
                    "father": self.father,
                    "mother": self.mother
                }

            }

        try:
            with open(self.FAMILY_FILE, "r") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
        except FileNotFoundError:
            data = [data_file]
            with open(self.FAMILY_FILE, "w") as file:
                json.dump(data, file, indent=4)
        else:
            data.append(data_file)
            with open(self.FAMILY_FILE, "w") as file:
                json.dump(data, file, indent=4)

    def delete_data(self):
        try:
            with open(self.FAMILY_FILE, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("File not available for delete.")
        else:
            data = [p for p in data if not (p["firstname"] == self.first_name and
                                            p["lastname"] == self.last_name)]
            print("Data deleted.")
            with open(self.FAMILY_FILE, "w") as file:
                json.dump(data, file, indent=4)


    def print_data(self):
        print(f"Name is {self.first_name} {self.last_name} and birthdate is {self.birthdate}")
        print(f"The father's name is {self.father} and mother's name is {self.mother}")
