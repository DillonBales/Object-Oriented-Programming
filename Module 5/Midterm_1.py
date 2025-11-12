# Name: Dillon Bales
# Date: 6/4/2025

class TaxCalculation:
    #initiate all the attributes
    def __init__(self, purchase_amount, sales_tax_rate, county_tax_rate):
        self.purcahse_amount = purchase_amount
        self.sales_tax_rate = sales_tax_rate
        self.county_tax_rate = county_tax_rate

    #Calculate the tax
    def total_tax(self):
        sales = self.purcahse_amount * self.sales_tax_rate
        county = self.purcahse_amount * self.county_tax_rate
        tax = sales + county
        return tax

    #Add tax to the purchase 
    def total_sales(self):
        sales = self.purcahse_amount * self.sales_tax_rate
        county = self.purcahse_amount * self.county_tax_rate
        total = self.purcahse_amount + county + sales
        return total
    
class CustomTaxCalculation(TaxCalculation):
    #Initiate the new attribute
    def __init__(self, purchase_amount, sales_tax_rate, county_tax_rate, custom_rate):
        super().__init__(purchase_amount, sales_tax_rate, county_tax_rate)
        self.custom_rate = custom_rate

    #Calculate the tax with custom tax
    def total_tax(self):
        sales = self.purcahse_amount * self.sales_tax_rate
        county = self.purcahse_amount * self.county_tax_rate
        custom = self.purcahse_amount * self.custom_rate
        tax = sales + county + custom
        return tax
    
#Polymorphism
regular = TaxCalculation(15, 0.005, 0.03)
custom = CustomTaxCalculation(15, 0.005, 0.03, 0.05)

def print_tax(object):
    print(f"Total Tax: {round(object.total_tax(), 2)}")

print_tax(regular)
print_tax(custom)

#Testing
purchase1 = TaxCalculation(100, 0.07, 0.03)
purchase2 = CustomTaxCalculation(250.50, 0.06, 0.025, 0.01)
print(round(purchase1.total_tax(), 2))
print(round(purchase1.total_sales(), 2))
print(round(purchase2.total_tax(), 2))