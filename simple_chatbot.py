# A simple rule-based chatbot using Python dictionaries, conditionals, and string processing

import random
from datetime import datetime

print("---------------------------------WELCOME TO THE PYTHON CHATBOT----------------------------------------")
print("")
print("*" * 100)

name = input("Enter your good name : ")


#Defined Responses in Dictionary 
Responses = { 
            "greetings":["Hello! How can i help you Today",
                           "Hi there! What can i do for You?",
                           "hey! nice to chat with you."],
            "how_are_you":["I'm doing great! Thanks for asking.",
                           "I'm fine and ready to chat",
                           "All good here. How about you?"],
            "farewell":["See You Later",
                      "Bye! Take Care."
                      "GoodBye! have a great day!",
                      "Thanks for chatting"],
            "thanks":["You're welcome!",
                      "No problem !",
                      "Happy to Help",
                      "Mention Not"],
            "weather":["I can't check live weather right now, but I hope it's nice outside!",
                        "Weather chat is my thing, but I don't have live internet access here.",
                        "I cannot fetch real-time weather, but you can ask me about weather in general."],
            "name": [
                    "I am SimpleChatBot, your Python assistant.",
                    "People call me SimpleChatBot.",
                    "I'm a basic chatbot created in Python."],
            "help": [
                    "You can say hello, ask my name, ask the time, ask about weather, say thanks, or type bye to exit.",
                    "Try inputs like: hello, who are you, time, weather, help, joke, how are you, or bye."
                ],
            "joke": [
                    "Why did the computer get cold? Because it left its Windows open!",
                    "Why do programmers prefer dark mode? Because light attracts bugs!",
                    "Why was the Python code so calm? Because it knew how to handle exceptions."
                ],
            "mood": [
                    "I'm feeling productive!",
                    "I'm feeling helpful today!",
                    "I'm in a good mood to chat."
                ],
            "small_talk": [
                    "That's interesting!",
                    "Tell me more.",
                    "Hmm, I see.",
                    "Okay, let's talk more about it."]
            }


def bot_response(user_input):
    #Return a response based on the user's input
    user_input = user_input.lower().strip()
    # 1. Greetings 
    greetings = ["hello","hi","hey","good morning","good evening","good afternoon"]
    if any(word in user_input for word in greetings):
        return random.choice(Responses["greetings"])        #it picks one random element from the value list that is defined in dictionary
    
    # 2. Farewell / Exit
    farewells = ["bye", "goodbye", "see you", "exit", "quit"]
    if any(word in user_input for word in farewells):
        return random.choice(Responses["farewell"])

    # 3. Thanks
    thanks_words = ["thank you", "thanks", "thx", "thanku","thankyou"]
    if any(word in user_input for word in thanks_words):
        return random.choice(Responses["thanks"])

    # 4. Asking name
    name_words = ["your name", "who are you", "what is your name", "tell me your name"]
    if any(word in user_input for word in name_words):
        return random.choice(Responses["name"])

    # 5. Weather inquiry
    weather_words = ["weather", "rain", "sunny", "cloudy", "temperature", "forecast"]
    if any(word in user_input for word in weather_words):
        return random.choice(Responses["weather"])

    # 6. Time inquiry
    time_words = ["time", "current time", "what time"]
    if any(word in user_input for word in time_words):
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # 7. How are you?
    how_are_you_words = ["how are you", "how r you", "how are u", "how do you do"]
    if any(word in user_input for word in how_are_you_words):
        return random.choice(Responses["how_are_you"])

    # 8. Asking for help
    help_words = ["help", "what can you do", "commands", "options"]
    if any(word in user_input for word in help_words):
        return random.choice(Responses["help"])

    # 9. Joke request
    joke_words = ["joke", "funny", "make me laugh"]
    if any(word in user_input for word in joke_words):
        return random.choice(Responses["joke"])

    # 10. Mood question
    mood_words = ["how is your mood", "mood", "feeling", "are you happy"]
    if any(word in user_input for word in mood_words):
        return random.choice(Responses["mood"])

    # 11. Small talk / general responses
    small_talk_words = ["okay", "cool", "nice", "hmm", "wow", "huh"]
    if any(word in user_input for word in small_talk_words):
        return random.choice(Responses["small_talk"])
    # 12. Answer for nknown input 
    return f"Sorry {name} !, I am not able to answer these question. Please type 'HELP' in which you get the type of questions that I can answer easily. ThankYou {name}"


def main():
    print(f"ChatBot: Hello {name}! Type 'help' to see what I can do. OR Type 'bye' to EXIT. ")

    try:
        while True:
            user_input = input(f"{name} : ")

            if not user_input.lower():                    # if user types nothing and press ENTER key 
                print("ChatBot : Please type something so I can respond.")
                continue
  
            response = bot_response(user_input)
            print("ChatBot: ", response)

            if user_input.lower().strip() in ['bye','goodbye','exit','quit']:
                print("------------------------------ThankYou for using the ChatBot-----------------------------------")
                break

    except KeyboardInterrupt:
        print("\nChatBot: Goodbye!")


if __name__=="__main__":
    main()


