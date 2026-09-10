import time
import winsound

def countdownS(study):
    while study:
        mins, secs = divmod(study, 60)
        timer = '{:02d}{:02d}'.format(mins, secs)

        print(timer, end='\r')
        time.sleep(1)
        study-=1
    winsound.Beep(500, 500)     
    print("Time's up! Take a break!")
    


def countdownR(rest):
    while rest:
        mins, secs = divmod(rest, 60)
        timer = '{:02d}{:02d}'.format(mins, secs)

        print(timer, end='\r')
        time.sleep(1)
        rest-=1
    winsound.Beep(750, 500)
    print("Time's up! Back on the grind!")
    



def sessionCount(amount):
    while (amount != 0):
        countdownS(int(study))
        time.sleep(1)
        countdownR(int(rest))
        time.sleep(1)
        amount -= 1
    print("\n\n!! Study Session Over !! \nYou did it! Congrats!\n\n")




print("~~ Welcome to YourPomo! ~~\n\n")

study = int(input("How long would you like to study (in seconds)? "))
rest = int(input("\n How long would you like to rest (in seconds)? "))
amount = int(input("\nAlright, and how many rounds? (1 round = study + rest): "))

print("\n\nOK! Ready, set... STUDY!")
time.sleep(1)

sessionCount(amount)