import os, sys
try:
    import requests
    from colorama import Fore
except:
    print("Module requests not found")
        

VERSION = "0.9.0"

API = "https://lookup.binlist.net/"

def banner():
    print(Fore.BLUE + "                              ________")
    print(Fore.CYAN + "                          ,o88~~88888888o,")
    print(Fore.GREEN + "                        ,~~?8P  88888     8,")
    print(Fore.YELLOW + "                       d  d88 d88 d8_88     b")
    print(Fore.YELLOW + "                      d  d888888888          b")
    print(Fore.RED + "                      8,?88888888  d8.b o.   8")
    print(Fore.YELLOW + "                      8~88888888~ ~^8888\ db 8")
    print(Fore.YELLOW + "                      ?  888888          ,888P")
    print(Fore.GREEN + "                        `   8888888b   ,888'")
    print(Fore.CYAN + "                          ~-?8888888 _.P-~ ")
    print(Fore.BLUE + "                               ~~~~~~")

def clean():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def check(cardNum):
    try:
        data = requests.get(API+cardNum).json()
        sys.stdout.flush()
        Fore.YELLOW
        print(Fore.RED + "\n\n CC Info \n")
        print(Fore.YELLOW + "\n [Country] " + data['country']['name'])
        print("\n [Sheme] " + data['scheme'])
        print("\n [Type] " + data['type'])
        print("\n [Brand] " + data['brand'])
        print("\n [Bank name] " + data['bank']['name'])
        print("\n [Latitude] " + data['latitude'])
        print("\n [Longitude] " + data['longitude'])
    except:
        pass


if __name__ == '__main__':
    clean()
    banner()
    cardNum = input(" CC -> ")
    check(cardNum)