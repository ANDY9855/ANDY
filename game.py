lary = "The Great Larry: "
name = "Unknown: "
print(name + "Hello adventurer!")
hi = input("Y/N: ")
print(name + "I don't remember seeing you.")
print(name + "You must be new here!")

cevap1 = int(input("1) yes I'm new \n2) nope I have always been here: "))
if cevap1 == 1:
    print(name + "How great! New people are always welcome!")
    print("Well... Of course if you are not a turtle")
    print("*laughs*")
elif cevap1 == 2:
    print(name + "How odd... As the guard of these precious lands,")
    print("I would like to apologise for not knowing you. I hope you would accept my apology. I also hope that you are not a turtle.")

cevap2 = int(input("1) where am I \n2) who are you: "))
if cevap2 == 1:
    print(name + "Haha, don't be silly! You are at the lands of Mother Miranda!")
    print("The best place you could ever be! (Again, if you are not a turtle or... ARE YOU!)")
elif cevap2 == 2:
    print(lary + "I am The Great Larry and will be your guide through your adventure!")

print(lary + "Pardon my audacity, but I haven't seem to get your name.")
print("Y/N: My name is,")
y = input()
yn = y + ": "
print(lary)
print("What a beautiful name for a beautiful person like you! It's a pleasure to meet you!")
print(yn + "It's my pleasure.")
print(lary + "You see, I am protecting the precious borders of this land for ages! Before I let you in, if you wouldn't mind I need to check if you are a turtle or not.")
cevap3 = int(input("1) what's wrong with being a turtle: "))
print(lary + "Turtles are terrible creatures! Did you know that they were shapeshifters?")
# Continue the story here...
# ...previous code...

if cevap3 == 1:
    print(yn + "I had no idea! Are they dangerous?")
    print(lary + "Oh, indeed! Turtles can transform into anything they desire. They've been known to impersonate rocks, trees, and even other animals. Their shapeshifting abilities make them elusive and mysterious.")
    print(name + "Fascinating! But why would they do that?")
    print(lary + "Ah, my dear adventurer, that's the million-dollar question! Some say it's for protection, while others believe they do it just for fun. Regardless, we must remain vigilant.")
    print(name + "I promise I'm not a turtle!")
    print(lary + "Good! Now, let's proceed. Beyond these gates lies a realm of magic and danger. Are you ready for your adventure?")
    adventure_ready = input("Y/N: ")
    if adventure_ready.lower() == "y":
        print(lary + "Excellent! Brace yourself, for the unknown awaits. Follow me!")
        # Continue the story with more twists and turns...
    else:
        print(lary + "No worries, my friend. Take your time. When you're ready, just say the word, and we'll embark on this extraordinary journey together.")
else:
    print(name + "I assure you, I'm not a turtle!")
    print(lary + "Very well. Let's move forward. The path ahead is treacherous, but with courage and wit, you'll prevail. Are you prepared?")
    adventure_ready = input("Y/N: ")
    if adventure_ready.lower() == "y":
        print(lary + "Splendid! Follow me, and let the adventure begin!")
        # Continue the story with more twists and turns...
    else:
        print(lary + "No rush, my friend. Whenever you're ready, we'll step into the unknown together.")