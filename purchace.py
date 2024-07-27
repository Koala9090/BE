pamount = 223
if pamount >= 1000:
    discount = 0.1
elif pamount >= 500:
    discount = 0.05
else :
    discount = 0
final_price = pamount*(1-discount)
print ("the final price is",final_price)
