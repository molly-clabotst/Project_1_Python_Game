import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def main():
    
    die = Die()

    posConsent = "r"
    isHuman = True

    loosingRoll = 1
    initRoll = 2
    winCond = 20

    humanTally = 0
    computerTally = 0
    

    userConsent = input("Welcome to Piggy the dice game. Press 'R' to play.  ")

# Game play Loop
    while userConsent.lower() == posConsent:
        result = initRoll
        rawl = 'r'

# Rolling loop
        while humanTally!=winCond and computerTally!=winCond and rawl.lower()=="r":
            result = die.roll()
            # Human Rolls            
            if isHuman:
                rawl = ''
                if result != loosingRoll:
                    humanTally+=result
                    print(f"\nCongrats you got a {result}, your score is now {humanTally}.")
                    if humanTally>=winCond:
                        print("\nCongrats you won!\n\n")
                    else:
                        rawl = input("Press 'R' to roll again.  ")
                else:
                    print("\nUuu, you got a 1. Your turn is over\n\n")
                    rawl = 'r'  
                    isHuman=False
            # Computer rolls
            else:
                if result != loosingRoll:
                    computerTally+=result
                    print(f"Woo, I'm a computer and I got a good roll.\nMy score is {computerTally}")
                    if computerTally>=winCond:
                        rawl = ''
                        print("\nWoooo! I won!\n\n")
                else:
                        print("Bummer, I got a 1. This computers' turn is over!\n")
                        isHuman=True
            


        userConsent = input("Press 'R' to play again.  ")          

main()