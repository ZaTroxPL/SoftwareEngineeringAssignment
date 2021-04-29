import Processes

exit_application = False

print("Welcome")
print("In order to view stored data, type in 'display data' command,\n" +
      "if you wish to see a more detailed view, type in 'display detailed data'")

while not exit_application:
    main_menu_navigation = input("user input: ").lower()
    if main_menu_navigation == "exit" or main_menu_navigation == "quit":
        exit_application = True
    elif main_menu_navigation == "display data":
        print("display data in the csv file")
    elif main_menu_navigation == "display detailed data":
        print("display data with all fields in the csv file")
    elif main_menu_navigation.startswith("update "):
        print("update selected record")
    elif main_menu_navigation == "add new record":
        print("add new record")
    elif main_menu_navigation.startswith("remove "):
        Processes.remove_record(main_menu_navigation)
    else:
        print("user input not recognised, please try again")