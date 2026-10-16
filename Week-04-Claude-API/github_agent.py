# Week 04 - PROJECT - github_agent.py
#
# NAYA CONCEPT KUCH NAHI HAI. Sab kuch tum pehle kar chuke ho:
#   - functions        -> Week-03 ka github_tool.py (copy kar lo)
#   - tool definition  -> kal ka tool_use.py
#   - while loop       -> kal ka tool_use.py (bilkul same)
#
# BANANA KYA HAI:
# Ek agent jisse tum AAM BHASHA me pucho aur wo khud decide kare
# ki kaunsa function chalana hai.
#
#
# KAAM:
#
# 1. Week-03 wale github_tool.py se ye teen function copy karo:
#       fetch_user(username)
#       fetch_repos(username)
#       top_repos(repos, n=5)
#
# 2. DO wrapper function banao jo Claude ke liye TEXT lautaye:
#
#    def tool_get_user(username):
#        - fetch_user chalao
#        - None aaye to  return "User nahi mila: <username>"
#        - warna ek chhoti si line banao, jaise:
#          "Sarmesh | followers: 30137 | public repos: 90"
#
#    def tool_get_top_repos(username, n=5):
#        - fetch_repos + top_repos chalao
#        - har repo ki ek line: "naam - stars stars - language"
#        - sab lines ko jod kar EK string banao  (hint: "\n".join(...))
#
#    DHYAN: dono string lautayenge, dict/list nahi. Kyun? Kal wali galti yaad karo.
#
# 3. tools list banao - dono ke liye definition
#    get_top_repos me do parameter: username (required), n (optional)
#
# 4. run_tool(name, tool_input) likho - naam se sahi wrapper chalao
#
# 5. while loop - kal wale tool_use.py se bilkul same. Copy kar sakte ho.
#
# 6. Sawaal input() se lo, taaki baar-baar code na badalna pade
#
#
# TEST (teeno karo):
#   a) "torvalds ke top 3 repos batao"
#   b) "kennethreitz kaun hai aur uske kitne followers hai?"
#   c) "ajhsdkjahsd123xyz ke repos dikhao"     <- user hai hi nahi, crash na ho
#
#
# EK SAWAAL SOCHNA (code nahi, jawab):
#   fetch_repos 30 repo laata hai. Agar tum poore 30 Claude ko bhej do
#   to kya dikkat hogi? (hint: usage me input_tokens dekhna)
#
# Chalane ke liye:  python github_agent.py

# Yahan se likhna shuru karo:

# 1. User ka data fetch karo

import sys

import requests
import anthropic
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")


load_dotenv()

client = anthropic.Anthropic()

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
def top_repos(repos, n):
    sorted_repos = sorted(
        repos,
        key=lambda repo: repo["stargazers_count"],
        reverse=True
    )

    return sorted_repos[:n]

# wrapper function

def tool_get_user(username):
    user= fetch_user(username)

    if user is None:
        return f"User nahi mila: {username}"

    name = user.get("name") or user["login"]
    followers = user["followers"]
    repos_count = user["public_repos"]

    return f"{name} | followers: {followers} | public repos : {repos_count}"

def tool_get_top_repo(username, n):
    repos= fetch_repos(username)

    if repos is None:
        return f"No repo exist"

    best = top_repos(repos,n)

    lines =[]
    for repo in best:
        name = repo["name"]
        stars=repo["stargazers_count"]
        language = repo["language"] or "Unknown"

        lines.append(f"{name} - {stars} stars - {language}")
    return "\n".join(lines)


tools=[

    {
        "name": "get_user",
        "description":"Github user ki profile aur followers ki information nikalo.",
        "input_schema":{

             "type":"object",
             "properties":{

                 "username":{

                     "type":"string",
                     "description":"Github username"
                 }
             },

             "required":["username"]
        }

    },

    {
        "name": "get_top_repos",
        "description": "GitHub user ki sabse zyada stars wali repositories nikalo.",
        "input_schema": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": "GitHub username"
                },
                "n": {
                    "type": "integer",
                    "description": "Kitni top repositories chahiye",
                    "default": 5
                }
            },
            "required": ["username"]
        }
    }

]

def run_tool(name, tool_input):
    if name == "get_user":
        return tool_get_user(tool_input["username"])
    elif name == "get_top_repos":
        return tool_get_top_repo(tool_input["username"],tool_input.get("n",5))

    return f"unknown tool:{name}"


def run_agent(question):
    
    messages = [
        {"role": "user","content":question}
    ]

    while True:
        response = client.messages.create(
            model="claude-opus-5-5",
            max_tokens=1024,
            tools=tools,
            messages = messages
        )

        messages.append({

            "role":"assistant",
            "content":response.content
        })

         # Agar tool call nahi hai, final answer dikhao

        if response.stop_reason != "tool_use":
            for block in response.content:
                if block.type == 'text':
                    print(block.text)
            break

        # claude ke requested tools execute karo

        tool_result = []

        for block in response.content:
            if block.type == "tool_use":
                result = run_tool(block.name,block.input)

                print(f"\n[Tool executed: {block.name}]")

                tool_result.append({
                    "type":"tool_result",
                    "tool_use_id": block.id,
                    "content":result
                })

        messages.append({
            "role":"user",
            "content": tool_result
        })


if __name__ == '__main__':
    question = input("GitHub ke baree mein kya jaanna hai?")

    run_agent(question)


        
        

