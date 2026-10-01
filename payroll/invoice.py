# Author: Hmun Cung Hnin Nichin
# Date: 9/30/2026
# File: invoice.py
# Description: Define invoice class
from payroll.payable import Payable


class Invoice(Payable):
    #Class Attribute
    invoice_count = 0
    def __init__(self, part_name:str, price: float, quantity: int) -> None:
        self.part_name = part_name
        self.price = price
        self.quantity = quantity

    def calculate_payment(self) -> float:
        return self.price * self.quantity

    def to_dict(self) -> dict:
        return {
            'part_name': self.part_name,
            'price': self.price,
            'quantity': self.quantity,
            'payment_amount': self.calculate_payment()
        }

    @classmethod
    def get_invoice_count(cls) -> int:
        return cls.invoice_count
