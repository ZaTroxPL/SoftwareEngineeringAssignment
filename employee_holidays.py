import os.path
import operator
import csv


class EmployeeHolidays:

    def __init__(self, file_location, table_sorting):
        self.file_location = file_location

        # error handling
        assert(os.path.isfile(self.file_location)), "Specified file doesn't exist."

        with open(file_location, "r", newline="") as csv_read_employee_holidays:
            self._set_field_names(csv_read_employee_holidays, table_sorting)
            self._set_records_and_ids(csv_read_employee_holidays, table_sorting)
        # automatically closes the file at the end

    # following python naming convention, methods with 1 underscore at the start are supposed to be "private" methods
    # not sure whether to call the function _set_field_names or _read_field_names, same with the 1 function below
    def _set_field_names(self, csv_read_employee_holidays, table_sorting):
        fieldnames = csv_read_employee_holidays.readline().split(",")

        # strip spaces around the fieldnames
        for value in range(0, len(fieldnames)):
            fieldnames[value] = fieldnames[value].strip()

        # check if 'id' field exists
        assert ("id" in fieldnames), "'id' field doesn't exists in the provided csv file"

        # check if the sorting fields exist
        for field in table_sorting:
            assert (field in fieldnames), f"{field} field doesn't exists in the provided csv file"

        self.fieldnames = fieldnames
        # reset the file to it's original position
        csv_read_employee_holidays.seek(0)

    def _set_records_and_ids(self, csv_read_employee_holidays, table_sorting):

        csv_dictionary_reader = csv.DictReader(csv_read_employee_holidays)
        records = list()
        ids = set()

        for record in csv_dictionary_reader:
            # check if the record contains a numeric value in the id field
            assert (not record["id"].strip() == ""), "'id' field doesn't contain a value in the provided csv file"
            assert (record["id"].strip().isnumeric()), \
                "'id' field doesn't contain a numeric value in the provided csv file"

            records.append(record)
            ids.add(record["id"])

        assert(len(records) == len(ids)), "There are duplicate ids"

        # sorting the records by the setting defined table_sorting
        records.sort(key=operator.itemgetter(*table_sorting))

        self.records = records
        self.ids = ids

    def set_column_widths(self, display_data_fields):

        # create empty dictionary
        column_widths = dict()

        # populate the dictionary with the length of the field name as the default value
        for display_field in display_data_fields:
            column_widths[display_field] = len(display_field)

        # for every record in csv file
        for record in self.records:
            # for every field in a record
            for field in record:
                # check if the field is one of the selected fields
                for display_field in display_data_fields:
                    if field == display_field:
                        column_width = len(record[field])
                        # check if new width is bigger than the old one
                        if column_width > column_widths[display_field]:
                            column_widths[display_field] = column_width

        self.column_widths = column_widths

    def check_record_exists(self, user_input, command_name):

        # extract id from the user input
        record_id = str(user_input).split(f"{command_name}")[1].strip()

        if record_id in self.ids:
            return {"exists": True, "id": record_id}
        return {"exists": False, "id": record_id}

    def display_table(self, display_data_fields, table_sorting, display_specific_records=None):

        # make sure that the display_specific_records list is always empty at the start of the method
        if display_specific_records is None:
            display_specific_records = []

        fieldnames = self.fieldnames

        # sorting the records by the setting defined as table_sorting
        self.records.sort(key=operator.itemgetter(*table_sorting))
        records = self.records

        if len(display_specific_records) > 0:
            records = display_specific_records

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

        self.set_column_widths(display_data_fields)
        column_widths = self.column_widths

        table = []

        # create outline and header for the table
        outline = "+"
        header = "|"
        for column in column_widths:
            # +1 is for the + to have it's own place
            outline += f"-{'-':->{column_widths[column] + 1}}+"
            header += f" {column:^{column_widths[column]}} |"

        table.append(outline)
        table.append(header)
        table.append(outline)

        # for every record in csv file
        for record in records:
            row = "|"
            # for every selected field
            for display_field in display_data_fields:
                # for every field in a record
                for field in record:
                    # check if the field is one of the selected fields
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

    def create_record(self):

        record = dict()

        for field in self.fieldnames:
            if field == "id":
                # making sure that id is unique and that it's a string
                record[field] = str(int(max(self.ids)) + 1)
                continue
            record[field] = input(f"Please insert value for '{field}' field: ")

        print("New record has been successfully created")

        self.records.append(record)
        self.overwrite_file()

    def update_record(self, user_input, command_name, table_sorting):

        # check if the record with provided id exists
        result = self.check_record_exists(user_input, command_name)

        if not result["exists"]:
            print(f"record with the id of '{result['id']}' doesn't exists")
            return

        # create new list of records so that the self.records isn't overwritten
        records = self.records.copy()

        # search for a record with the same id as in the result object, take the 1st time in the list
        original_record = [record for record in records if record["id"] == result["id"]][0].copy()
        record_to_update = original_record.copy()
        self.display_table(self.fieldnames, table_sorting, [record_to_update])

        update_section = [
            "Please insert the name of the field you want to update.",
            "Type 'done' to save changes and come back to the main menu.",
            "You can also type in 'exit' to abort the update operation."
        ]

        for line in update_section:
            print(line)

        stop_updating = False

        while not stop_updating:
            update_menu_navigation = input("User Input: ").strip()

            if update_menu_navigation.lower() == "done":
                # get index of the original record
                index = self.records.index(original_record)
                # overwrite the original record at the specified index
                self.records[index] = record_to_update
                self.overwrite_file()
                self.display_table(self.fieldnames, table_sorting)
                stop_updating = True

            elif update_menu_navigation.lower() == "exit":
                stop_updating = True

            elif update_menu_navigation.lower() == "id":
                print("You cannot update the 'id' field")

            elif update_menu_navigation in self.fieldnames:
                record_to_update[update_menu_navigation] = input(f"{update_menu_navigation}: ")
                self.display_table(self.fieldnames, table_sorting, [record_to_update])

            else:
                print("Input not recognised, please enter 'exit' to abort the update operation,"
                      " 'done' to save the changes and exit the update operation or"
                      " enter the name of the field you want to update")

    def delete_confirmation(self, user_input, command_name):

        # check if the record with provided id exists
        result = self.check_record_exists(user_input, command_name)

        if not result["exists"]:
            print(f"record with the id of '{result['id']}' doesn't exists")
            return

        # make sure user wants to remove the record
        repeat_confirmation = True

        while repeat_confirmation:
            remove_confirmation = input(f"Are you sure you want to remove a record " +
                                        f"with the id of '{result['id']}'? (y/n)\n")

            if remove_confirmation == "y":
                # search for a record with the same id as in the result object, take the 1st time in the list
                record = [record for record in self.records if record["id"] == result["id"]][0]
                self.records.remove(record)
                self.overwrite_file()
                print("Record removed")
                repeat_confirmation = False
            elif remove_confirmation == "n":
                print("Operation aborted")
                repeat_confirmation = False
            else:
                print("command not understood, please enter 'y' for yes and 'n' for no")

    def overwrite_file(self):

        with open(self.file_location, "w", newline="") as csv_write_employee_holidays:
            csv_dictionary_writer = csv.DictWriter(csv_write_employee_holidays, self.fieldnames)

            # overwrite the file with the headers/fieldnames
            csv_dictionary_writer.writeheader()

            # overwrite the file
            csv_dictionary_writer.writerows(self.records)
