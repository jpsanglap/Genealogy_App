from familytree import FamilyTree
import json

class Person(FamilyTree):

    def __init__(self):
        super().__init__()


    def create_person(self):
        person_name = input("Name: ")
        if person_name == "":
            print("Need to input name before proceeding...")
            self.create_person()
        else:
            super().person_name(person_name)
            person_birthdate = input("Birthdate: ")
            super().person_birthdate(person_birthdate)
            person_father = input("Father's Name: ")
            person_mother = input("Mother's Name: ")
            super().create_parents(person_father, person_mother)
            self.print_data()

    def search_person(self,text):
        search_name = input(f"Enter name to be {text}: ")
        if search_name == "":
            print("Need to input name before proceeding...")
            self.search_person(text)
            return None
        else:
            try:
                with open("family_data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                print("File not available to search.")
            else:
                super().person_name(search_name)
                if self.name in data:
                    super().person_birthdate(data[self.name]["Birthdate"])
                    super().create_parents(data[self.name]["Father"], data[self.name]["Mother"])
                    self.print_data()
                    return True
                else:
                    print(f"{self.name} not found.")
                    return False


    def save_data(self):
        data_file = {
                self.name:
                    {
                        "Birthdate": self.birthdate,
                        "Father": self.father,
                        "Mother": self.mother
                    }
                }

        try:
            with open("family_data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("family_data.json", "w") as file:
                json.dump(data_file, file, indent=4)
        else:
            data.update(data_file)
            with open("family_data.json", "w") as file:
                json.dump(data, file, indent=4)

    def delete_data(self):
        try:
            with open("family_data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("File not available for delete.")
        else:
            del data[self.name]
            print("Data deleted.")
            with open("family_data.json", "w") as file:
                json.dump(data, file, indent=4)


    def print_data(self):
        print(f"Name is {self.name} and birthdate is {self.birthdate}")
        print(f"The father's name is {self.father} and mother's name is {self.mother}")
