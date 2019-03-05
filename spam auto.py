import keyboard
import string
import random
import time
spam = list(string.ascii_lowercase)
length = random.randint(3,50)
interval = eval(input("Interval?"))
times = eval(input("How many times?"))
for i in range (times):
    for i in range(length):
        keyboard.write(random.choice(spam))
    keyboard.press_and_release("enter")
    length = random.randint(8,15)
    time.sleep(interval)
    


    
