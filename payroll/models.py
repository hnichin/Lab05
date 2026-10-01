# Author: Hmun Cung Hnin Nichin
# Date: 9/30/2026
# File: models.py
# Description:
from payroll.payable import Payable
from abc import abstractmethod
class Person:
    def __init__(self, first_name:str, last_name:str, gender:str, ssn:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.ssn = ssn

    def to_dict(self) -> dict:
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'ssn': self.ssn
        }


class Employee(Payable):
    #Class Attribute
    employee_count = 0
    def __init__(self, person: Person, emp_id: int, years_of_service: int) -> None:
        self.person = person
        self.emp_id = emp_id
        self.years_of_service = years_of_service

        Employee.employee_count += 1
    @abstractmethod
    def calculate_payment(self) -> float:
        pass
    def to_dict(self) -> dict:
        return self.person.to_dict() | {
            'type': type(self).__name__,
            'emp_id': self.emp_id,
            'years_of_service': self.years_of_service,
            'payment': self.calculate_payment()
        }
    @classmethod
    def get_employee_count(cls) -> int:
        return cls.employee_count

class Secretary(Employee):
    def __init__(self, person, emp_id: int, years_of_service:int,wage:float, hours:int) -> None:
        super().__init__(person, emp_id, years_of_service)
        self.wage = wage
        self.hours = hours

    def calculate_payment(self) -> float:
        return self.wage * self.hours

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            'wages': self.wage,
            'hours': self.hours
                     })
        return data


class Manager(Employee):
    def __init__(self, person:Person, emp_id: int, years_of_service:int, department:str, salary: float) -> None:
        super().__init__(person, emp_id, years_of_service)
        self.department = department
        self.salary = salary

    def calculate_payment(self) -> float:
        return self.salary

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            'department': self.department,
            'salary': self.salary
        })
        return data

class SalesPerson(Employee):
    def __init__(self, person:Person, emp_id: int, years_of_service:int, sales: float, commission_rate: float) -> None:
        super().__init__(person, emp_id, years_of_service)
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_payment(self) -> float:
        return self.sales * self.commission_rate

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            'sales': self.sales,
            'commission_rate': self.commission_rate
        })
        return data

class ExecutiveManager(Manager):
    def __init__(self, person:Person, emp_id: int, years_of_service:int, department:str, salary: float, bonus: float) -> None:
        super().__init__(person, emp_id, years_of_service,department, salary)
        self.bonus = bonus

    def calculate_payment(self):
        print("salary:", self.salary, type(self.salary))
        print("bonus:", self.bonus, type(self.bonus))
        return self.salary + self.bonus

    def to_dict(self) -> dict:
        data = super().to_dict()

        data.update({
            "bonus": self.bonus
        })

        return data


