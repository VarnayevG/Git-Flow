def ask_about_mood(name):
    print(f"How's it going, {name}?")
    ans = input()
    if "good" in ans.lower() \
        or "fine" in ans.lower() \
        or "ok" in ans.lower() \
        or "alright" in ans.lower():
        return 1
    else:
        return 0

print(ask_about_mood('Gleb'))
