# Author: Karanjot Singh Kailay
# Date: 9/30/2026
# Name: payable.py
# Description: Define the abstract Payable class
from abc import ABC, abstractmethod

class Payable(ABC):
    @abstractmethod
    def calculate_payment(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
