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
        #Define LCD display
        self.display = LCDDisplay(sda=16, scl=17, i2cid=0)

        #created button with pin no and button handler
        self.button1 = Button(22,"1", buttonhandler =self)
        self.button2 = Button(26, "2", buttonhandler =self)
        self.button3 = Button(27, "3", buttonhandler =self)
        self.button4 = Button(28, "4", buttonhandler =self)
        self.led1 = Light(0,"led1")
        self.led2 = Light(2,"led2")
        self.led3 = Light(3,"led3")
        self.led4 = Light(6,"led4")

        #Created a led light with pin no
        self.led1 = Light(0,"led1")
        self.led2 = Light(2,"led2")
        self.led3 = Light(3,"led3")
        self.led4 = Light(6,"led4")
        
        self.List_led = [self.led1,self.led2,self.led3,self.led4]
        self.List_button = [self.button1,self.button2,self.button3,self.button4]
        self.score1 = 0
        self.score2 = 0

    def beep(self, tone=500, duration=150):
        print(f"Beeping the buzzer at {tone}hz for {duration} ms")
        self.play(tone)
        time.sleep(duration / 1000)
        self.stop()

    
        # Function to show a random sequence of LEDs
    def showsequence(self,x):
        #print(x)
        for a in x:
            #print(a)
            self.List_led[a].on()
            utime.sleep(1)
            self.List_led[a].off()
            utime.sleep(0.4)

     #Function to get the input from player its only one player game .
 
    
    def get_player_sequence(self,x):
        player_sequence = []
        while len(player_sequence) < len(x):
            for i, button_pin in enumerate(self.List_button):
                if button_pin.isPressed(): 
                    player_sequence.append(i)
                    utime.sleep(0.4)  # Debounce
        return player_sequence
        

    #Function to compare the sequence of led numbers with player input sequence
    # If the sequence matches we get  "won" in display
    #If the sequence doesn't match then "over" is shown in the display
     

    def run(self):
        self.display.showText("go", row=0, col=0)
        utime.sleep(0.5)
        while True:
            utime.sleep(0.8)
            
            sequence = [random.randint(0, 3) for _ in range(4)]
            self.display.showText("Player 1", row=0, col=0)
            memory.showsequence(self,sequence)
            b=memory.get_player_sequence(self,sequence)
            if b == sequence:
                self.score1 += 1 
            else:
                utime.sleep(0.5)
                self.display.showText(f"Score: {self.score1}", row=0, col=0)
                break
        while True:
            utime.sleep(0.5)
            sequence = [random.randint(0, 3) for _ in range(4)]
            self.display.showText("Player 2", row=0, col=0)
            memory.showsequence(self,sequence)
            b=memory.get_player_sequence(self,sequence)
            if b == sequence:
                self.score2 += 1 
            else:
                utime.sleep(0.5)
                self.display.showText(f"Score: {self.score2}", row=0, col=0)
                break    
        if self.score1 > self.score2:
            utime.sleep(0.5)
            self.display.showText(f"Player 1 won", row=0, col=0)
        elif self.score1 < self.score2:
            self.display.showText(f"Player 2 won", row=0, col=0)
        else:
            self.display.showText(f"Equal score", row=0, col=0)



   

   