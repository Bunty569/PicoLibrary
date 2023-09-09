# main.py
import time
from memory import *
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

counter = memory()
counter.run()


