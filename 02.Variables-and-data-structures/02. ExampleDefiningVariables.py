Name = "Mustafa Korkmaz"
phone = "15531315"
mail = "mustafa@gmail.com"
hometown = "Şanlıurfa"

vatRate = 0.18  # 'vateRate' yanlış yazmışsınız, VAT = KDV demek

productsPurchased1 = "Wireless mouse"
productsPurchased2 = "Wireless Keyboard"
productsPurchased3 = "Laptop"

priceProductPurchased1 = 550
priceProductPurchased2 = 650
priceProductPurchased3 = 55000

sumPriceProductsPurchased = priceProductPurchased1 + priceProductPurchased2 + priceProductPurchased3
print("Sum price of the products purchased:", sumPriceProductsPurchased)

totalVatAmount = sumPriceProductsPurchased * vatRate
print("Total VAT amount:", totalVatAmount)

totalPriceWithVat = sumPriceProductsPurchased + totalVatAmount
print("Total price including VAT:", totalPriceWithVat)
