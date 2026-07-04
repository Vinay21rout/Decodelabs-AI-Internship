# pre-defined rules and logic of output

responses = {
    "hello": "Hi there!",
    "help": "I can respond to greetings and simple commands.",
    "thanks": "You're welcome!",
    "how are you": "I'm just code, but I'm running fine!",
    "help": "I can respond to greetings, farewells, and simple questions.",
    "who are you": "I’m a rule-based chatbot built for Project 1.",
    "what can you do": "I can chat with you using predefined responses.",
    "good morning": "Good morning! Hope you have a productive day.",
    "good night": "Good night! Sleep well.",
    "ok": "Alright!",
    "yes": "Great!",
    "no": "Okay, noted.",
    "tell me a joke": "Why don’t programmers like nature? Too many bugs!",
    "favorite language": "Python, of course!",
    "decode labs": "DecodeLabs is powering this training project."
}

# bot input ability from user and handle fallback and exit control loop  

while True:
    user_input=input("User: ").lower().strip()
    if user_input in ['bye','quit','q']:
        print("GoodBye👋")
        break
    
    reply=responses.get(user_input,"I don't know!")
    print("Bot: ",reply)
        