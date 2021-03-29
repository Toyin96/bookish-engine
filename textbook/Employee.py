"""Models a real-life employee object"""


class Employee:
    """A class that depicts basic profile of an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Initializes the attributes of employee class"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Adds $5,000 to the annual salary by default"""
        self.annual_salary += raise_amount
