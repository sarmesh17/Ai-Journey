# Week 04 - chat_memory.py
#
# chat.py ki copy banao, aur usme ek cheez jodo:
# baat-cheet file me save ho, aur agli baar wahi se shuru ho.
#
# NAYA CONCEPT NAHI HAI - Week-03 ka json.dump / json.load.
#
#
# KAAM:
#
# 1. chat.py ko copy karke chat_memory.py bana lo (is file me paste kar do)
#
# 2. def save_history(messages, filename) banao
#       json.dump se messages ko file me likhe
#       encoding="utf-8" aur ensure_ascii=False lagana
#
# 3. def load_history(filename) banao
#       file ho to json.load karke list lautaye
#       file NA ho to khaali list []  lautaye
#       (hint: try/except FileNotFoundError, ya os.path.exists)
#
# 4. Program shuru hote hi:
#       messages = load_history("chat_history.json")
#       agar purani baat mili to batao: "Pichhli baat-cheet load hui (N messages)"
#
# 5. 'bye' pe nikalte waqt save_history(messages, "chat_history.json")
#
# 6. TEST: do sawaal pucho, 'bye' karo. Phir dobara chalao aur pucho
#    "maine abhi kya pucha tha?" - usko yaad hona chahiye.
#
#
# CHETAVNI - ek error aayega, aur wo JAAN-BOOJH KE hai:
#
#   Jab pehli baar save karne jaoge, json.dump CRASH karega.
#   Error padhna, samajhne ki koshish karna, phir batana.
#
#   Hint sochne ke liye: messages me assistant ka content kya hai?
#   String? dict? ya kuch aur? (response.content yaad karo)
#   Aur json sirf kin cheezon ko samajhta hai?
#
#   Error aaye to ruk jana - main saath me solve karunga.
#
# Chalane ke liye:  python chat_memory.py

# Yahan se likhna shuru karo:

