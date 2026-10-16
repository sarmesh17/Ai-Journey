# Week 04 - Tukda 2 - pehla asli API call
#
# KAAM:
#
# 1. Niche wala code chalao jaisa hai. Kya aaya?
#    (agar 401/403 error aaye to key ka type galat hai - batana)
#
# 2. response.usage print karo - kitne token lage?
#
# 3. Sawaal badal do - kuch aur pucho
#
# 4. system prompt add karo (niche samjhaya hai) aur farq dekho
#
# 5. max_tokens ko 20 kar do aur chalao. Jawab ka kya hua?
#    response.stop_reason print karo - kya kehta hai?
#
# Chalane ke liye:  python hello_claude.py

import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

# Key ka naam nahi dena padta - client khud ANTHROPIC_API_KEY dhundh leta hai
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1000,
    system="Tum ek sakht Python teacher ho. Hamesha Hinglish me jawab do, aur har jawab me ek chhota code example zaroor do.",
    messages=[
        {"role": "user", "content": "Namaste! Do line me batao ki Python kya hai."}
    ],
)

# response.content ek LIST hai - har item ek "block"
# har block text ka nahi hota, isliye type check karna zaroori hai
for block in response.content:
    if block.type == "text":
        print(block.text)


print(response.stop_reason)

print()
print("--- usage ---")
print(response.usage)
