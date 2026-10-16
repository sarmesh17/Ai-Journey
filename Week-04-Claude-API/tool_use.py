# Week 04 - Tukda 4 - TOOL USE (pehla)
#
# Pehle isko chalao aur OUTPUT dhyan se padho. Code baad me badlenge.
#
# KAAM:
#
# 1. Chalao jaisa hai. Output me dekho:
#    - kitni baar "--- API CALL" chhapa? (do sawaal ke liye kitne call?)
#    - Claude ne kya maanga, humne kya diya
#
# 2. Sawaal badal do: "Python kya hai?" poocho (jisme tool ki zaroorat nahi)
#    Ab kitne API call hue? stop_reason kya aaya?
#
# 3. Naya tool jodo: add_numbers(a, b) - do number jode
#    (tools list me definition, aur run_tool me handle karna)
#    Phir poocho: "456 aur 789 ka jod kya hai?"
#
# 4. Ab poocho: "abhi kitna baja hai, aur 100 + 250 kitna hota hai?"
#    Ek hi turn me Claude dono tool maang sakta hai? Dekho.
#
# Chalane ke liye:  python tool_use.py

from datetime import datetime
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()


# ----- 1. ASLI PYTHON FUNCTION (ye Claude nahi chalata, HUM chalate hai) -----

def get_current_time():
    return datetime.now().strftime("%d %B %Y, %H:%M:%S")


# ----- 2. CLAUDE KO BATANA KI KAUN SE TOOL HAI -----
# Ye sirf DESCRIPTION hai - code nahi. Claude isi se decide karta hai.

tools = [
    {
        "name": "get_current_time",
        "description": "Abhi ka date aur time deta hai. Jab user time, date, "
                       "'aaj', 'abhi' ke baare me puche tab isko call karo.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },

    {

      "name" : "add_number",
      "description":"Do number ko jodta hai.",
      "input_schema":{
        "type":"object",
        "properties":{

           "a": {"type":"number", "description":"phela number"},
           "b":{"type":"number","description":"doosra number"},

        },
        "required":["a","b"]
      }


    }
]


# ----- 3. NAAM SE ASLI FUNCTION CHALANA -----

def run_tool(name, tool_input):
    if name == "get_current_time":
        return get_current_time()
    elif name == "add_number":
        return sum_tool(
            tool_input["a"],
            tool_input["b"]
        )
    return f"Unknown tool: {name}"

def sum_tool(a,b):
    return str(a + b)
    


# ----- 4. LOOP -----

messages = [{"role": "user", "content": "add kardo 5 and 10 ko and abhi kitna baja hai ?"}]

call_number = 0

while True:
    call_number += 1
    print(f"\n--- API CALL {call_number} ---")

    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1000,
        tools=tools,
        messages=messages,
    )

    print("stop_reason:", response.stop_reason)

    # Claude ne tool nahi maanga = baat khatam
    if response.stop_reason != "tool_use":
        break

    # Claude ka turn history me daalo (tool_use block ke saath)
    messages.append({"role": "assistant", "content": response.content})

    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            print("  Claude ne maanga :", block.name, block.input)

            result = run_tool(block.name,block.input)
            print("  Humne jawab diya :", result)

            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,   # ye id match honi CHAHIYE
                "content": result,
            })

    # Tool ke jawab "user" message ban kar wapas jaate hai
    messages.append({"role": "user", "content": tool_results})


print("\n--- FINAL JAWAB ---")
for block in response.content:
    if block.type == "text":
        print(block.text)
