import discord
import colorama
import os
import requests
import json

from colorama import Fore

client = discord.Client()

def Clear():
    os.system('')
Clear()

with open('config.json') as f:
    config = json.load(f)

message = config['message']

print(f"""{Fore.RED}

▒█▀▄▀█ ▒█▀▀█ ▒█▀▄▀█ 　 ▒█▀▄▀█ ░█▀▀█ ▒█▀▀▀█ ▒█▀▀▀█ 　 ▒█▀▀▄ ▒█▀▄▀█ 
▒█▒█▒█ ▒█▀▀▄ ▒█▒█▒█ 　 ▒█▒█▒█ ▒█▄▄█ ░▀▀▀▄▄ ░▀▀▀▄▄ 　 ▒█░▒█ ▒█▒█▒█ 
▒█░░▒█ ▒█▄▄█ ▒█░░▒█ 　 ▒█░░▒█ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄▄█ 　 ▒█▄▄▀ ▒█░░▒█
{Fore.WHITE} made by Shiloh               
""") 

token = input('token:')
print('{0}'.format(client.user))

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
  print(f'{Fore.GREEN}Valid')
  input(f'{Fore.WHITE}press enter')

else:
  print(f'{Fore.RED}invalid')
  input(f'{Fore.WHITE}press enter')
  exit(0)
  Clear()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(f'''{message}''')
      print(f"{Fore.GREEN}sent")
    except:
       print(f"{Fore.RED}cant send")

client.run(token, bot=False) 
