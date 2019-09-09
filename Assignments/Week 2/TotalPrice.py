# TOTAL PRICE
def main ():
    int(purchasePrice)
    int(salesTaxRate)
    float(salesTax)
    float(totalPrice)


#Prompt user for the purchase price of item:
purchasePrice = int(input("What is the Purchase Price? "))
purchasePrice = int(purchasePrice)

#Prompt user for the sales tax rate:
salesTaxRate = int(input("What is the percentage Sales Tax Rate? "))
salesTaxRate = int(salesTaxRate)

#Calculate the sales tax of the item:
salesTax = salesTaxRate * purchasePrice

#Calculate the total price of the item:
totalPrice = (salesTax + purchasePrice)

#Display the total price of the item
print("The Total Price of the item is ", totalPrice)

