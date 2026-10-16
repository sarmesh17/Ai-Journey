# Week 04 - streaming.py
#
# Abhi tak: poora jawab ban-ne ka intezaar, phir ek saath print.
# Streaming: jaise-jaise Claude likhta hai, waise-waise dikhta hai.
#
# KAAM:
#
# 1. Neeche wala code chalao. Farq mehsoos karo.
#
# 2. Ab `flush=True` hata do aur dobara chalao. Kya badla?
#
# 3. Ab `end=""` hata do (flush wapas laga do). Kya hua? Kyun?
#
# 4. stream khatam hone ke baad ye add karo:
#
#        final = stream.get_final_message()
#        print()
#        print("stop_reason:", final.stop_reason)
#        print("usage:", final.usage)
#
#    (ye `with` block ke ANDAR hona chahiye - kyun? socho)
#
# 5. Ab chat.py ko streaming wala bana do (neeche hint hai)
#
# Chalane ke liye:  python streaming.py

import sys

import anthropic
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-opus-5-5",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Python me list aur dict ka farq 5 line me samjhao"}
    ],
) as stream:
    for text in stream.text_stream:
        print(text, end ="", flush=True)
    
    final = stream.get_final_message()
    print()
    print("stop_reason:", final.stop_reason)
    print("usage:", final.usage)





# ============================================
# POINT 5 KA HINT - chat.py me kya badlega
# ============================================
#
# PEHLE (chat.py me abhi ye hai):
#
#     response = client.messages.create(
#         model="claude-opus-5-5",
#         max_tokens=1000,
#         system="...",
#         messages=messages,
#     )
#
#     for block in response.content:
#         if block.type == "text":
#             print("Claude:", block.text)
#
#     messages.append({"role": "assistant", "content": response.content})
#
#
# BAAD ME (streaming ke saath):
#
#     print("Claude: ", end="", flush=True)
#
#     with client.messages.stream(
#         model="claude-opus-5-5",
#         max_tokens=1000,
#         system="...",
#         messages=messages,
#     ) as stream:
#         for text in stream.text_stream:
#             print(text, end="", flush=True)
#
#         response = stream.get_final_message()
#
#     print()
#     messages.append({"role": "assistant", "content": response.content})
#
# DHYAN: `response` ab bhi mil raha hai - get_final_message() se.
#        Isliye history wali line BILKUL waisi hi rehti hai.
