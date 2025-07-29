class FamilyTree:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.birthdate = ""
        self.father = ""
        self.mother = ""

    def person_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def person_birthdate(self, year, month, day):
        if day == "" and month != "" and year != "":
            self.birthdate = f"{month}-{year}"
        elif day == "" and month == "" and year != "":
            self.birthdate = f"{year}"
        elif day == "" and month == "" and year == "":
            self.birthdate = ""
        else:
            self.birthdate = f"{day}-{month}-{year}"

    def create_parents(self, father, mother):
        self.father = father
        self.mother = mother



