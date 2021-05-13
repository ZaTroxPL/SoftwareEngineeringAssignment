import os.path
import json


class Setting:

    def __init__(self, setting_file_location):

        # error handling
        assert (os.path.isfile(setting_file_location)), "Specified file doesn't exist."

        with open(setting_file_location, "r") as json_file:
            json_loaded_file = (json.load(json_file))

            command_names = json_loaded_file["command_names"]

            # sanitize the setting file by converting everything to str()
            for command in command_names:
                command_names[command] = str(command_names[command]).strip().lower()

            self.command_names = command_names

            data_fields = json_loaded_file["display_data_fields"]

            # sanitize the setting file by converting everything to str()
            for i in range(0, len(data_fields)):
                data_fields[i] = str(data_fields[i]).strip()

            self.display_data_fields = data_fields

            # sanitize the setting by converting to str()
            self.file_location = str(json_loaded_file["file_location"])
