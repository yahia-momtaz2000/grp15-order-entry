from abc import ABC, abstractmethod


class Taxable(ABC):
    # class attributes [ static attributes ]
    VAT_PERCENTAGE = 14

    @abstractmethod
    def get_tax(self, amount):
        pass
