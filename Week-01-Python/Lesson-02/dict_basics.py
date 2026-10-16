# Lesson 02 - Tukda 3 - dict_basics.py
#
# KAAM (ek-ek point tick karte jaana):
#
# 1. Ek dict banao apne baare me - 4 key: name, age, city, language
# 2. Usme se sirf name aur city print karo
# 3. age ko 1 saal badha do (hint: user["age"] = user["age"] + 1)
# 4. Ek naya key add karo: "framework" -> "Flutter"
# 5. Ek key jo dict me NAHI hai, usko [] se print karne ki koshish karo.
#    KeyError apni aankhon se dekho. Error dekhne ke baad us line ko
#    comment kar do (line ke aage # laga do) taaki aage ka code chale.
# 6. Wahi missing key .get() se print karo - do tarah se:
#       - bina default (None aayega)
#       - default ke saath (apna message aayega)
# 7. Aakhir me poora dict print karo
#
# Chalane ke liye:  python dict_basics.py

# Yahan se likhna shuru karo:

about_me={'name': 'Sarmesh','age' : 7,'city': 'Birgunj','language': 'Bhojpuri'}

print(about_me['name'])
print(about_me['city'])
about_me['age']=about_me['age'] + 1
print(about_me['age'])
about_me['framework'] = 'flutter'
#print(aboutMe['version'])
print(about_me.get('version'))
print(about_me.get('version','key nahi mila malik'))
print(about_me)






