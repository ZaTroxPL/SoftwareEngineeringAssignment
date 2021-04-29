import csv


def check_record_exists(id):
    return False


def remove_record(user_input):

    # extract id from the user input
    id = str(user_input).split("remove ")[1].strip()

    # check if the record with provided id exists
    exists = check_record_exists(id)

    if not exists:
        print(f"record with the id of '{id}' doesn't exists")
        return
    # make sure user wants to remove the record
    repeat_confirmation = True

    while repeat_confirmation:
        remove_confirmation = input(f"Are you sure you want to remove {id} record? (y/n)\n")

        if remove_confirmation == "y":
            print("Record removed")
            repeat_confirmation = False
        elif remove_confirmation == "n":
            print("Operation aborted")
            repeat_confirmation = False
        else:
            print("command not understood, please enter 'y' for yes and 'n' for no")
