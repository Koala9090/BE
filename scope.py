
"""def counting_function():
    count = 10
    print (f"counter : {count}")
def logging_function():
    count = "Number of logging"
    print(f"loggings : {count}")


counting_function()
logging_function()
"""

# Global scope
x = "global x"

def outer_function():
    # Enclosing scope
    x = "enclosing x"
    
    def inner_function():
        # Local scope
        x = "local x"
        print("Inside inner_function:")
        print("x =", x)  # This will print "local x"
    
    inner_function()
    
    # Accessing the enclosing scope variable
    print("Inside outer_function:")
    print("x =", x)  # This will print "enclosing x"

# Calling the outer_function
outer_function()

# Accessing the global scope variable
print("In the global scope:")
print("x =", x)  # This will print "global x"
