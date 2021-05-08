import json


class Settings:

    def __init__(self, setting_file_location):
        with open(setting_file_location, "r") as json_file:
            loaded_file = (json.load(json_file))

            command_names = loaded_file["command_names"]

            # sanitize the setting file by converting everything to str()
            for command in command_names:
                command_names[command] = str(command_names[command]).strip()

            self.command_names = command_names

            data_fields = loaded_file["display_data_fields"]

            # sanitize the setting file by converting everything to str()
            for i in range(0, len(data_fields)):
                data_fields[i] = str(data_fields[i]).strip()

            self.display_data_fields = data_fields
