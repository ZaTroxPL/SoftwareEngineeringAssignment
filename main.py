import app_setup
import processes


settings = app_setup.Settings("app_settings.json")

exit_application = False

welcome_section = [
    "Welcome",
    "In order to see a list of available commands, please type in 'help'"
]

for line in welcome_section:
    print(line)

while not exit_application:
    main_menu_navigation = input("user input: ").lower().strip()
    if main_menu_navigation == "exit" or main_menu_navigation == "quit":
        exit_application = True
    elif main_menu_navigation == "help":
        help_section = {
            "exit/quit": "exits the application",
            f"{settings.command_names['display_data']}": "displays a table with the most import fields",
            f"{settings.command_names['display_all_data']}": "displays a table with all of the fields",
            f"{settings.command_names['create']}": "adds new record",
            f"{settings.command_names['update']} id": "updates record that matches the id provided by the user",
            f"{settings.command_names['delete']} id": "removes record that matches the id provided by the user"
        }

        for key in help_section:
            print(f"{key:<{settings.longest_command + 5}} - {help_section[key]}")
        print("replace the 'id' with an actual id of the record you want to update/delete")
    elif main_menu_navigation == f"{settings.command_names['display_data']}":
        print("display data in the csv file")
    elif main_menu_navigation == f"{settings.command_names['display_all_data']}":
        print("display data with all fields in the csv file")
    elif main_menu_navigation == f"{settings.command_names['create']}":
        print("add new record")
    elif main_menu_navigation.startswith(f"{settings.command_names['update']}"):
        print("update selected record")
    elif main_menu_navigation.startswith(f"{settings.command_names['delete']}"):
        processes.delete_record(main_menu_navigation, settings.command_names['delete'])
    else:
        print("user input not recognised, please try again")
