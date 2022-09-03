import discord
from discord import Client, Status
status = "online, dnd, idle, invisible"
name = "the name of your status"
emoji = "the emoji of your status"
token = "your token"
from datetime import datetime
from colorama import Fore, Back, Style
client = Client(self_bot=True)
@client.event
async def on_ready():
    day = datetime.now() - client.user.created_at
    print(f"{Fore.GREEN}Logged in\nUser : {client.user}\nID : {client.user.id}\nCreation Date : {client.user.created_at} ({day.days})\nBadges : ")
    for badg in client.user.public_flags.all():
        print(badg)
    if status == "online":
        await client.change_presence(status=Status.online,activity=discord.CustomActivity(name=name, emoji=emoji))
    elif status == "dnd": 
        await client.change_presence(status=Status.dnd,activity=discord.CustomActivity(name=name, emoji=emoji))
    elif status == "idle":
        await client.change_presence(status=Status.idle,activity=discord.CustomActivity(name=name, emoji=emoji))
    elif status == "invisible" : 
        await client.change_presence(status=Status.invisible,activity=discord.CustomActivity(name=name, emoji=emoji))
    print(f"{Fore.GREEN}Your Status Changed To {name} {emoji}{Style.RESET_ALL}")
client.run(token)
