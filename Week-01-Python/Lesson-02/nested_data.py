# Lesson 02 - Tukda 4 - nested_data.py
#
# Ye Lesson 02 ka last kaam hai. Aur ye asli AI data ka shape hai.
#
# KAAM (ek-ek point tick karte jaana, file ke comment se):
#
# 1. Apna about_me dict dobara banao (4-5 key)
# 2. .items() se loop chalao - har line pe "key: value" print karo
# 3. Ek NESTED dict banao - user ke andar ek "skills" dict ho. Aise:
#
#       user = {
#           "name": "Sarmesh",
#           "skills": {"flutter": "strong", "python": "seekh raha hu"}
#       }
#
#    Isme se "python" ki value print karo (chained [] use karna padega)
#
# 4. Ab LIST OF DICTS banao - ye AI API ka asli shape hai.
#    3 messages ki list, har message ek dict:
#
#       messages = [
#           {"role": "user", "text": "hello"},
#           {"role": "ai", "text": "hi, kaise ho?"},
#           {"role": "user", "text": "python seekh raha hu"},
#       ]
#
# 5. Us list pe loop chalao aur aise print karo:
#       user: hello
#       ai: hi, kaise ho?
#       user: python seekh raha hu
#
# 6. Aakhri message ka text print karo (hint: [-1] aur phir key)
#
# 7. Sirf "user" ke messages print karo (loop ke andar if)
#
# Chalane ke liye:  python nested_data.py

# Yahan se likhna shuru karo:

about_me={'name': 'Sarmesh','age' : 7,'city': 'Birgunj','language': 'Bhojpuri'}

for key,value in about_me.items():
    print(f"{key} : {value}")

user = {

    "name": "Sarmesh",
    "skills": {"flutter": "strong", "python": "seekh raha hu"}
}

print(user["skills"]["python"])

users=[

   {"role": "user", "text": "hello"},
  {"role": "ai", "text": "hi, kaise ho?"},
  {"role": "user", "text": "python seekh raha hu"},

]

for item in users:
    print(f'{item["role"]} : {item["text"]}') 

# akhri message
print(users[-1]["text"])

for item in users:
    if item["role"] == "user":
        print(item["text"])


    





