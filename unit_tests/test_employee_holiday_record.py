import unittest
import datetime
import employee_holiday_record
from employee_holiday_record_exception import FieldUpdateError


class TestEmployeeHolidayRecord(unittest.TestCase):

    def test_initialisation_with_none(self):

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        # get all fields
        fields = emp_record.__dict__.keys()

        for field in fields:

            value = emp_record.__getattribute__(field)

            if field == "_initialisation_finished":
                self.assertTrue(value)
            else:
                self.assertIsNone(value)

    def test_initialisation_with_1_field_populated(self):

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(1)

        # get all fields
        fields = emp_record.__dict__.keys()

        for field in fields:

            value = emp_record.__getattribute__(field)

            if field == "_initialisation_finished":
                self.assertTrue(value)
            elif field == "_id":
                self.assertEqual(value, 1)
            else:
                self.assertIsNone(value)

    def test_set_previous_field_updates(self):

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()
        emp_record._set_previous_field_update("field_name_test", "field_value_test")

        self.assertEqual(emp_record._previous_field_update, "field_name_test")
        self.assertEqual(emp_record._previous_field_update_value, "field_value_test")

    def test_empty_record_as_dict(self):

        # expected values
        expected_dict = {
            "id": None,
            "year": None,
            "employee_id": None,
            "first_name": None,
            "last_name": None,
            "yearly_holiday_allowance": None,
            "leftover_holiday_from_previous_year": None,
            "holidays_for_this_year": None,
            "holidays_taken": None,
            "holidays_left": None,
            "email": None,
        }

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()
        emp_record_as_dict = emp_record.as_dict()

        self.assertDictEqual(expected_dict, emp_record_as_dict)

    def test_populated_record_as_dict(self):

        # expected values
        expected_dict = {
            "id": 1,
            "year": 2021,
            "employee_id": 1,
            "first_name": "test",
            "last_name": "test",
            "yearly_holiday_allowance": 20,
            "leftover_holiday_from_previous_year": 0,
            "holidays_for_this_year": 20,
            "holidays_taken": 0,
            "holidays_left": 20,
            "email": "test@test.test",
        }

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(1, 2021, 1, "test", "test", 20, 0, 20, 0, 20,
                                                                   "test@test.test")
        emp_record_as_dict = emp_record.as_dict()

        self.assertDictEqual(expected_dict, emp_record_as_dict)

    def test_populated_against_empty_record_as_dict(self):

        # expected values
        expected_dict = {
            "id": 1,
            "year": 2021,
            "employee_id": 1,
            "first_name": "test",
            "last_name": "test",
            "yearly_holiday_allowance": 20,
            "leftover_holiday_from_previous_year": 0,
            "holidays_for_this_year": 20,
            "holidays_taken": 0,
            "holidays_left": 20,
            "email": "test@test.test",
        }

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()
        emp_record_as_dict = emp_record.as_dict()

        self.assertNotEqual(expected_dict, emp_record_as_dict)

    def test_wrong_type_error(self):

        # test values
        wrong_types = [
            {}, [], True, set(), bytes()
        ]

        for wrong_type in wrong_types:
            with self.assertRaises(TypeError) as exception:
                employee_holiday_record.EmployeeHolidayRecord._parse_input_into_int(wrong_type)

            self.assertEqual(exception.exception.args[0], "Passed value is of an incompatible type")

    def test_int_parser_with_empty_string(self):
        with self.assertRaises(AssertionError) as exception:
            employee_holiday_record.EmployeeHolidayRecord._parse_input_into_int("")

        self.assertEqual(exception.exception.args[0], "Passed text is empty")

    def test_int_parser_with_non_numeric_string(self):
        with self.assertRaises(AssertionError) as exception:
            employee_holiday_record.EmployeeHolidayRecord._parse_input_into_int("test")

        self.assertEqual(exception.exception.args[0], "Passed text doesn't contain a numeric value")

    def test_set_id_field_to_sub_0_value(self):

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        with self.assertRaises(AssertionError) as exception:
            emp_record.id = -1

        self.assertEqual(exception.exception.args[0], "Passed value is below 0")

    def test_set_id_field_to_1_value(self):

        # test values
        value = 1

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()
        emp_record.id = value

        self.assertEqual(emp_record.id, value)

    def test_set_year_field_to_sub_2000_value_without_confirmation(self):

        # test values
        year = 1999

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.year = year

        self.assertEqual(exception.exception.args[0], "Passed value is below 2000")

    def test_set_year_field_to_sub_2000_value_with_confirmation(self):

        # test values
        year = 1999

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.year = year

        self.assertEqual(exception.exception.args[0], "Passed value is below 2000")

        self.assertEqual(emp_record._previous_field_update, "year")
        self.assertEqual(emp_record._previous_field_update_value, year)

        emp_record.year = year
        self.assertEqual(year, emp_record.year)

    def test_set_year_field_to_2001_value_without_confirmation(self):

        # test values
        year = 2001

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.year = year

        self.assertEqual(exception.exception.args[0], "Passed value is not the same as current year")

    def test_set_year_field_to_2001_value_with_confirmation(self):

        # test values
        year = 2001

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.year = year

        self.assertEqual(exception.exception.args[0], "Passed value is not the same as current year")

        self.assertEqual(emp_record._previous_field_update, "year")
        self.assertEqual(emp_record._previous_field_update_value, year)

        emp_record.year = year
        self.assertEqual(year, emp_record.year)

    def test_set_year_field_to_current_year_value(self):

        # test values
        value = datetime.date.today().year

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()
        emp_record.year = value

        self.assertEqual(emp_record.year, value)

    def test_set_employee_id_to_sub_0_value_without_confirmation(self):

        # test values
        employee_id = -1

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.employee_id = employee_id

        self.assertEqual(exception.exception.args[0], "Passed value is below 0")

    def test_set_employee_id_to_sub_0_value_with_confirmation(self):

        # test values
        employee_id = -1

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.employee_id = employee_id

        self.assertEqual(exception.exception.args[0], "Passed value is below 0")

        self.assertEqual(emp_record._previous_field_update, "employee_id")
        self.assertEqual(emp_record._previous_field_update_value, employee_id)

        emp_record.employee_id = employee_id
        self.assertEqual(employee_id, emp_record.employee_id)

    def test_set_yearly_holiday_allowance_to_above_30(self):

        # test values
        yearly_holiday_allowance = 31

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.yearly_holiday_allowance = yearly_holiday_allowance

        self.assertEqual(exception.exception.args[0], "Passed value is above 30")

    def test_set_yearly_holiday_allowance_to_25(self):

        # test values
        yearly_holiday_allowance = 25

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        emp_record.yearly_holiday_allowance = yearly_holiday_allowance

        self.assertEqual(emp_record.yearly_holiday_allowance, yearly_holiday_allowance)

    def test_set_yearly_holiday_allowance_to_below_20(self):

        # test values
        yearly_holiday_allowance = 19

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord()

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.yearly_holiday_allowance = yearly_holiday_allowance

        self.assertEqual(exception.exception.args[0], "Passed value is below 20")

    def test_set_leftover_holiday_from_previous_year_field_to_above_yearly_holiday_allowance_field(self):

        # test values
        yearly_holiday_allowance = 20
        leftover_holiday_from_previous_year = 21

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(None, None, None, None, None,
                                                                   yearly_holiday_allowance)

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.leftover_holiday_from_previous_year = leftover_holiday_from_previous_year

        self.assertEqual(exception.exception.args[0], "Passed value is above yearly_holiday_allowance")

    def test_set_leftover_holiday_from_previous_year_field_to_below_yearly_holiday_allowance(self):

        # test values
        yearly_holiday_allowance = 20
        leftover_holiday_from_previous_year = 19

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(None, None, None, None, None,
                                                                   yearly_holiday_allowance)

        emp_record.leftover_holiday_from_previous_year = leftover_holiday_from_previous_year

        self.assertEqual(emp_record.leftover_holiday_from_previous_year, leftover_holiday_from_previous_year)

    def test_set_holidays_for_this_year_to_not_sum_of_allowance_and_previous_year_fields(self):

        # test values
        yearly_holiday_allowance = 20
        leftover_holiday_from_previous_year = 5
        holidays_for_this_year = 15

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(None, None, None, None, None,
                                                                   yearly_holiday_allowance,
                                                                   leftover_holiday_from_previous_year)

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.holidays_for_this_year = holidays_for_this_year

        self.assertEqual(exception.exception.args[0], "Passed value is not equal to the sum of "
                                                      "\"yearly_holiday_allowance\" and "
                                                      "\"leftover_holiday_from_previous_year\" fields")

    def test_set_holidays_for_this_year_to_sum_of_allowance_and_previous_year_fields(self):

        # test values
        yearly_holiday_allowance = 20
        leftover_holiday_from_previous_year = 5
        holidays_for_this_year = 25

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(None, None, None, None, None,
                                                                   yearly_holiday_allowance,
                                                                   leftover_holiday_from_previous_year)

        emp_record.holidays_for_this_year = holidays_for_this_year

        self.assertEqual(emp_record.holidays_for_this_year, holidays_for_this_year)

    def test_set_holidays_taken_field_to_above_holidays_for_this_year(self):

        # test values
        holidays_taken = 30

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(None, None, None, None, None, 20, 5, 25)

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.holidays_taken = holidays_taken

        self.assertEqual(exception.exception.args[0], "Passed value is above holidays_for_this_year")

    def test_set_holidays_taken_field(self):

        # test values
        holidays_taken = 20

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(None, None, None, None, None, 20, 5, 25)
        emp_record.holidays_taken = holidays_taken

        self.assertEqual(emp_record.holidays_taken, holidays_taken)

    def test_set_holidays_left_to_above_difference_between_holidays_for_this_year_and_holidays_taken(self):

        # test values
        holidays_for_this_year = 25
        holidays_taken = 20
        holidays_left = 10

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(None, None, None, None, None, 20, 5,
                                                                   holidays_for_this_year, holidays_taken)

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.holidays_left = holidays_left

        self.assertEqual(exception.exception.args[0], "Passed value is above the difference between "
                                                      "\"holidays_for_this_year\" and \"holidays_taken\"")

    def test_set_holidays_left_to_below_difference_between_holidays_for_this_year_and_holidays_taken(self):

        # test values
        holidays_for_this_year = 25
        holidays_taken = 20
        holidays_left = 1

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(None, None, None, None, None, 20, 5,
                                                                   holidays_for_this_year, holidays_taken)

        with self.assertRaises(FieldUpdateError) as exception:
            emp_record.holidays_left = holidays_left

        self.assertEqual(exception.exception.args[0], "Passed value is below the difference between "
                                                      "\"holidays_for_this_year\" and \"holidays_taken\"")

    def test_set_holidays_left_to_difference_between_holidays_for_this_year_and_holidays_taken(self):

        # test values
        holidays_for_this_year = 25
        holidays_taken = 20
        holidays_left = 5

        # actual values
        emp_record = employee_holiday_record.EmployeeHolidayRecord(None, None, None, None, None, 20, 5,
                                                                   holidays_for_this_year, holidays_taken)
        emp_record.holidays_left = holidays_left

        self.assertEqual(emp_record.holidays_left, holidays_left)
