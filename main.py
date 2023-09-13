import requests
import os 
import colorama
from colorama import Fore
import time

y = Fore.CYAN
w = Fore.MAGENTA
r = Fore.RED


def banner():
  print(f"""{w}
  
        ██╗░░██╗░█████╗░██╗███████╗░█████╗░██╗░░██╗██╗░░░██╗
        ██║░██╔╝██╔══██╗██║╚════██║██╔══██╗██║░██╔╝██║░░░██║
        █████═╝░███████║██║░░███╔═╝██║░░██║█████═╝░██║░░░██║
        ██╔═██╗░██╔══██║██║██╔══╝░░██║░░██║██╔═██╗░██║░░░██║
        ██║░╚██╗██║░░██║██║███████╗╚█████╔╝██║░╚██╗╚██████╔╝
        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░╚═════╝░
        Copyright © 2023 github.com/n1rox1337 / dc: n1_rox
            """)
banner()

key = input(f'{y}[?] Key : ')
password = input(f'{y}[?] Password : ')

def resetcreds():
  print(f"{r}[!] THE PASSWORD YOU ENTERED IS WRONG! PLEASE TRY AGAIN OR RESET IT BY FILLING THE DETAILS GIVEN BELOW!")
  productkey = input(F'{w}[?] Product Key : ')
  newpassword = input(F'{w}[?] New Password : ')
  embed = {
            "avatar_url":"https://media.discordapp.net/attachments/869954417540104273/907033501554073680/Screenshot_20211107-162536_YouTube.jpg?width=609&height=430",
            "embeds": [
                {
                    "author": {
                        "name": "Kaizoku Webhook Tool",
                        "icon_url": "https://media.discordapp.net/attachments/869954417540104273/907033501554073680/Screenshot_20211107-162536_YouTube.jpg?width=609&height=430"
                    },
                    "description": f"**CREDS RESET **\n```Product Key : {productkey}\nNew Password : {newpassword}```",
                    "color": 0,

                    "thumbnail": {
                      "url": "https://media.discordapp.net/attachments/869954417540104273/907033501554073680/Screenshot_20211107-162536_YouTube.jpg?width=609&height=430"
                    },       

                    "footer": {
                      "text": "© github.com/n1rox1337"
                    }
                }
            ]
        }
  requests.post("https://discord.com/api/webhooks/1151633786128322651/fwu9yJ-E3tUsg3p5Oo8H2W9eCm4NnETeCPfP_3c_kVN3I24llJcleVkhG0JjkL-vs8Nn", json=embed)
  print("Request Sent! Please wait, our team will contact you soon.")

def spam():
    webhook = input(f"{w}[>] WEBHOOK URL : ")
    message = input(f"{w}[>] MESSAGE TO SPAM : ")
    while True:
        try:
            r = requests.post(webhook, json={'content': message})
            if r.status_code == 204:
                print(f'{y}[!] Sent  {message} TO {webhook}')
        except:
            print(f"{r}INVALID :" + webhook)
            time.sleep(2)
            os.system('cls')
            Panel()

def sendmsg():
    webhook = input(f"{w}[>] WEBHOOK URL : ")
    message = input(f"{w}[>] MESSAGE TO SEND : ")
    try:
            r = requests.post(webhook, json={'content': message})
            if r.status_code == 204:
                print(f'{y}[!] Sent  {message} TO {webhook}')
    except:
        print(f"{r}INVALID :" + webhook)
        time.sleep(2)
        os.system('cls')
        Panel()

def dlt():
    webhook = input(f"{w}[>] WEBHOOK URL : ")
    try:
            r = requests.delete(webhook)
            if r.status_code == 204:
                print(f'{y}[!] SUCCESSFULLY DELETED WEBHOOK : {webhook}')
                time.sleep(3)
    except:
        print(f"{r}INVALID :" + webhook)
        time.sleep(2)
        os.system('cls')
        Panel()

pastebin = "https://pastebin.com/raw/Hw7W3iJm"
response = requests.get(pastebin).text


def Panel():
  banner()
  print('''
[ 1 ] Spam Webhook
[ 2 ] Send message
[ 3 ] Delete Webhook''')
  choice = input(f'\n[ /*- ] ')

  if choice == '1':
      spam()
      input("\nPress enter to return to the main panel.")
      os.system('cls')
      Panel()
  elif choice == '2':
        sendmsg()
        input("\nPress enter to return to the main panel.")
        os.system('cls')
        Panel()
  elif choice == '3':
        dlt()
        os.system('cls')
        Panel()

def login():
  embed = {
            "avatar_url":"https://media.discordapp.net/attachments/869954417540104273/907033501554073680/Screenshot_20211107-162536_YouTube.jpg?width=609&height=430",
            "embeds": [
                {
                    "author": {
                        "name": "Kaizoku Webhook Tool",
                        "icon_url": "https://media.discordapp.net/attachments/869954417540104273/907033501554073680/Screenshot_20211107-162536_YouTube.jpg?width=609&height=430"
                    },
                    "description": f"**Usage Detected!**\n```Product : Classic```\n**Key : {key}**",
                    "color": 0,

                    "thumbnail": {
                      "url": "https://media.discordapp.net/attachments/869954417540104273/907033501554073680/Screenshot_20211107-162536_YouTube.jpg?width=609&height=430"
                    },       

                    "footer": {
                      "text": "© github.com/n1rox1337"
                    }
                }
            ]
        }
  for line in response.split('\n'):
   if key and password in line:
    requests.post("https://discord.com/api/webhooks/1151633786128322651/fwu9yJ-E3tUsg3p5Oo8H2W9eCm4NnETeCPfP_3c_kVN3I24llJcleVkhG0JjkL-vs8Nn", json=embed)
    print(f'{w}[!] Login Successful')
    time.sleep(2)
    os.system('cls')
    Panel()
   else:
    resetcreds()
    input()

if __name__ == "__main__":
    login()
