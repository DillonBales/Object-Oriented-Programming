# Dillon Bales
# 5/14/2025

class TaxCalculation:
    salesTax = 0.0675
    countyTax = 0.04
    
    def __init__(self, purchase):
        self.purchase = purchase

    def totalTax(self):
        sales = self.purchase * TaxCalculation.salesTax
        county = self.purchase * TaxCalculation.countyTax
        total = sales + county

        print(f"The total tax for this purchase is ${total:.2f}")

    def totalSales(self):
        sales = self.purchase * TaxCalculation.salesTax
        county = self.purchase * TaxCalculation.countyTax
        total = sales + county + self.purchase 

        print(f"The total for this purchase is ${total:.2f}")


paid = input("How much is this purchase: $")

purchase1 = TaxCalculation(float(paid))
purchase1.totalTax()
purchase1.totalSales()



    