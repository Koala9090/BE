adjective1 = input("Enter an adjective to describe the day : ")
adjective2 = input("Enter an adjective to describe an animal : ")
adjective3 = input("Enter an adjective describe something haha: ")
adjective4 = input("Enter an adjective describe a feeling : ")
if adjective1.lower() in ["rainy","gloomy","stormy","cloudy"]:
    day_activity = "i bought an umbrela "
else:
    day_activity = "i was exited to see the animals"

story_template =f"""On a beautiful {adjective1} day,{day_activity} 
I went to the zoo. I saw a funny {adjective2} monkey swinging from the trees. 
Then, I spotted a majestic {adjective3} lion lounging in the sun.  
What a wild and {adjective4} experience! """
print (story_template) 
