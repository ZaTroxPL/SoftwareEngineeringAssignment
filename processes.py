import csv


def check_record_exists(user_input, command_name):

    # extract id from the user input
    record_id = str(user_input).split(f"{command_name}")[1].strip()

    # open csv file with just read permissions
    with open("employee_holidays.csv", "r", newline="") as csv_read_employee_holidays:

        csv_dictionary_reader = csv.DictReader(csv_read_employee_holidays)

        # loop through each record/line in the csv file to see if the record with specified id exists
        for record in csv_dictionary_reader:
            if record["id"] == record_id:
                return {"exists": True, "id": record_id}

    return {"exists": False, "id": record_id}


def get_field_names():
    with open("employee_holidays.csv", "r", newline="") as file_read_employee_holidays:
        fieldnames = file_read_employee_holidays.readline().split(",")
        for value in range(0, len(fieldnames)):
            fieldnames[value] = fieldnames[value].strip()
        return fieldnames


def get_column_widths(display_data_fields):

    # create empty dictionary
    column_widths = dict()

    # populate the dictionary with the length of the field name as the default value
    for display_field in display_data_fields:
        column_widths[display_field] = len(display_field)

    with open("employee_holidays.csv", "r", newline="") as csv_read_employee_holidays:
        csv_dictionary_reader = csv.DictReader(csv_read_employee_holidays)

        # for every record in csv file
        for record in csv_dictionary_reader:
            # for every field in a record
            for field in record:
                # check if the field is one of the selected fields
                for display_field in display_data_fields:
                    if field == display_field:
                        column_width = len(record[field])
                        # check if new width is bigger than the old one
                        if column_width > column_widths[display_field]:
                            column_widths[display_field] = column_width

    return column_widths


def display_table(display_data_fields):

    fieldnames = get_field_names()

    # making sure all provided fields exist
    for field in display_data_fields:
        match_found = False
        for table_name in fieldnames:
            if field == table_name:
                match_found = True
                break

        if not match_found:
            print(f"field '{field}' couldn't be matched to any existing fields, aborting this operation")
            return

    column_widths = get_column_widths(display_data_fields)

    table = []

    # create outline and header for the table
    outline = "+"
    header_fieldnames = "|"
    for column in column_widths:
        # +1 is for the + to have it's own place
        outline += f"-{'-':->{column_widths[column] + 1}}+"
        header_fieldnames += f" {column:^{column_widths[column]}} |"

    table.append(outline)
    table.append(header_fieldnames)
    table.append(outline)

    # create rows for the table
    with open("employee_holidays.csv", "r", newline="") as csv_read_employee_holidays:
        csv_dictionary_reader = csv.DictReader(csv_read_employee_holidays)

        # for every record in csv file
        for record in csv_dictionary_reader:
            row = "|"
            # for every field in a record
            for field in record:
                # check if the field is one of the selected fields
                for display_field in display_data_fields:
                    if field == display_field:
                        # check if value is a number, if so right align, otherwise left align
                        if record[field].isnumeric():
                            row += f" {record[field]:>{column_widths[display_field]}} |"
                        else:
                            row += f" {record[field]:<{column_widths[display_field]}} |"
            table.append(row)

    table.append(outline)

    for line in table:
        print(line)


def display_full_table():

    fieldnames = get_field_names()
    display_table(fieldnames)


def delete_process(user_input, command_name):

    # check if the record with provided id exists
    result = check_record_exists(user_input, command_name)

    if not result["exists"]:
        print(f"record with the id of '{result['id']}' doesn't exists")
        return

    # make sure user wants to remove the record
    repeat_confirmation = True

    while repeat_confirmation:
        remove_confirmation = input(f"Are you sure you want to remove record with the id of '{result['id']}'? (y/n)\n")

        if remove_confirmation == "y":
            delete_record(result["id"])
            print("Record removed")
            repeat_confirmation = False
        elif remove_confirmation == "n":
            print("Operation aborted")
            repeat_confirmation = False
        else:
            print("command not understood, please enter 'y' for yes and 'n' for no")


def delete_record(record_id):

    # create empty list for records and get field names
    records = []
    fieldnames = get_field_names()

    # open file in read only mode
    with open("employee_holidays.csv", "r", newline="") as csv_read_employee_holidays:
        csv_dictionary_reader = csv.DictReader(csv_read_employee_holidays)

        for record in csv_dictionary_reader:
            if record["id"] != record_id:
                records.append(record)

    with open("employee_holidays.csv", "w", newline="") as csv_write_employee_holidays:
        csv_dictionary_writer = csv.DictWriter(csv_write_employee_holidays, fieldnames)

        # overwrite the file with the headers
        csv_dictionary_writer.writeheader()

        # overwrite the file
        csv_dictionary_writer.writerows(records)
