"""Classes for melon orders."""
class AbstractMelonOrder:
    order_type = None       
    tax = 0

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def __repr__(self):
        return f"< species = {self.species} qty = {self.qty} shipped = {self.shipped} order_type = {self.order_type} tax = {self.tax}>"

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    #def __init__(self, species, qty):
    #   """Initialize melon order attributes."""

        #self.species = species
        #self.qty = qty
        #self.shipped = False
    order_type = "domestic"
    tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

        #self.species = species
        #self.qty = qty
    # country_code = country_code
        #self.shipped = False

    order_type = "international"
    tax = 0.17

        
    def __init__(self,species,qty,country_code):
       
        super().__init__(species, qty)  # [calls the __init__ on the parent]
        self.country_code = country_code

    def __repr__(self):
        return f"< species = {self.species} qty = {self.qty} shipped = {self.shipped} order_type = {self.order_type} tax = {self.tax} country_code = {self.country_code}>"


    def get_total(self):
        """Calculate price, including tax."""

        
        #then base_price =  5 * 1.5
        #else base_price = 5
        # 
        base_price = 5
        
        if self.species == "christmas melon":
            base_price = 5 * 1.5  #7.5
            

        total = (1 + self.tax) * self.qty * base_price
        

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
