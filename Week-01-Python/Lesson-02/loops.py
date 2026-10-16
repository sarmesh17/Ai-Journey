# Lesson 02 - Tukda 2 - loops.py
#
# KAAM:
# 1. Wahi hardware list banao (ya nayi list, kuch bhi)
# 2. for loop se har cheez print karo - aise:  "1 - cpu"  ... nahi,
#    pehle simple: sirf "cpu", "keyboard" ... har line pe ek
# 3. Ek loop se list ki saari cheezein CAPITAL me print karo
#    (hint: .upper() string pe lagta hai)
# 4. range() wala loop: 1 se 5 tak ginti print karo
# 5. Ek loop likho jo list me se sirf un cheezon ko print kare
#    jinka naam 5 letter se bada hai  (hint: loop ke andar if)
#
# Chalane ke liye:  python loops.py

# Yahan se likhna shuru karo:

hardware = ['cpu','keyboard','mouse','monitor']



for index, item in enumerate(hardware):
    print(f'{index} - {item}')

for item in hardware:
    print(item.upper())

for i in range(1,6):
    print(i)

for items in hardware:
    if len(items) > 5:
        print(items)

hardware.remove('cpu')

print(hardware)