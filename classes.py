# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Default attribute value

#     def get_descriptive_name(self):
#         full_name = f"{self.year} {self.make} {self.model}"
#         return full_name

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#            self.odometer_reading += miles



# my_car = Car("Toyota", "AE86", 1995)
# print(my_car.get_descriptive_name())  # Output: 2020 Toyota Camry

# my_car.read_odometer()  # Output: This car has 0 miles on it.
# my_car.update_odometer(1000)  # Update odometer reading
# my_car.read_odometer()  # Output: This car has 100 miles on it.

# my_car.increment_odometer(5000)  # Increment odometer reading
# my_car.read_odometer()  # Output: This car has 150 miles on it.






# class students:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display_name(self):
#         print(f"Name : {self.name} age : {self.age}")

# student1=students("alice",44)
# student1.display_name()


# class product:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def calc(self):
#         print(f"name : {self.name}, value = ", self.price * self.quantity)  

# products = product("tanpond",990,3)
# # products.calc()

# class OutOfStockError(Exception):
#     def __init__(self, item_name):
#         self.item_name = item_name

#     def __str__(self):
#         return f"Sorry, the item '{self.item_name}' is out of stock."

# class InsufficientQuantityError(Exception):
#     def __init__(self, item_name, requested, available):
#         self.item_name = item_name
#         self.requested = requested
#         self.available = available

#     def __str__(self):
#         return f"Sorry, we only have {self.available} '{self.item_name}' in stock. You requested {self.requested}."

# product_inventory = {
#     "apple": 10,
#     "banana": 5,
#     "orange": 0,  # Out of stock
#     "grapes": 3
# }

# def purchase_item(item, quantity):
#     try:
#         if item not in product_inventory:
#             raise KeyError(item)
#         if product_inventory[item] == 0:
#             raise OutOfStockError(item)
#         if product_inventory[item] < quantity:
#             raise InsufficientQuantityError(item, quantity, product_inventory[item])
        
#         print(f"Purchase successful: {quantity} {item}(s)")
#         product_inventory[item] -= quantity
#     except KeyError:
#         print(f"Sorry, '{item}' is not available in our inventory.")

# # Testing the improved function
# try:
#     purchase_item("apple", 5)  # Should be successful
#     purchase_item("apple", 4)  # Should raise InsufficientQuantityError
#     purchase_item("apple", 2)  # Should raise OutOfStockError
#     purchase_item("pear", 1)  # Should print item not available
# except OutOfStockError as e:
#     print(e)
# except InsufficientQuantityError as e:
#     print(e)





# def divide_numbers():
#     try:
#         num1 =float(input("Enter First number : ")) 
#         num2 =float(input("Enter Second number : "))
#         result = num1 / num2
#         print(f"{num1} / {num2} = {result}")
#     except ZeroDivisionError:
#         print("you cannot divide by 0")
#     except ValueError:
#         print("enter a valid value")

# divide_numbers()

# def file_read():
#     file_name = input("Enter a valid file name : ")
#     try:
#         with open(file_name, 'r')as file :
#             content = file.read()
#             print("file content : ")
#             print(content)
#     except FileNotFoundError:
#         print(f"{file_name} does not exist")

# file_read()

class ValueTooHighError(Exception):
    def __init__(self, value):
        self.value = value
        self.message= f"{value} is too high "
        super().__init__(self.message)
def check_number ():
            try:
                vv=int(input("enter a number less than 100 : "))
                if vv > 100:
                    raise ValueTooHighError(vv)
                print(f"{vv} is less than 100 ")
            except ValueTooHighError as e:
                print(e)
            except ValueError:
                 print("Error: Please enter a valid integer!")
check_number()