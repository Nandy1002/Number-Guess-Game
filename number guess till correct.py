import pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def say(text):
    engine.say(text)
    engine.runAndWait()
    
print("INSTRUCTIONS:--")
say("INSTRUCTIONS")
print("This game has a Hidden Number, You have to find that number by Guessing.")
print("I will help you to guess that number in each attemted by telling its greater or smaller than the original.")
say("This game has a Hidden Number, You have to find that number by Guessing. I will help you to guess that number in each attemted by telling its greater or smaller than the original.    NOW.....Enter your guessed number... ")  
n = int(input("Enter your guessed number : "))
temp = 47
# print("You have 5 Chances")
i = 0
while i>=0:
    i += 1
    if n>temp:
        print("The Guessed number is greater than the actual number ")
        say("Your Guessed number is greater than the actual number...Enter your guessed number again...")       
        n = int(input("Enter your guessed number again : "))
    elif n<temp:
        print("The Guessed number is smaller than the actual number ")
        say("Your Guessed number is smaller than the actual number...Enter your guessed number again...")
        n = int(input("Enter your guessed number again : "))
    else:
        print("You guessed the right number")
        say("WOW..... You guessed the right number")
        break

print(f"Congrats You win in your {i} attempt")
say(f"Congrats, You win the game in your {i} attempt")
print("Thanks for playing.....")
say("Thanks. for Playing.")