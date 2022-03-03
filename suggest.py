def suggest(mood_flag):
    good_mood_suggestion = [
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
        print("That's good! Why don't you...?")
    elif mood_flag == 0:
        print("Sorry to hear that. Maybe you should...")
    else:
        print("Incorrect flag")