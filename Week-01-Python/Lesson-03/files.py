# Lesson 03 - Tukda 2 - files.py
#
# KAAM (ek-ek point tick karte jaana):
#
# 1. "w" mode se notes.txt me 3 line likho (har line ke aakhir me \n lagana)
#
# 2. "r" mode se poori file ek saath padho aur print karo
#
# 3. Line-by-line loop se padho, .strip() ke saath print karo
#
# 4. "a" mode se ek nayi line add karo. Phir dobara padho -
#    4 line dikhni chahiye (purani 3 + nayi 1)
#
# 5. AB DHYAN SE: "w" mode se sirf ek line likho ("test") aur dobara padho.
#    Purani 4 line ka kya hua? Apni aankhon se dekho.
#    (ye jaan-boojh ke data udana hai - taaki aage galti se na ho)
#
# 6. def save_messages(messages, filename) banao -
#    messages list ko file me "role: text" format me likhe, har line pe ek
#    Phir aise call karo:   save_messages(messages, "chat.txt")
#    Aur chat.txt VS Code me khol ke dekho - 3 line sahi likhi hai ya nahi
#
# 7. def load_lines(filename) banao -
#    file ki saari line ek LIST me return kare (har line .strip() ki hui)
#    Phir aise call karo:   print(load_lines("chat.txt"))
#    Wahi 3 line list ban kar wapas aani chahiye
#
# messages list ye use karo:
#

#
# Chalane ke liye:  python files.py
#
# NOTE: notes.txt apne aap ban jaayegi, tumhe banani nahi hai

# Yahan se likhna shuru karo:



with open("notes.txt", "w") as file:
    file.write("pheli line\n")
    file.write("dusri line\n")
    file.write("teesri line\n")

with open("notes.txt","r") as file:
    content = file.read()
    print(content)

with open("notes.txt", "r") as file:
    for line in file:
     print(line.strip())

with open("notes.txt", "a") as file:
   file.write("fourth line\n")

with open("notes.txt", "r") as file:
   content= file.read()
   print(content)

with open("notes.txt","w") as file:
   file.write('test\n')

with open("notes.txt","r") as file:
   print(file.read())


messages = [
     {"role": "user", "text": "hello"},
     {"role": "ai", "text": "hi, kaise ho?"},
     {"role": "user", "text": "python seekh raha hu"},
    ]

def save_message(messages, filename):
   with open(filename,"w") as file:
      for msg in messages:
         file.write(f"{msg["role"]}: {msg["text"]}\n")

save_message(messages, "chat.txt")

def load_line(filename):
   result = []
   with open(filename,"r") as file:
      for msg in file:
         result.append(msg.strip())
   return result

print(load_line("chat.txt"))