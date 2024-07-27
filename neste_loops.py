counter = 5

while counter > 0:
    inerr_counter = 1
    while inerr_counter <= counter:
        print (inerr_counter * "wa",end=" " )
        inerr_counter += 1
    print()
    counter -= 1


for i in range(1, 11):
  # Outer loop iterates through rows (multiplication factors)
  for j in range(1, 11):
    # Inner loop iterates through columns (other factors)
    product = i * j
    print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
  print()  # Move to a new line after each row


rows = 5

for i in range (1, rows+1):
   for j in range (1, i+1):
        print("*", end="")
   print()

rows = 5

for i in range(1, rows + 1):
  for j in range(1, i + 1):
    print("*", end="")
  print()  
