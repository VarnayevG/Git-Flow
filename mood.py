def ask_about_mood(name: str) -> int:
    print(f"How's it going, {name}?")
    ans = input()
    good_moods = ['ok', 'fine', 'good', 'alright']
    if ans.lower() in good_moods:
        return 1
    else:
        return 0
