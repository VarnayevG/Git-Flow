def ask_about_mood(name: str) -> int:
    """

    Ask about person's mood and return
    number based on the answer

    Parameters:
        name: person's name

    Returns:
        1 if answer is among "good moods" options
        0 if otherwise
    """
    print(f"How's it going, {name}?")
    ans = input()
    good_moods = ['ok', 'fine', 'good', 'alright']
    if ans.lower() in good_moods:
        return 1
    else:
        return 0
