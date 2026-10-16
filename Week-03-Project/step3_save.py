# Week 03 - Project - Step 3 - file me save karo
#
# Ab data ko file me rakhenge - do tarah se, aur farq dekhenge.
#
# KAAM:
#
# 1. Step 2 ka kaam dobara: username se repos lao + guard
#    (copy kar sakte ho, ye dohrana nahi, base hai)
#
# 2. def save_as_text(repos, filename) banao -
#    har line pe "name - stars - language" likhe
#    encoding="utf-8" lagana mat bhoolna
#    Call karo: save_as_text(repos, "repos.txt")
#
# 3. repos.txt khol ke dekho - theek dikh raha hai?
#
# 4. Ab JSON me save karo:
#
#       import json
#
#       with open("repos.json", "w", encoding="utf-8") as f:
#           json.dump(repos, f, indent=2, ensure_ascii=False)
#
#    repos.json khol ke dekho
#
# 5. JSON wapas load karo:
#
#       with open("repos.json", "r", encoding="utf-8") as f:
#           wapas = json.load(f)
#
#    print(type(wapas))        - kya mila?
#    print(len(wapas))         - kitne?
#    print(wapas[0]["name"])   - chal raha hai?
#
# 6. Ab text wali file wapas load karo (Lesson 03 wala load_lines)
#    print(type(...)) aur pehla element print karo
#
# 7. SOCHO AUR BATAO: dono wapas aaye, par ek farq hai.
#    JSON se kya mila? Text se kya mila?
#    wapas[0]["stargazers_count"] + 10  -- ye chalega?
#    text wali file se stars nikaal ke +10 kar sakte ho?
#
# Chalane ke liye:  python step3_save.py

# Yahan se likhna shuru karo:



import requests
import json

# 1. Username se repositories lao + guard

username = "kennethreitz"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

if response.status_code == 200:
    print("API call successful!")

    repos = response.json()

    print("Type:", type(repos))
    print("Total repos:", len(repos))

    # 2. Repositories ko text file me save karo

    def save_as_text(repos, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for repo in repos:
                name = repo["name"]
                stars = repo["stargazers_count"]
                language = repo["language"] or "unknown"

                f.write(f"{name} - {stars} - {language}\n")

    save_as_text(repos, "repos.txt")

    print("\nRepositories saved to repos.txt")

    # 3. JSON file me save karo

    with open("repos.json", "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=2, ensure_ascii=False)

    print("Repositories saved to repos.json")

    # 4. JSON file wapas load karo

    with open("repos.json", "r", encoding="utf-8") as f:
        wapas = json.load(f)

    print("\n--- JSON File Loaded ---")
    print("Type:", type(wapas))
    print("Total repos:", len(wapas))

    if len(wapas) > 0:
        print("First repo:", wapas[0]["name"])

        # Stars number hai, isliye +10 kar sakte hain
        stars = wapas[0]["stargazers_count"]
        print("Stars + 10:", stars + 10)

    # 5. Text file wapas load karo (load_lines)

    def load_lines(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()

    text_data = load_lines("repos.txt")

    print("\n--- Text File Loaded ---")
    print("Type:", type(text_data))

    if len(text_data) > 0:
        print("First element:", text_data[0].strip())

    # 6. Text aur JSON ka farq

    print("\n--- Difference ---")
    print("JSON returns structured Python data.")
    print("Text returns strings.")

else:
    print("API request failed!")
    print("Status code:", response.status_code)
    print("Response:", response.text)


