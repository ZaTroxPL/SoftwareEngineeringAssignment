import app_setup
import employee_holidays


settings = app_setup.Settings("app_settings.json")
employee_holidays = employee_holidays.EmployeeHolidays("employee_holidays.csv")

welcome_section = [
    "Welcome",
    "In order to see a list of available commands, please type in 'help'"
]

for line in welcome_section:
    print(line)

exit_application = False

while not exit_application:
    main_menu_navigation = input("user input: ").lower().strip()
    if main_menu_navigation == "exit" or main_menu_navigation == "quit":
        exit_application = True

    elif main_menu_navigation == "help":
        help_section = [
            ["exit/quit", "exits the application"],
            ["reload settings", "reloads the app_settings.json file into the app"],
            [f"{settings.command_names['display_data']}", "displays a table with the most import fields"],
            [f"{settings.command_names['display_all_data']}", "displays a table with all of the fields"],
            [f"{settings.command_names['create']}", "adds new record"],
            [f"{settings.command_names['update']} id", "updates record that matches the id provided by the user"],
            [f"{settings.command_names['delete']} id", "removes record that matches the id provided by the user"],
            "replace the 'id' with an actual id of the record you want to update/delete"
        ]

        longest_command = 0

        for line in help_section:
            # check if line is a list
            if type(line) == type(help_section):
                if len(line[0]) > longest_command:
                    longest_command = len(line[0])

        for line in help_section:
            # check if line is a list
            if type(line) == type(help_section):
                print(f"{line[0]:<{longest_command + 3}} - {line[1]}")
            else:
                print(line)

    elif main_menu_navigation == "reload settings":
        settings = app_setup.Settings("app_settings.json")
        print("settings have been reloaded")

    elif main_menu_navigation == f"{settings.command_names['display_data']}":
        employee_holidays.display_table(settings.display_data_fields)

    elif main_menu_navigation == f"{settings.command_names['display_all_data']}":
        employee_holidays.display_table(employee_holidays.fieldnames)

    elif main_menu_navigation == f"{settings.command_names['create']}":
        employee_holidays.create_record()

    elif main_menu_navigation.startswith(f"{settings.command_names['update']}"):
        employee_holidays.update_record(main_menu_navigation, settings.command_names['update'])

    elif main_menu_navigation.startswith(f"{settings.command_names['delete']}"):
        employee_holidays.delete_confirmation(main_menu_navigation, settings.command_names['delete'])

    else:
        print("user input not recognised, please try again or type 'help' to see a list of available commands")
