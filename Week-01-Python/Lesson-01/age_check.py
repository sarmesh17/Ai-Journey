# Exercise 2 - age_check.py
#
# KAAM:
# User se umar input() se lo (int() lagana mat bhoolna).
# Phir batao:
#   18 ya zyada  -> "Adult ho"
#   13 se 17     -> "Teenager ho"
#   13 se kam    -> "Bachcha ho"
#
# Hint: Python me "else if" nahi hota, "elif" hota hai.
# Indentation 4 space - colon ke baad andar.
#
# Chalane ke liye:  python age_check.py

# Yahan se likhna shuru karo:

age = int( input('age bato aapna: '))


if age >= 18:
    print('You are Adult')
elif age >= 13:
    print('You are teeneger')
else:
    print('you are child')
