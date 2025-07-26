class FamilyTree:

    def __init__(self):
        self.name = ""
        self.birthdate = ""
        self.father = ""
        self.mother = ""

    def person_name(self, name):
        self.name = name

    def person_birthdate(self, birthdate):
        self.birthdate = birthdate

    def create_parents(self, father, mother):
        self.father = father
        self.mother = mother



