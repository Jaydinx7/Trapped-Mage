
import os
import sys
import time
from typewriter import typewriter
from loading_bar import loading_bar


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Example game flow
clear()
print("""



    ███        ▄████████    ▄████████    ▄███████▄    ▄███████▄    ▄████████ ████████▄          ▄▄▄▄███▄▄▄▄      ▄████████    ▄██████▄     ▄████████
▀█████████▄   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███   ▀███       ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███   ███    ███
   ▀███▀▀██   ███    ███   ███    ███   ███    ███   ███    ███   ███    █▀  ███    ███       ███   ███   ███   ███    ███   ███    █▀    ███    █▀ 
    ███   ▀  ▄███▄▄▄▄██▀   ███    ███   ███    ███   ███    ███  ▄███▄▄▄     ███    ███       ███   ███   ███   ███    ███  ▄███         ▄███▄▄▄    
    ███     ▀▀███▀▀▀▀▀   ▀███████████ ▀█████████▀  ▀█████████▀  ▀▀███▀▀▀     ███    ███       ███   ███   ███ ▀███████████ ▀▀███ ████▄  ▀▀███▀▀▀    
    ███     ▀███████████   ███    ███   ███          ███          ███    █▄  ███    ███       ███   ███   ███   ███    ███   ███    ███   ███    █▄ 
    ███       ███    ███   ███    ███   ███          ███          ███    ███ ███   ▄███       ███   ███   ███   ███    ███   ███    ███   ███    ███
   ▄████▀     ███    ███   ███    █▀   ▄████▀       ▄████▀        ██████████ ████████▀         ▀█   ███   █▀    ███    █▀    ████████▀    ██████████
              ███    ███                                                                                                                            


      
""")
input("""
      
 ▄▄▄·▄▄▄  ▄▄▄ ..▄▄ · .▄▄ ·     ▄▄▄ . ▐ ▄ ▄▄▄▄▄▄▄▄ .▄▄▄      ▄▄▄▄▄          .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▄  ▄▄▄▄▄     ▄· ▄▌      ▄• ▄▌▄▄▄       ▐▄▄▄      ▄• ▄▌▄▄▄   ▐ ▄ ▄▄▄ . ▄· ▄▌        
▐█ ▄█▀▄ █·▀▄.▀·▐█ ▀. ▐█ ▀.     ▀▄.▀·•█▌▐█•██  ▀▄.▀·▀▄ █·    •██  ▪         ▐█ ▀. •██  ▐█ ▀█ ▀▄ █·•██      ▐█▪██▌▪     █▪██▌▀▄ █·      ·██▪     █▪██▌▀▄ █·•█▌▐█▀▄.▀·▐█▪██▌        
 ██▀·▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄    ▐▀▀▪▄▐█▐▐▌ ▐█.▪▐▀▀▪▄▐▀▀▄      ▐█.▪ ▄█▀▄     ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄  ▐█.▪    ▐█▌▐█▪ ▄█▀▄ █▌▐█▌▐▀▀▄     ▪▄ ██ ▄█▀▄ █▌▐█▌▐▀▀▄ ▐█▐▐▌▐▀▀▪▄▐█▌▐█▪        
▐█▪·•▐█•█▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█    ▐█▄▄▌██▐█▌ ▐█▌·▐█▄▄▌▐█•█▌     ▐█▌·▐█▌.▐▌    ▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█•█▌ ▐█▌·     ▐█▀·.▐█▌.▐▌▐█▄█▌▐█•█▌    ▐▌▐█▌▐█▌.▐▌▐█▄█▌▐█•█▌██▐█▌▐█▄▄▌ ▐█▀·.        
.▀   .▀  ▀ ▀▀▀  ▀▀▀▀  ▀▀▀▀      ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀     ▀▀▀  ▀█▄▀▪     ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀ ▀▀▀       ▀ •  ▀█▄▀▪ ▀▀▀ .▀  ▀     ▀▀▀• ▀█▄▀▪ ▀▀▀ .▀  ▀▀▀ █▪ ▀▀▀   ▀ •  ▀  ▀  ▀
""")
clear()

loading_bar("Loading world...")
time.sleep(1)
clear()

time.sleep(5)
typewriter("“You have wandered too far, mortal soul…”")
time.sleep(1)
input()
clear()

typewriter("(A faint light shimmers, forming a celestial figure.)")
time.sleep(1)
input()
clear()

print("Goddess:",end=" ")
typewriter("“Once, I offered you mercy. But mercy was not enough to change your fate.”")
time.sleep(1)
input()
clear()

print("Goddess:",end=" ")
typewriter("“Now, you shall carry the mark of my curse — until your will proves stronger than your doom.”")
time.sleep(1)
input()
clear()

typewriter("You awaken in a misty forest...")
time.sleep(1)
input()
clear()

typewriter("You awaken in a misty forest...")
time.sleep(1)
input()
clear()



# (Black screen. A low hum fades in — whispers echo faintly. A heartbeat… then silence.)
# Narrator / Goddess (soft, ethereal voice):
# “You have wandered too far, mortal soul…”
# (A faint light shimmers, forming a celestial figure.)
# Goddess:
# “Once, I offered you mercy. But mercy was not enough to change your fate.”
#  “Now, you shall carry the mark of my curse — until your will proves stronger than your doom.”
# (A blinding flash — the screen cracks like glass, then fades to darkness again.)
# Sound: A gasp. The sound of stone scraping. Books falling.
# Text on screen:
# You awaken among the ruins of a forgotten library... deep beneath the earth.
# (Flickering torchlight reveals ancient tomes, chains, dust in the air...)
# MC (whispering):
# “...Where… am I?”
# (The music swells. Title fades in.)
# [Game Title]











































































































































































# from inputimeout import inputimeout, TimeoutOccurred










































































































































# import time

# timeout = 10  # total time allowed in seconds
# start_time = time.time()
# inputs = []

# print(f"You have {timeout} seconds to enter multiple inputs.")

# while True:
#     remaining = timeout - (time.time() - start_time)
#     if remaining <= 0:
#         print("Time is up!")
#         break
    
#     try:
#         # Set timeout for each input as the remaining time
#         answer = inputimeout(prompt=f"Enter input (time left {int(remaining)}s): ", timeout=remaining)
#         inputs.append(answer)
#     except TimeoutOccurred:
#         print("\nTime is up!")
#         break

# print("Your inputs:", inputs)
