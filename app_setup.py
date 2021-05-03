import json


class Settings:

    def __init__(self, setting_file_location):
        with open(setting_file_location, "r") as json_file:
            self.command_names = (json.load(json_file))["command_names"]

        longest_command = 0

        for command in self.command_names:
            if len(self.command_names[command]) > longest_command:
                longest_command = len(self.command_names[command])

        self.longest_command = longest_command
