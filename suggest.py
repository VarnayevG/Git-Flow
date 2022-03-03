from xml.dom.expatbuilder import ElementInfo


def suggest(mood_flag):
    if mood_flag == 1:
        print("That's good! Why don't you...?")
    elif mood_flag == 0:
        print("Sorry to hear that. Maybe you should...")
    else:
        print("Incorrect flag")