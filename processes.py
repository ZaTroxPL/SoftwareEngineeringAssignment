import csv


def check_record_exists(user_input, command_name):

    # extract id from the user input
    id = str(user_input).split(f"{command_name}")[1].strip()

    # open csv file with just read permissions
    with open("employee_holidays.csv", "r") as csv_employee_holidays:

        csv_dictionary_reader = csv.DictReader(csv_employee_holidays)

        # loop through each record/line in the csv file to see if the record with specified id exists
        for record in csv_dictionary_reader:
            if record["id"] == id:
                return {"exists": True, "id": id}

    return {"exists": False, "id": id}


def delete_record(user_input, command_name):

    # check if the record with provided id exists
    result = check_record_exists(user_input, command_name)

    if not result["exists"]:
        print(f"record with the id of '{result['id']}' doesn't exists")
        return

    # make sure user wants to remove the record
    repeat_confirmation = True

    while repeat_confirmation:
        remove_confirmation = input(f"Are you sure you want to remove {result['id']} record? (y/n)\n")

        if remove_confirmation == "y":
            print("Record removed")
            repeat_confirmation = False
        elif remove_confirmation == "n":
            print("Operation aborted")
            repeat_confirmation = False
        else:
            print("command not understood, please enter 'y' for yes and 'n' for no")
