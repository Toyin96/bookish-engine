import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests all the functionalities present in class Employee"""

    def setUp(self) -> None:
        """creates an employee object to be used throughout all the methods"""
        self.employee = Employee("Toyin", "Onagoruwa", 2500000)

    def test_give_default_raise(self):
        """test to see if employee would be given default $5000 by default"""
        self.employee.give_raise()
        self.assertEqual(2505000, self.employee.annual_salary)

    def test_give_custom_raise(self):
        """test to see if a custom raise would reflects in an employee's annual salary"""
        self.employee.give_raise(650_000)
        self.assertEqual(3_150_000, self.employee.annual_salary)


if __name__ == '__main__':
    unittest.main()
