value = input("enter a value of any kind :")

match value:
    case str():
        print("you entered a string :", value)
    case int():
        print("you entered an intenger :", value)
    case _:
        print("you are a dumb fuck")
