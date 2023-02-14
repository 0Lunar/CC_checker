import os, sys
try:
    import requests
except:
    print("Module requests not found")
        

VERSION = "0.9.0"

API = "https://lookup.binlist.net/"

def banner():
    print('''                              ________
                          ,o88~~88888888o,
                        ,~~?8P  88888     8,
                       d  d88 d88 d8_88     b
                      d  d888888888          b
                      8,?88888888  d8.b o.   8
                      8~88888888~ ~^8888\ db 8
                      ?  888888          ,888P
                       ?  `8888b,_      d888P
                        `   8888888b   ,888'
                          ~-?8888888 _.P-~ 
                               ~~~~~~
    ''')

def clean():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def check(cardNum):
    try:
        data = requests.get(API+cardNum).json()
        sys.stdout.flush()
        print("\n\n CC Info \n")
        print("\n [Country] " + data['country']['name'])
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
