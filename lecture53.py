def vat_calculate(price):
    totalprice = price+(price*7/100)
    return totalprice

print(vat_calculate(int(input("Product Price="))))
