from create_person import Person
from tree_image import image


def options():
    while True:
        try:
            choice = int(input("[1] Add Name\n"
                           "[2] Find Name\n"
                           "[3] Delete Name\n"))
            if choice in [1,2,3]:
                return choice
            else:
                print("Invalid choice. Input should be 1-3 only.")
        except ValueError:
            print("Invalid choice. Input should be 1-3 only.")

def add_name():
    person = Person()
    person.create_person()
    save_or_not = input("Do you want to save this information? (Y/N): ")

    if save_or_not.lower() == "y":
        person.save_data()
        print("Data was saved.")
    else:
        print("Data was not saved.")

def search_name():
    person = Person()
    person.search_person(del_flag=False)

def delete_person():
    person = Person()
    found = person.search_person(del_flag=True)
    if found:
        del_or_not = input("Do you want to delete this details? (Y/N): ")

        if del_or_not.lower() == "y":
            print("Data will be deleted...")
            person.delete_data()
        else:
            print("Data will not be deleted.")

def main():
    print("Welcome to SALINLAHI! Your Filipino Genealogy App")
    print(image)
    print("What do you want to do today?")
    process = True
    while process:
        choice = options()
        if choice == 1:
            add_name()
        elif choice == 2:
            search_name()
        elif choice == 3:
            delete_person()
        continue_or_not = input("Do you want to do something else? (Y/N): ")

        if continue_or_not.lower() == "n":
            process = False

if __name__ == "__main__":
    main()
