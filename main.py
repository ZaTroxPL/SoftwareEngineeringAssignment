import app_setup
import employee_holidays


# make sure that this runs only as a main
if __name__ == "__main__":
    setting = app_setup.Setting("app_settings.json")
    employee_holidays = employee_holidays.EmployeeHolidays(setting.file_location, setting.table_sorting)

    # text is in a list to make the code more readable
    welcome_section = [
        "Welcome",
        "In order to see a list of available commands, please type in 'help'"
    ]

    for line in welcome_section:
        print(line)

    # loop exit condition
    exit_application = False

    while not exit_application:
        # making user input case insensitive and removing spaces at the start and end of a string
        main_menu_navigation = input("User Input: ").lower().strip()
        if main_menu_navigation == "exit" or main_menu_navigation == "quit":
            exit_application = True

        elif main_menu_navigation == "help":
            help_section = [
                ["exit/quit", "exits the application"],
                ["reload settings", "reloads the app_settings.json file into the app"],
                [f"{setting.command_names['display_data']}", "displays a table with the most import fields"],
                [f"{setting.command_names['display_all_data']}", "displays a table with all of the fields"],
                [f"{setting.command_names['create']}", "adds new record"],
                [f"{setting.command_names['update']} id", "updates record that matches the id provided by the user"],
                [f"{setting.command_names['delete']} id", "removes record that matches the id provided by the user"],
                "replace the 'id' with an actual id of the record you want to update/delete"
            ]

            longest_command = 0

            # assign longest_command
            for line in help_section:
                # check if line is a list
                if type(line) == type(help_section):
                    if len(line[0]) > longest_command:
                        longest_command = len(line[0])

            # print out the help_section
            for line in help_section:
                # check if line is a list
                if type(line) == type(help_section):
                    print(f"{line[0]:<{longest_command + 3}} - {line[1]}")
                else:
                    print(line)

        elif main_menu_navigation == "reload settings":
            setting = app_setup.Setting("app_settings.json")
            print("settings have been reloaded")

        elif main_menu_navigation == f"{setting.command_names['display_data']}":
            employee_holidays.display_table(setting.display_data_fields)

        elif main_menu_navigation == f"{setting.command_names['display_all_data']}":
            employee_holidays.display_table(employee_holidays.fieldnames)

        elif main_menu_navigation == f"{setting.command_names['create']}":
            employee_holidays.create_record()

        elif main_menu_navigation.startswith(f"{setting.command_names['update']}"):
            employee_holidays.update_record(main_menu_navigation, setting.command_names['update'])

        elif main_menu_navigation.startswith(f"{setting.command_names['delete']}"):
            employee_holidays.delete_confirmation(main_menu_navigation, setting.command_names['delete'])

        else:
            print("user input not recognised, please try again or type 'help' to see a list of available commands")
