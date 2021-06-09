import unittest
import employee_holiday_table


class TestEmployeeHolidayTable(unittest.TestCase):

    def test_wrong_storage_file_location(self):
        # test values
        storage_file_location = "test"

        with self.assertRaises(AssertionError):
            employee_holiday_table.EmployeeHolidayTable(storage_file_location, ["id"])

    def test_table_without_id_field(self):
        # test values
        storage_file_location = "test_employee_holidays_csv_files/no_id.csv"

        with self.assertRaises(AssertionError):
            employee_holiday_table.EmployeeHolidayTable(storage_file_location, ["year"])

    def test_sort_by_non_existent_field(self):
        # test values
        storage_file_location = "../employee_holidays.csv"

        with self.assertRaises(AssertionError):
            employee_holiday_table.EmployeeHolidayTable(storage_file_location, ["test"])

    def test_no_id_value(self):
        # test values
        storage_file_location = "test_employee_holidays_csv_files/no_id_value.csv"

        with self.assertRaises(AssertionError):
            employee_holiday_table.EmployeeHolidayTable(storage_file_location, ["id"])

    def test_non_numeric_id_value(self):
        # test values
        storage_file_location = "test_employee_holidays_csv_files/non_numeric_id_value.csv"

        with self.assertRaises(AssertionError):
            employee_holiday_table.EmployeeHolidayTable(storage_file_location, ["id"])

    def test_duplicate_ids(self):
        # test values
        storage_file_location = "test_employee_holidays_csv_files/duplicate_ids.csv"

        with self.assertRaises(AssertionError):
            employee_holiday_table.EmployeeHolidayTable(storage_file_location, ["id"])

    def test_column_widths(self):
        # test values
        storage_file_location = "test_employee_holidays_csv_files/column_widths.csv"

        # expected values
        expected_column_widths = {
            "id": 2,
            "year": 4,
            "employee_id": 11,
            "first_name": 10,
            "last_name": 9
        }

        # actual values
        emp = employee_holiday_table.EmployeeHolidayTable(storage_file_location, ["id"])
        emp.set_column_widths(["id", "year", "employee_id", "first_name", "last_name"])
        actual_column_widths = emp.column_widths

        self.assertDictEqual(expected_column_widths, actual_column_widths)

    def test_record_exists(self):
        # test values
        storage_file_location = "test_employee_holidays_csv_files/check_record_exists.csv"

        # expected values
        expected_return_value = {"exists": True, "id": 1}

        # actual values
        emp = employee_holiday_table.EmployeeHolidayTable(storage_file_location, ["id"])
        actual_return_value = emp.check_record_exists("check 1", "check")

        self.assertEqual(expected_return_value, actual_return_value)

    def test_record_does_not_exists(self):
        # test values
        storage_file_location = "test_employee_holidays_csv_files/check_record_exists.csv"

        # expected values
        expected_return_value = {"exists": False, "id": 123}

        # actual values
        emp = employee_holiday_table.EmployeeHolidayTable(storage_file_location, ["id"])
        actual_return_value = emp.check_record_exists("check 123", "check")

        self.assertEqual(expected_return_value, actual_return_value)


if __name__ == '__main__':
    unittest.main()
