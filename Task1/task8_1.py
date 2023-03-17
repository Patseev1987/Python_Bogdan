from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def get_check(string):
    count = 0
    if string.replace(" ", "") == "":
        print("You didn't enter any information")
        return False
    for i in all_data:
        new_string = i.split()
        arrrr = ""
        for x in range(1, len(new_string)):
            arrrr += new_string[x].strip()+" "
        if string.lower().strip() == arrrr.lower().strip():
            count += 1
    if count > 0:
        print("You have this contact")
        return False
    return True


def delete_contact():
    global last_id
    show_all()
    flag_delete = True
    delete_object = ""
    while flag_delete:
        delete_object = input(
            "Enter the contact number which you want to delete: ")
        if delete_object.isdigit() and 0 < int(delete_object) <= last_id:
            flag_delete = False
        else:
            print("You entered the wrong number. Try again.")
    last_id = 1
    with open(file_base, "w", encoding="utf-8") as f:
        for i in all_data:
            if int(delete_object) != int(i.split()[0]):
                new_string = ""
                for x in range(1, len(i.split())):
                    new_string += i.split()[x]+" "
                f.write(f"{last_id} {new_string}\n")
                last_id += 1


def change_contact():
    global last_id
    point = search_before_action()
    flag_delete = True
    delete_object = ""
    while flag_delete:
        delete_object = input(
            "Enter the contact number which you want to change: ")
        if delete_object.isdigit() and delete_object.strip() in point:
            flag_delete = False
        else:
            print("You entered the wrong number. Try again.")
    last_id = 1
    array = ["surname", "name", "patronymic", "phone_number"]
    changed_string = ""
    for i in array:
        changed_string += input(f"Enter changed  {i} ") + " "
    if get_check(changed_string):
        with open(file_base, "w", encoding="utf-8") as f:
            for i in all_data:
                if int(delete_object) != int(i.split()[0]):
                    new_string = ""
                    for x in range(1, len(i.split())):
                        new_string += i.split()[x]+" "
                    f.write(f"{last_id} {new_string}\n")
                else:
                    f.write(f"{last_id} {changed_string}\n")
                last_id += 1


def search_before_action():
    count = []

    name_flag = True
    while name_flag:
        search_name = input("Enter a option for search ")
        if search_name.strip() == "":
            print("You didn't enter any information. Try again.")
        else:
            name_flag = False
        for x in all_data:
            for i in range(1, len(x.split())):
                if search_name.lower() in x.split()[i].lower():
                    print(x)
                    count.append(x.split()[0])
    count = list(set(count))
    return count


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def search_contact():
    read_records()
    search_flag = True
    while search_flag:
        answer = input("Select search option:\n"
                       "1. Surname \n"
                       "2. Name\n"
                       "3. Patonymic\n"
                       "4. Phone number\n"
                       "5. Back\n")
        match answer:
            case "1":
                search_flag = False
                name_flag = True
                while name_flag:
                    search_name = input("Enter a seurname for search ")
                    if search_name.strip() == "":
                        print("You didn't enter any information. Try again.")
                    else:
                        name_flag = False
                for x in all_data:
                    if search_name.lower() in x.split()[1].lower():
                        print(x)
            case "2":
                search_flag = False
                name_flag = True
                while name_flag:
                    search_name = input("Enter a name for search ")
                    if search_name.strip() == "":
                        print("You didn't enter any information. Try again.")
                    else:
                        name_flag = False
                for x in all_data:
                    if search_name.lower() in x.split()[2].lower():
                        print(x)
            case "3":
                search_flag = False
                name_flag = True
                while name_flag:
                    search_name = input("Enter a patronymic for search ")
                    if search_name.strip() == "":
                        print("You didn't enter any information. Try again.")
                    else:
                        name_flag = False
                for x in all_data:
                    if search_name.lower() in x.split()[3].lower():
                        print(x)
            case "4":
                search_flag = False
                name_flag = True
                while name_flag:
                    search_name = input("Enter a phone number for search ")
                    if search_name.strip() == "":
                        print("You didn't enter any information. Try again.")
                    else:
                        name_flag = False
                for x in all_data:
                    if search_name.lower() in x.split()[4].lower():
                        print(x)
            case "5":
                search_flag = False
            case _:
                print("Try again!\n")


def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        string += input(f"Enter {i} ") + " "
    last_id += 1
    if get_check(string):
        with open(file_base, "a", encoding="utf-8") as f:
            print(f"This contact was added {string}")

            f.write(f"{last_id} {string}\n")


def import_export():
    global file_base
    export_flag = True
    while export_flag:
        answer = input("Enter what you want to do:\n"
                       "1. Import base\n"
                       "2. Export base\n"
                       "3. Back\n")
        match answer:
            case "1":
                export_flag = False
                import_base_name = input(
                    "Enter a imported base without (.txt)\n")
                import_base_name = import_base_name.strip()+".txt"
                if not path.exists(import_base_name):
                    print(f"{import_base_name} isn't exist")
                else:
                    file_base = import_base_name
            case "2":
                export_flag = False
                export_name_base = input(
                    "Enter a exported name base without (.txt)\n")
                export_name_base = export_name_base.strip()+".txt"
                with open(export_name_base, "w", encoding="utf-8")as f:
                    for i in all_data:

                        f.write(i.strip()+"\n")
            case "3":
                export_flag = False
            case _:
                print("Try again!\n")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change a record\n"
                       "5. Delete a record\n"
                       "6. Exp/Imp a base\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                change_contact()
            case "5":
                delete_contact()
            case "6":
                import_export()
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()
