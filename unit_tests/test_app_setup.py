import unittest
import app_setup


class TestAppSetup(unittest.TestCase):

    def setUp(self):
        self.expected_setting = {
            "command_names": {
                "display_data": "data",
                "display_all_data": "all data",
                "create": "create",
                "update": "update",
                "delete": "delete"
            },
            "display_data_fields": [
                "id",
                "year",
                "first_name",
                "holidays_left",
                "email"
            ],
            "file_location": "employee_holidays.csv"
        }

        self.actual_setting = app_setup.Setting("../app_settings.json")

    def test_command_names_type_setting(self):
        # expected results
        expected_setting = self.expected_setting

        # actual results
        actual_setting = self.actual_setting

        # comparison
        self.assertEqual(
            type(expected_setting["command_names"]),
            type(actual_setting.command_names)
        )

    def test_command_names_key_value_types_setting(self):
        # expected results
        expected_setting = self.expected_setting

        # actual results
        actual_setting = self.actual_setting

        # comparisons
        self.assertEqual(
            type(expected_setting["command_names"]["display_data"]),
            type(actual_setting.command_names["display_data"])
        )

        self.assertEqual(
            type(expected_setting["command_names"]["display_all_data"]),
            type(actual_setting.command_names["display_all_data"])
        )

        self.assertEqual(
            type(expected_setting["command_names"]["create"]),
            type(actual_setting.command_names["create"])
        )

        self.assertEqual(
            type(expected_setting["command_names"]["update"]),
            type(actual_setting.command_names["update"])
        )

        self.assertEqual(
            type(expected_setting["command_names"]["delete"]),
            type(actual_setting.command_names["delete"])
        )

    def test_display_data_fields_type_setting(self):
        # expected results
        expected_setting = self.expected_setting

        # actual results
        actual_setting = self.actual_setting

        # comparison
        self.assertEqual(
            type(expected_setting["display_data_fields"]),
            type(actual_setting.display_data_fields)
        )

    def test_file_location_type_setting(self):
        # expected results
        expected_setting = self.expected_setting

        # actual results
        actual_setting = self.actual_setting

        # comparison
        self.assertEqual(
            type(expected_setting["file_location"]),
            type(actual_setting.file_location)
        )

    def test_wrong_setting_file_location(self):
        # test values
        setting_file_location = "test"

        with self.assertRaises(AssertionError):
            app_setup.Setting(setting_file_location)


if __name__ == '__main__':
    unittest.main()
