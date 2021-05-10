import csv


class EmployeeHolidays:

    def __init__(self, file_location):
        self.file_location = file_location
        with open(file_location, "r", newline="") as csv_read_employee_holidays:
            self.set_field_names(csv_read_employee_holidays)
            self.set_records_and_ids(csv_read_employee_holidays)

    def _set_field_names(self, file):
        fieldnames = file.readline().split(",")
        for value in range(0, len(fieldnames)):
            fieldnames[value] = fieldnames[value].strip()
        self.fieldnames = fieldnames
        # reset the file to it's original position
        file.seek(0)

    def _set_records_and_ids(self, csv_read_employee_holidays):

        csv_dictionary_reader = csv.DictReader(csv_read_employee_holidays)
        records = list()
        ids = set()

        for record in csv_dictionary_reader:
            assert("id" in record), "'id' field doesn't exists in the provided csv file"
            records.append(record)
            ids.add(record["id"])

        assert(len(records) == len(ids)), "There are duplicate ids"

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

    def display_table(self, display_data_fields, display_specific_records=[]):

        fieldnames = self.fieldnames
        records = self.records
        if len(display_specific_records) > 0:
            records = [record for record in records if record["id"] in display_specific_records]

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

        self.records.append(record)
        self.overwrite_file()

    def update_record(self, user_input, command_name):

        # check if the record with provided id exists
        result = self.check_record_exists(user_input, command_name)

        if not result["exists"]:
            print(f"record with the id of '{result['id']}' doesn't exists")
            return

        # search for a record with the same id as in the result object, take the 1st time in the list
        record_to_update = [record for record in self.records if record["id"] == result["id"]][0]
        self.display_table(self.fieldnames, [record_to_update["id"]])

        stop_updating = False

        while not stop_updating:
            update_menu_navigation = input("Please insert the name of the field you want to update, " +
                                           "once you feel like you are done with your changes, type 'done'")


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


"""
hol = EmployeeHolidays("employee_holidays.csv")
print(hol.records)
print(hol.ids)
"""