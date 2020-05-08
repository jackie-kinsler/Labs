"""Classes for melon orders."""
class AbstractMelonOrder():

    order_type = None
    tax = 0

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species == 'Christmas':
            base_price = 5 * 1.5

        
        total = (1 + self.tax) * self.qty * base_price

        if self.country_code != 'USA':
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = 'domestic'
    tax = 0.08
    
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 'USA')


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = 'international'
    tax = 0.17

    def __init__(self, species, qty):
        super().__init__(species, qty, 'AUS')

class GovernmentMelonOrder(DomesticMelonOrder):

    tax = 0.00
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True 






