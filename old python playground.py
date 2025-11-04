print("|- - - */ Outfit Picker \* - - -|")
print("A set of questions will be asked. Please answer accordingly!")

error_message = str("You are missing some input or have typed an invalid answer. Please try again! :(")

# INPUT
weather = input("Is the weather rainy or sunny? (rainy/sunny) ")
if weather.lower() == "sunny":
    temperature = input("Is the temperature warm, pleasant, or cold? (warm/pleasant/cold) ")
elif weather.lower() == "rainy":
    temperature = None
else:
    print(error_message)
dress_code = input("Do you have to follow a strict dress code? (yes/no) ")
if dress_code.lower() == "no":
    event_type = input("Are you going to a formal or casual setting? (formal/casual) ")
elif dress_code.lower() == "yes":
    event_type = None
else:
    print(error_message)
    
# NESTED IF ELSE STATEMENTS
if weather.lower() == "sunny":
    if temperature.lower() == "warm":
        if dress_code.lower() == "yes":
            print("Follow the dress code, but keep your outfit light as much as possible!")
        elif event_type.lower() == "formal":
            print("Wear light, formal clothing.")
        elif event_type.lower() == "casual":
            print("Wear any comfortable casual outfits, but keep your clothes light!")
        else:
            print(error_message)
    elif temperature.lower() == "pleasant":
        if dress_code.lower() == "yes":
            print("Follow the dress code as you see fit.")
        elif event_type.lower() == "formal":
            print("Choose any presentable formal outfits.")
        elif event_type.lower() == "casual":
            print("You can wear whatever you like!")
        else:
            print(error_message)
    elif temperature.lower() == "cold":
        if dress_code.lower() == "yes":
            print("Follow the dress code, and wear a coat or jacket to keep yourself warm.")
        elif event_type.lower() == "formal":
            print("Feel free to pick any presentable formal outfits, preferably heavy ones.")
        elif event_type.lower() == "casual":
            print("Pick any casual outfit you like, but wear a hoodie, jacket, or any cold outerwear as well.")
        else:
            print(error_message)
    else:
        print(error_message)
elif weather.lower() == "rainy":
    if dress_code.lower() == "yes":
        print("")
    elif event_type.lower() == "formal":
        print("")
    elif event_type.lower() == "casual":
        print("")
    else:
        print(error_message)
else:
    print(error_message)