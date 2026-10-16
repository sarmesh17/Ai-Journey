
import requests

# 1. Username aur URL
username = "kennethreitz"
url = f"https://api.github.com/users/{username}/repos"

# 2. API call + guard
response = requests.get(url)

if response.status_code == 200:
    print("API call successful!")

    # 3. JSON data aur type check
    repos = response.json()
    print("Type:", type(repos))

    # 4. Total repositories
    print("Total repos:", len(repos))

    # 5. Pehle repo ka naam + 6. Keys
    if len(repos) > 0:
        print("First repo:", repos[0]["name"])
        print("Keys:", repos[0].keys())

    # 7. Har repo ka naam, stars aur language
    print("\n--- All Repositories ---")

    for repo in repos:
        name = repo["name"]
        stars = repo["stargazers_count"]
        language = repo["language"] or "unknown"

        print(f"{name} - {stars} stars - {language}")

    # 8. Sirf 100 se zyada stars wale repos (normal loop)
    print("\n--- Repos with More Than 100 Stars (Loop) ---")

    popular_repos = []

    for repo in repos:
        if repo["stargazers_count"] > 100:
            popular_repos.append(repo)

    for repo in popular_repos:
        print(
            f'{repo["name"]} - '
            f'{repo["stargazers_count"]} stars - '
            f'{repo["language"] or "unknown"}'
        )

    print("Popular repos count:", len(popular_repos))

    # 9. Wahi filter comprehension se, sirf names
    popular_names = [
        repo["name"]
        for repo in repos
        if repo["stargazers_count"] > 100
    ]

    print("\n--- Popular Repo Names (Comprehension) ---")
    print(popular_names)

    # 10. Sabse zyada stars wala repo
    if len(repos) > 0:
        most_starred = repos[0]

        for repo in repos:
            if repo["stargazers_count"] > most_starred["stargazers_count"]:
                most_starred = repo

        print("\n--- Most Starred Repository ---")
        print("Name:", most_starred["name"])
        print("Stars:", most_starred["stargazers_count"])
        print("Language:", most_starred["language"] or "unknown")

else:
    print("API request failed!")
    print("Status code:", response.status_code)
    print("Response:", response.text)
