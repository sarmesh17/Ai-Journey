# Key load ho rahi hai ya nahi - ye check karta hai
# Koi API call NAHI karta, isliye paisa kharch nahi hoga

import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("ANTHROPIC_API_KEY")

if key:
    # Poori key kabhi print mat karo - sirf shuru aur aakhir
    print("Key mil gayi:", key[:10] + "..." + key[-4:])
    print("Lambai:", len(key))
else:
    print("Key NAHI mili - .env file check karo")
