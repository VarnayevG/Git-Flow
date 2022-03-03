import random

def suggest(mood_flag):
    good_mood_suggestions = [
        "work on your projects",
        "go out with your friends",
        "go see a movie",
        "do sports",
    ]

    bad_mood_suggestions = [
        "go get some sleep",
        "get some fresh air",
        "drink some tea",
        "talk to your friends",
    ]

    if mood_flag == 1:
        suggestion = random.choice(good_mood_suggestions)
        print(f"That's good! Why don't you {suggestion}?")
    elif mood_flag == 0:
        suggestion = random.choice(bad_mood_suggestions)
        print(f"Sorry to hear that. Maybe you should {suggestion}")
    else:
        print("Incorrect flag")