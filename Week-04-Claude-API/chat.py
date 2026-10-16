# Week 04 - Tukda 3 - baat-cheet (multi-turn conversation)
#
# Ab asli chat banayenge - jo pichhli baat yaad rakhe.
#
# KAAM:
#
# 1. Niche wala code pura karo (TODO likhe hai jahan)
#
# 2. Chalao aur teen sawaal pucho jisme DOOSRA sawaal pehle se juda ho.
#    Jaise:
#       "Mera naam Sarmesh hai"
#       "Mera naam kya hai?"        <- yaad hai?
#       "Usme kitne letter hai?"    <- "usme" kis cheez ka?
#
# 3. Har turn pe input_tokens dekho. Wo badh rahe hai ya same?
#    SOCHO: kyun?
#
# 4. Ab messages.append wali assistant line COMMENT kar do, aur dobara
#    wahi teen sawaal pucho. Ab kya hota hai?
#    (ye sabse zaroori experiment hai - zaroor karna)
#
# Chalane ke liye:  python chat.py

import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

# Poori baat-cheet yahan jama hoti hai - wahi list of dicts
messages = []

print("Chat shuru. Nikalne ke liye 'bye' likho.\n")

while True:
    user_input = input("Tum: ").strip()

    if user_input.lower() == "bye":
        print("Chalo, phir milte hai!")
        break

    if not user_input:
        continue

    # 1. User ka message history me daalo
    messages.append({"role": "user", "content": user_input})

    # 2. POORI history bhejo
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1000,
        system="Tum ek dost jaise Python teacher ho. Hinglish me, chhote jawab do.",
        messages= messages
    )

    # 3. Jawab print karo
    for block in response.content:
        if block.type == "text":
            print("Claude:", block.text)

    # 4. Claude ka jawab bhi history me daalo
    #    DHYAN: response.content daalna hai, sirf text NAHI
    messages.append({"role": "assistant", "content": response.content})

    # TODO: 
    print(response.usage.input_tokens)
    print(response.usage.output_tokens)

    print()
