# Lesson 03 - Tukda 1 - functions.py
#
# KAAM (ek-ek point tick karte jaana):
#
# 1. def greet(name) banao - andar print kare "Namaste, <name>!"
#    Phir use do baar call karo, do alag naam se
#
# 2. def add(a, b) banao - jo jod ke RETURN kare (print nahi)
#    Call karke result ek variable me rakho, phir print karo
#
# 3. def shout(text) banao - jo sirf print kare, return na kare
#    Ab print(shout("hello")) karo - kya aata hai? Dhyan se dekho.
#
# 4. def greet2(name, lang="hindi") banao - default parameter wala
#    Do baar call karo: ek bar lang diye bina, ek bar lang="english" ke saath
#
# 5. def long_words(items) banao - list leta hai, aur un cheezon ki
#    LIST return karta hai jinke naam 5 letter se bade hai
#    (hint: andar khaali list banao, loop+if, append, phir return)
#
# 6. def only_user(messages) banao - Lesson 02 wali messages list leta hai,
#    aur sirf role == "user" wale messages ki list return karta hai
#
# Chalane ke liye:  python functions.py

# Yahan se likhna shuru karo:

def name(name):
    print(f'my name is {name}')

name('sarmesh')
name('rajan')

def add(a,b):
    return a+b

total= add(5,10)
print(total)

def shout(text):
    print(text)

print(shout('hello'))
def greet2(name,language='hinglish'):
    print(f'{name}, {language}')

greet2('Rahul')
greet2('Sarmesh','English')


def long_word(items):
    result =[]
    for item in items:
        if len(item) > 5:
            result.append(item)
    return result

hardware = ['cpu','keyboard','mouse','monitor']

long_word(hardware)

users=[

   {"role": "user", "text": "hello"},
  {"role": "ai", "text": "hi, kaise ho?"},
  {"role": "user", "text": "python seekh raha hu"},

]

def only_user(message):
    result = []
    for item in message:
         if item["role"] == "user":

          result.append(item)
    return result


only_user(users)