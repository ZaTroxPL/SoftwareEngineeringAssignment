import datetime
from employee_holiday_record_exception import FieldUpdateError


class EmployeeHolidayRecord:

    def __init__(self, id=None, year=None, employee_id=None, first_name=None, last_name=None,
                 yearly_holiday_allowance=None, leftover_holiday_from_previous_year=None, holidays_for_this_year=None,
                 holidays_taken=None, holidays_left=None, email=None):
        # Used to make sure that setters work properly during initialisation of records from the csv file
        self._initialisation_finished = False

        # setting properties
        self.id = id
        self.year = year
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.yearly_holiday_allowance = yearly_holiday_allowance
        self.leftover_holiday_from_previous_year = leftover_holiday_from_previous_year
        self.holidays_for_this_year = holidays_for_this_year
        self.holidays_taken = holidays_taken
        self.holidays_left = holidays_left
        self.email = email

        self._initialisation_finished = True
        self._set_previous_field_updates(None, None)

    def _set_previous_field_updates(self, field_name, value):
        # this is used as confirmation when user wants to input questionable but allowed data values
        self._previous_field_update = field_name
        self._previous_field_update_value = value

    def as_dict(self):
        return \
            {
                "id": self.id,
                "year": self.year,
                "employee_id": self.employee_id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "yearly_holiday_allowance": self.yearly_holiday_allowance,
                "leftover_holiday_from_previous_year": self.leftover_holiday_from_previous_year,
                "holidays_for_this_year": self.holidays_for_this_year,
                "holidays_taken": self.holidays_taken,
                "holidays_left": self.holidays_left,
                "email": self.email
            }

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if type(value) != str and type(value) != int and value is not None:
            raise TypeError("Passed value is of an incompatible type")

        if value is None:
            self._id = None
            return
        elif type(value) == str:
            # check if the value contains a numeric value in the id field and check if the value is below 0
            assert (not value.strip() == ""), "'id' field doesn't contain a value"
            assert (value.strip().isnumeric()), "'id' field doesn't contain a numeric value"

        # at this point, only ints and strings that can be converted into an int should be left
        value = int(value)

        assert (value >= 0), "Passed value is below 0"
        self._id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if type(value) != str and type(value) != int and value is not None:
            raise TypeError("Passed value is of an incompatible type")

        if value is None:
            self._year = None
            return
        elif type(value) == str:
            # check if the value contains a numeric value in the id field and check if the value is below 0
            assert (not value.strip() == ""), "'year' field doesn't contain a value"
            assert (value.strip().isnumeric()), "'year' field doesn't contain a numeric value"

        # at this point, only ints and strings that can be converted into an int should be left

        value = int(value)

        if self._initialisation_finished:
            # try catch will take care of handling those errors and asking user for confirmation
            if self._previous_field_update != "year" or self._previous_field_update_value != value:
                self._set_previous_field_updates("year", value)
                if value <= 2000:
                    raise FieldUpdateError("Passed value is below 2000")
                elif value != datetime.date.today().year:
                    raise FieldUpdateError("Passed value is not the same as current year")

        self._year = value

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        if type(value) != str and type(value) != int and value is not None:
            raise TypeError("Passed value is of an incompatible type")

        if value is None:
            self._employee_id = None
            return
        elif type(value) == str:
            # check if the value contains a numeric value in the id field and check if the value is below 0
            assert (not value.strip() == ""), "'employee_id' field doesn't contain a value"
            assert (value.strip().isnumeric()), "'employee_id' field doesn't contain a numeric value"

        # at this point, only ints and strings that can be converted into an int should be left
        value = int(value)

        if self._initialisation_finished:
            # try catch will take care of handling those errors and asking user for confirmation
            if self._previous_field_update != "employee_id" or self._previous_field_update_value != value:
                self._set_previous_field_updates("employee_id", value)
                if value <= 0:
                    raise FieldUpdateError("Passed value is below 0")

        assert (value >= 0), "Passed value is below 0"
        self._employee_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._set_previous_field_updates("first_name", value)
        self._first_name = str(value)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._set_previous_field_updates("last_name", value)
        self._last_name = str(value)

    @property
    def yearly_holiday_allowance(self):
        return self._yearly_holiday_allowance

    @yearly_holiday_allowance.setter
    def yearly_holiday_allowance(self, value):
        if type(value) != str and type(value) != int and value is not None:
            raise TypeError("Passed value is of an incompatible type")

        if value is None:
            self._yearly_holiday_allowance = None
            return
        elif type(value) == str:
            # check if the value contains a numeric value in the id field and check if the value is below 0
            assert (not value.strip() == ""), "'yearly_holiday_allowance' field doesn't contain a value"
            assert (value.strip().isnumeric()), "'yearly_holiday_allowance' field doesn't contain a numeric value"

        # at this point, only ints and strings that can be converted into an int should be left
        value = int(value)

        if self._initialisation_finished:
            # try catch will take care of handling those errors and asking user for confirmation
            if self._previous_field_update != "yearly_holiday_allowance" or self._previous_field_update_value != value:
                self._set_previous_field_updates("yearly_holiday_allowance", value)
                if value <= 20:
                    raise FieldUpdateError("Passed value is below 20")
                elif value > 30:
                    raise FieldUpdateError("Passed value is above 30")

        assert (value >= 0), "Passed value is below 0"
        self._yearly_holiday_allowance = value

    @property
    def leftover_holiday_from_previous_year(self):
        return self._leftover_holiday_from_previous_year

    @leftover_holiday_from_previous_year.setter
    def leftover_holiday_from_previous_year(self, value):
        if type(value) != str and type(value) != int and value is not None:
            raise TypeError("Passed value is of an incompatible type")

        if value is None:
            self._leftover_holiday_from_previous_year = None
            return
        elif type(value) == str:
            # check if the value contains a numeric value in the id field and check if the value is below 0
            assert (not value.strip() == ""), "'leftover_holiday_from_previous_year' field doesn't contain a value"
            assert (value.strip().isnumeric()), \
                "'leftover_holiday_from_previous_year' field doesn't contain a numeric value"

        # at this point, only ints and strings that can be converted into an int should be left
        value = int(value)

        if self._initialisation_finished:
            # try catch will take care of handling those errors and asking user for confirmation
            if self._previous_field_update != "leftover_holiday_from_previous_year" or self._previous_field_update_value != value:
                self._set_previous_field_updates("leftover_holiday_from_previous_year", value)
                if value > self.yearly_holiday_allowance:
                    raise FieldUpdateError("Passed value is above yearly_holiday_allowance")
                elif value < 0:
                    raise FieldUpdateError("Passed value is below 0")

        assert (value >= 0), "Passed value is below 0"
        self._leftover_holiday_from_previous_year = value

    @property
    def holidays_for_this_year(self):
        return self._holidays_for_this_year

    @holidays_for_this_year.setter
    def holidays_for_this_year(self, value):
        if type(value) != str and type(value) != int and value is not None:
            raise TypeError("Passed value is of an incompatible type")

        if value is None:
            self._holidays_for_this_year = None
            return
        elif type(value) == str:
            # check if the value contains a numeric value in the id field and check if the value is below 0
            assert (not value.strip() == ""), "'holidays_for_this_year' field doesn't contain a value"
            assert (value.strip().isnumeric()), "'holidays_for_this_year' field doesn't contain a numeric value"

        # at this point, only ints and strings that can be converted into an int should be left
        value = int(value)

        if self._initialisation_finished:
            # try catch will take care of handling those errors and asking user for confirmation
            if self._previous_field_update != "holidays_for_this_year" or self._previous_field_update_value != value:
                self._set_previous_field_updates("holidays_for_this_year", value)
                if value != (self.yearly_holiday_allowance + self.leftover_holiday_from_previous_year):
                    raise FieldUpdateError("Passed value is not equal to the sum of \"yearly_holiday_allowance\" and "
                                           "\"leftover_holiday_from_previous_year\" fields")

        assert (value >= 0), "Passed value is below 0"
        self._holidays_for_this_year = value

    @property
    def holidays_taken(self):
        return self._holidays_taken

    @holidays_taken.setter
    def holidays_taken(self, value):
        if type(value) != str and type(value) != int and value is not None:
            raise TypeError("Passed value is of an incompatible type")

        if value is None:
            self._holidays_taken = None
            return
        elif type(value) == str:
            # check if the value contains a numeric value in the id field and check if the value is below 0
            assert (not value.strip() == ""), "'holidays_taken' field doesn't contain a value"
            assert (value.strip().isnumeric()), "'holidays_taken' field doesn't contain a numeric value"

        # at this point, only ints and strings that can be converted into an int should be left
        value = int(value)

        if self._initialisation_finished:
            # try catch will take care of handling those errors and asking user for confirmation
            if self._previous_field_update != "holidays_taken" or self._previous_field_update_value != value:
                self._set_previous_field_updates("holidays_taken", value)
                if value > self.holidays_for_this_year:
                    raise FieldUpdateError("Passed value is above holidays_for_this_year")
                elif value < 10:
                    raise FieldUpdateError("Passed value is below 10")

        assert (value >= 0), "Passed value is below 0"
        self._holidays_taken = value

    @property
    def holidays_left(self):
        return self._holidays_left

    @holidays_left.setter
    def holidays_left(self, value):
        if type(value) != str and type(value) != int and value is not None:
            raise TypeError("Passed value is of an incompatible type")

        if value is None:
            self._holidays_left = None
            return
        elif type(value) == str:
            # check if the value contains a numeric value in the id field and check if the value is below 0
            assert (not value.strip() == ""), "'holidays_left' field doesn't contain a value"
            assert (value.strip().isnumeric()), "'holidays_left' field doesn't contain a numeric value"

        # at this point, only ints and strings that can be converted into an int should be left
        value = int(value)

        if self._initialisation_finished:
            # try catch will take care of handling those errors and asking user for confirmation
            if self._previous_field_update != "holidays_left" or self._previous_field_update_value != value:
                self._set_previous_field_updates("holidays_left", value)
                if value > (self.holidays_for_this_year - self.holidays_taken):
                    raise FieldUpdateError("Passed value is above the difference between holidays_for_this_year "
                                           "and holidays_taken")
                elif value < (self.holidays_for_this_year - self.holidays_taken):
                    raise FieldUpdateError("Passed value is below the difference between holidays_for_this_year "
                                           "and holidays_taken")

        assert (value >= 0), "Passed value is below 0"
        self._holidays_left = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._set_previous_field_updates("email", value)
        self._email = str(value)
