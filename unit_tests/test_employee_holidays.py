import unittest
import employee_holidays


class TestEmployeeHolidays(unittest.TestCase):

    def test_wrong_storage_file_location(self):
        # test values
        setting_file_location = "test"

        with self.assertRaises(AssertionError):
            employee_holidays.Setting(setting_file_location)


if __name__ == '__main__':
    unittest.main()
