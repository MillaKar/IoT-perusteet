import time
time.sleep(0.1) # Wait for USB to become ready

print("Asking names...")
name = input("Input your name: ")
if name == ("Milla"):
    print("Wow, you're awesome!")
else:
    print("Okay...")
