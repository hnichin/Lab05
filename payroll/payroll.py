# Author: Karanjot Singh Kailay, Mukul Kumar, Hmun Cung Hnin Ni Chin
# Date: 9/30/2026
# File: payroll.py
# Description: makes the invoices and employees and gets the totals for the payroll page

from payroll.invoice import Invoice
from payroll.models import Person, Secretary, Manager, SalesPerson, Employee, ExecutiveManager


# works for any payable just calls its to_dict
def serialize_payroll(payable):
    return payable.to_dict()

def build_payroll_data():
    # reset the counts so they don't keep adding up on every refresh
    Employee.employee_count = 0
    Invoice.invoice_count = 0
    person1 = Person(
        "Alice",
        "Wong",
        "Female",
        "123-45-6789"
    )
    person2 = Person(
        "Thomas",
        "Cho",
        "Male",
        "987-65-4321"
    )
    person3 = Person(
        "Elena",
        "Stone",
        "Female",
        "222-33-4444"
    )
    person4 = Person(
        "John",
        "Davis",
        "Male",
        "111-22-3333"
    )

    secretary = Secretary(
        person1,
        101,
        2,
        25.0,
        40
    )

    manager = Manager(
        person2,
        102,
        8,
        "IT",
        8500.0
    )
    executive_manager = ExecutiveManager(
        person3,
        103,
        10,
        "Operations",
        12000.0,
        2500.0
    )
    sales_person = SalesPerson(
        person4,
        104,
        4,
        15000.0,
        0.08
    )

    invoice1 = Invoice("Printer Cartridge",75.5,3)
    invoice2 = Invoice("Monitor Stand", 42.99, 2)

    payables = [secretary, manager, sales_person, executive_manager, invoice1, invoice2]
    payable_dictionary = []
    gross_count = 0

# get each ones dict and add up the pay
    for payable in payables:
        data = serialize_payroll(payable)
        payable_dictionary.append(data)
        gross_count += payable.calculate_payment()

# send it all back for flask
    return  {
        "payables": payable_dictionary,
        "invoice_count": Invoice.get_invoice_count(),
        "employee_count": Employee.get_employee_count(),
        "total_gross": gross_count
    }



