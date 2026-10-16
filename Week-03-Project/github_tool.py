
import requests
import json


# 1. User ka data fetch karo
def fetch_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()

        return None

    except requests.RequestException:
        return None


# 2. User ki repositories fetch karo
def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()

        return None

    except requests.RequestException:
        return None


# 3. Stars ke hisaab se top repositories nikalo
def top_repos(repos, n=5):
    sorted_repos = sorted(
        repos,
        key=lambda repo: repo["stargazers_count"],
        reverse=True
    )

    return sorted_repos[:n]


# 4. Human-readable report save karo
def save_report(user, repos, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f'Name: {user.get("name") or user["login"]}\n')
        f.write(f'Followers: {user["followers"]}\n')
        f.write(f'Total repos: {user["public_repos"]}\n')

        f.write("\n--- Top Repositories ---\n")

        for repo in repos:
            name = repo["name"]
            stars = repo["stargazers_count"]
            language = repo["language"] or "unknown"

            f.write(f"{name} - {stars} stars - {language}\n")


# 5. Repositories ko JSON file mein save karo
def save_json(repos, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=2, ensure_ascii=False)


# 6. Main function
def main():
    username = input("GitHub username: ").strip()

    if not username:
        print("Error: Username cannot be empty.")
        return

    user = fetch_user(username)
    repos = fetch_repos(username)

    if user is None:
        print("Error: User not found or GitHub API unavailable.")
        return

    if repos is None:
        print("Error: Could not fetch repositories.")
        return

    # Top 5 repositories
    best_repos = top_repos(repos)

    print(f"\nGitHub User: {user.get('name') or user['login']}")
    print(f"Followers: {user['followers']}")
    print(f"Total public repos: {user['public_repos']}")

    print("\n--- Top 5 Repositories ---")

    if len(best_repos) == 0:
        print("This user has no public repositories.")
    else:
        for repo in best_repos:
            name = repo["name"]
            stars = repo["stargazers_count"]
            language = repo["language"] or "unknown"

            print(f"{name} - {stars} stars - {language}")

    # Files save karo
    try:
        save_report(user, best_repos, "report.txt")
        save_json(repos, "repos.json")

    except OSError as error:
        print(f"\nError saving files: {error}")
        return

    # Final summary
    print("\n--- Summary ---")
    print(f"Username: {user['login']}")
    print(f"Repositories fetched: {len(repos)}")
    print(f"Repositories displayed: {len(best_repos)}")
    print("Report saved: report.txt")
    print("JSON saved: repos.json")


# 7. Program start
if __name__ == "__main__":
    main()
