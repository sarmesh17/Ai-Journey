# Lesson 04 - Tukda 3 - comprehension.py
#
# Har point me: pehle normal loop se likho, phir comprehension se.
# Dono ka output print karo - dono SAME aana chahiye. Wahi proof hai.
#
# Ye data use karo:
#
# hardware = ['cpu', 'keyboard', 'mouse', 'monitor', 'ram']
# nums = [1, 5, 8, 12, 3, 20]
# messages = [
#     {"role": "user", "text": "hello"},
#     {"role": "ai", "text": "hi, kaise ho?"},
#     {"role": "user", "text": "python seekh raha hu"},
# ]
#
# KAAM:
#
# 1. hardware ki sab cheezein CAPITAL me - ek nayi list banao
#    (pehle loop se, phir comprehension se, dono print)
#
# 2. nums me se sirf 10 se bade number ki list
#
# 3. nums ke har number ka double
#
# 4. messages me se sirf "user" wale messages ki list
#
# 5. messages ko "role: text" string ki list me badlo
#
# 6. hardware me se sirf wo jinme letter 'o' aata hai
#    (hint: 'o' in item  --  ye True/False deta hai)
#
# 7. Ab sochne wala: nums me se sirf EVEN number, aur unka square
#    (hint: ek comprehension me badalna aur chaanna dono ho sakta hai)
#
# Chalane ke liye:  python comprehension.py

# Yahan se likhna shuru karo:

#normal loop

capital_hardware = []

for item in hardware:
    capital_hardware.append( item.upper())
    print(capital_hardware)

# comprehension

result2 = [item.upper() for item in hardware]
print(result2)


# Lesson 04 - Tukda 3 - comprehension.py

hardware = ['cpu', 'keyboard', 'mouse', 'monitor', 'ram']
nums = [1, 5, 8, 12, 3, 20]

messages = [
    {"role": "user", "text": "hello"},
    {"role": "ai", "text": "hi, kaise ho?"},
    {"role": "user", "text": "python seekh raha hu"},
]

# 1. Hardware ko CAPITAL me convert karo

# Normal loop
capital_hardware = []

for item in hardware:
    capital_hardware.append(item.upper())

print("1. Normal loop:", capital_hardware)

# List comprehension
result1 = [item.upper() for item in hardware]

print("1. Comprehension:", result1)


# 2. Sirf 10 se bade numbers

# Normal loop
greater_than_10 = []

for num in nums:
    if num > 10:
        greater_than_10.append(num)

print("\n2. Normal loop:", greater_than_10)

# List comprehension
result2 = [num for num in nums if num > 10]

print("2. Comprehension:", result2)


# 3. Har number ka double

# Normal loop
doubles = []

for num in nums:
    doubles.append(num * 2)

print("\n3. Normal loop:", doubles)

# List comprehension
result3 = [num * 2 for num in nums]

print("3. Comprehension:", result3)


# 4. Sirf user wale messages

# Normal loop
user_messages = []

for message in messages:
    if message["role"] == "user":
        user_messages.append(message)

print("\n4. Normal loop:", user_messages)

# List comprehension
result4 = [
    message for message in messages
    if message["role"] == "user"
]

print("4. Comprehension:", result4)


# 5. Messages ko "role: text" strings me badlo

# Normal loop
formatted_messages = []

for message in messages:
    formatted_messages.append(
        f'{message["role"]}: {message["text"]}'
    )

print("\n5. Normal loop:", formatted_messages)

# List comprehension
result5 = [
    f'{message["role"]}: {message["text"]}'
    for message in messages
]

print("5. Comprehension:", result5)


# 6. Hardware me se jinme letter 'o' hai

# Normal loop
hardware_with_o = []

for item in hardware:
    if 'o' in item:
        hardware_with_o.append(item)

print("\n6. Normal loop:", hardware_with_o)

# List comprehension
result6 = [item for item in hardware if 'o' in item]

print("6. Comprehension:", result6)


# 7. Even numbers ke squares

# Normal loop
even_squares = []

for num in nums:
    if num % 2 == 0:
        even_squares.append(num ** 2)

print("\n7. Normal loop:", even_squares)

# List comprehension
result7 = [num ** 2 for num in nums if num % 2 == 0]

print("7. Comprehension:", result7)
