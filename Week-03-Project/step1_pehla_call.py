# Week 03 - Project - Step 1 - pehla API call
#
# Ye project: GitHub se kisi user ke repos laana, chaanna, file me save karna.
# GitHub ka ye API free hai - koi key nahi, koi paisa nahi.
#
# KAAM:
#
# 1. requests import karo
#
# 2. Is URL pe GET call karo (apna GitHub username daal sakte ho,
#    ya koi bhi - "torvalds" try karke dekho):
#
#       https://api.github.com/users/torvalds
#
# 3. response.status_code print karo - 200 aana chahiye
#
# 4. response.json() ka result ek variable me rakho, aur print karo
#    (bohot saara data aayega - ghabrana mat)
#
# 5. type() se check karo - .json() ne kya diya? dict ya list?
#
# 6. Us data me se ye teen cheez print karo:
#       - name
#       - public_repos
#       - followers
#
# 7. Ab ek aisi key maango jo hai hi nahi - "salary"
#    [] se bhi try karo aur .get() se bhi. Farq dekho.
#
# 8. URL me username galat kar do (jaise "ajhsdkjahsd123xyz")
#    aur status_code dekho. Kya aaya?
#
# Chalane se pehle: venv activate hona chahiye aur requests install hona chahiye
# Chalane ke liye:  python step1_pehla_call.py

# Yahan se likhna shuru karo:=

import requests

url= "https://api.github.com/users/ajhsdkjahsd123xyz"
response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    data = response.json()
    print(data["name"])
    print(data.get("salary"))
    print(data["public_repos"])
    print(data["followers"])
    print(type(data))

else:
    print("Gadbad hui, code:", response.status_code)


# print(data["salary"])






