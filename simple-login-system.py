import time
import msvcrt as m


balance = 0
accountname = ""
email = ""

def registration():
    print("What is your name?")
    global accountname
    accountname = str(input(": "))
    print("What is your Email?")
    global email
    email = str(input(": "))
    Main.start()

def account():
    global accountname
    print("Username: " + accountname)
    global email
    print("Email:" + email)
    input("Press Enter to continue...")
    accountstats()

def accountstats():

    print("What do you want?")
    ("a = Account-Informations")
    print("a = Account-Informations")
    print("c = change creds")
    print("00 = go back")
    print("Your choice?")
    while True:
        accask = input()
        if accask.lower() == "a":
            account()
            accountstats()
        if accask.lower() == "c":
            credchanger()
        if accask.lower() == "00":
                Main.start()


class balancestats():

    def wishes():
        wish = input("Wish to see balance? (yes/no)")
        if wish == "yes":
            global accounname
            print("The balance of user" + accountname + "is" + str(balance) + "$")
            input("Press Enter to continue...")
            Main.start()
        if wish == "no":
            print("quitting")
            Main.start()
        else:
            balancestats()


def credchanger():
    print("What do you want?")
    print("a = change Name")
    print("b = change email")
    while True:
        accask = input()
        if accask.lower() == "a":
             print("Whats is your new name?")
             global accountname
             accountname = input(": ")
             print("Your Name has successfully changed to: " + accountname)
             input("Press Enter to continue...")
             Main.start()
        if accask.lower() == "c":
             print("Whats is your new Email?")
             global email
             email = input(": ")
             print("Your Email has successfully changed to: " + email)
             input("Press Enter to continue...")
             Main.start()

        else:
             credchanger()



def payin():
    while True:
        cash = input("How much $ do you have for indraw? ")
        awareness = input("You want to transfer " + str(cash) + "$" ", right?")
        if awareness == "yes":
            global balance
            balance = balance + int(cash)
            print("okay your balance is now " + str(balance) + "$" )
            input("Press Enter to continue...")
            Main.start()
            if awareness == "no":
                print("okay, quitting")
                Main.start()
            else:
                payin()


class Main:
    
    def start():     
        print("What do you want to see?")
        print("b = balance")
        print("i = add cash")
        print("a = Account")
        print("Your choice?")
        while True:
            ask = input()
            if ask.lower() == "b":
                balancestats.wishes()
                break
            if ask.lower() == "i":
                payin()
                break
            if ask.lower() == "a":
                accountstats()                       
            else:
                Main.start()
                   
                


registration()

