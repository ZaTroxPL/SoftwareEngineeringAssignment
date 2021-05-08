import app_setup
import processes


settings = app_setup.Settings("app_settings.json")

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

        # get longest command
        longest_command = 0

        for line in help_section:
            # check if the line is a list
            if type(line) == type(help_section):
                if len(line[0]) > longest_command:
                    longest_command = len(line[0])

        for line in help_section:
            # check if the line is a list
            if type(line) == type(help_section):
                print(f"{line[0]:<{longest_command + 3}} - {line[1]}")
            else:
                print(line)

    elif main_menu_navigation == "reload settings":
        settings = app_setup.Settings("app_settings.json")
        print("settings have been reloaded")

    elif main_menu_navigation == f"{settings.command_names['display_data']}":
        processes.display_table(settings.display_data_fields)

    elif main_menu_navigation == f"{settings.command_names['display_all_data']}":
        processes.display_full_table()

    elif main_menu_navigation == f"{settings.command_names['create']}":
        print("add new record")

    elif main_menu_navigation.startswith(f"{settings.command_names['update']}"):
        print("update selected record")

    elif main_menu_navigation.startswith(f"{settings.command_names['delete']}"):
        processes.delete_process(main_menu_navigation, settings.command_names['delete'])

    else:
        print("user input not recognised, please try again or type 'help' to see a list of available commands")
