import time
import random
import machine
from Buzzer import *
from Button import *
from Displays import *
from Lights import *

class memory:
    

    def __init__(self):
        self.number = 0
        self.display = LCDDisplay(sda=16, scl=17, i2cid=0)
        self.button1 = Button(4,"1", buttonhandler =self)
        self.button2 = Button(5, "2", buttonhandler =self)
        self.button3 = Button(6, "3", buttonhandler =self)
        self.led1 = Light(0,"led1")
        self.led2 = Light(1,"led2")
        self.led3 = Light(2,"led3")
        #self.Text1=LCDDisplay("go", row=0, col=0)
        
        #self.Text2=LCDDisplay("over", row=0, col=0)
        #self.display()
        
        self.List_led = [self.led1,self.led2,self.led3]
        self.List_button = [self.button1,self.button2,self.button3]
        
     
        # Function to show a random sequence of LEDs
    def showsequence(self,x):
        print(x)
        for a in x:
            print(a)
            self.List_led[a].on()
            utime.sleep(1)
            self.List_led[a].off()
            utime.sleep(0.2)
    
    def get_player_sequence(self,x):
        player_sequence = []
        while len(player_sequence) < len(x):
            for i, button_pin in enumerate(self.List_button):
                if button_pin.isPressed(): 
                    player_sequence.append(i)
                    utime.sleep(0.3)  # Debounce
        return player_sequence

    def run(self):
        self.display.showText("Go", row=0, col=0)
        while True:
            sequence = [random.randint(0, 2) for _ in range(5)]
            memory.showsequence(self,sequence)
            b=memory.get_player_sequence(self,sequence)
            print(sequence,b)
            if b == sequence:
                self.display.showText("won", row=0, col=0) 
            else:
                self.display.showText("over", row=0, col=0) 
                break
    


   