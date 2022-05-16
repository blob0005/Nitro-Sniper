reqerror = False
colorerror = False
anyerror = False
try:
    import requests
except Exception:
    reqerror = True
    anyerror = True
try:
    import colorama
except Exception:
    print("e")
    colorerror = True
    anyerror = True

if anyerror == True:
    while True:
        fix = input("Missing Modules, Wanna Try To Auto Fix (y/n): ")
        if fix == "y" or fix == "n":
            break
        else:
            print("Enter A Valid Choice")
    if fix == "n":
        print("Press Enter To Close The Program")
        input("")
        exit()
    if fix == "y":
        try:
            import os
            os.system("pip install requests")
            os.system("pip install colorama")
        except Exception:
            print("Error While Fixing, Add blob#0005 For Help :)")
            input("")
            exit()
        print("Hopefully The Errors Shod Be Fixed, Restart The Program")
        input("")
        exit()
import random
import time
colorama.init(autoreset=True)
def valid():
    print("Enter A Valid Choice")
    return
while True:
    autocheck = input("Want To Auto Check (y/n): ")
    if autocheck == "y" or autocheck == "n":
        break
    else:
        valid()
while True:
    try:
        delay = input("Enter Delay: ")
        delay = float(delay)
        break
    except Exception:
        valid()
while True:
    save = input("Auto Save (y/n): ")
    if save == "n" or save == "y":
        break
    else:
        valid()
while True:
    try:
        limit = input("Enter Limit: ")
        limit = int(limit)
        break
    except Exception:
        valid()
if autocheck == "y":
    while True:
        autowehook = input("Want Send Valid Codes To An Webhook (y/n): ")
        if autowehook == "y" or autowehook == "n":
            break
        else:
            valid()
    if autowehook == "y":
        while True:
            try:
                webhook = input("Enter Webhook: ")
                re = requests.get(webhook)
                re = str(re)
                if "200" in re:
                    break
                else:
                    print("Webhook Is Invalid")
            except Exception:
                print("Webhook Invalid")
if autocheck == "n":
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    done = 0
    while True: 
        n1 = random.choice(choices)
        n2 = random.choice(choices)
        n3 = random.choice(choices)
        n4 = random.choice(choices)
        n5 = random.choice(choices)
        n6 = random.choice(choices)
        n7 = random.choice(choices)
        n8 = random.choice(choices)
        n9 = random.choice(choices)
        n10 = random.choice(choices)
        n11 = random.choice(choices)
        n12 = random.choice(choices)
        n13 = random.choice(choices)
        n14 = random.choice(choices)
        n15 = random.choice(choices)
        n16 = random.choice(choices)
        code = f"{n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}{n9}{n10}{n11}{n12}{n13}{n14}{n15}{n16}"
        done = int(done) + 1 
        print(f"[{str(done)}] Generated Code: https://discord.gift/" + code)
        if save == "y":
            file = open("unchecked_nitro_codes.txt", "a")
            file.writelines("https://discord.gift/"+code+"\n")
            file.close()
        if int(done) == int(limit):
            print("Done, Press Enter To Close Program")
            input("")
            exit()
        time.sleep(float(delay))
if autocheck == "y":
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    done = 0
    while True: 
        n1 = random.choice(choices)
        n2 = random.choice(choices)
        n3 = random.choice(choices)
        n4 = random.choice(choices)
        n5 = random.choice(choices)
        n6 = random.choice(choices)
        n7 = random.choice(choices)
        n8 = random.choice(choices)
        n9 = random.choice(choices)
        n10 = random.choice(choices)
        n11 = random.choice(choices)
        n12 = random.choice(choices)
        n13 = random.choice(choices)
        n14 = random.choice(choices)
        n15 = random.choice(choices)
        n16 = random.choice(choices)
        code = f"{n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}{n9}{n10}{n11}{n12}{n13}{n14}{n15}{n16}"
        r1 = requests.get("https://discordapp.com/api/v6/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
        r1 = str(r1)
        done = int(done) + 1
        if "200" in r1:
            print(colorama.Fore.GREEN + f"[{str(done)}] Generated Valid Code: https://discord.gift/" + code)
            if save == "y":
                file = open("valid_nitro_codes.txt", "a")
                file.writelines("https://discord.gift/"+code+"\n")
                file.close()
            while True:
                r2 = requests.post(webhook, json={"username": "Nitro Sniper", "content": "@everyone **Sniped A New Code:** "+code})
                r2 = str(r2)
                if "204" in r2:
                    print("Sent Code To Webhook")
                    break
                else:
                    print("Ratelimited, Retrying...")

        if "200" not in r1:
            print(colorama.Fore.RED + f"[{str(done)}] Generated Invalid Code: https://discord.gift/" + code)
            if save == "y":
                file = open("invalid_nitro_codes.txt", "a")
                file.writelines("https://discord.gift/"+code+"\n")
                file.close()
        if int(done) == int(limit):
            print("Done, Press Enter To Close Program")
            input("")
            exit()
        time.sleep(float(delay))
