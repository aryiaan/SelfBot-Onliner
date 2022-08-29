import discord
from discord import Client, Status
status = "online, dnd, idle, invisible"
name = "the name of your status"
emoji = "the emoji of your status"
token = "your token"
client = Client(self_bot=True)
@client.event
async def on_ready():
    print("Logged in as ", client.user)
    if status == "online":
        await client.change_presence(status=Status.online,activity=discord.CustomActivity(name=name, emoji=emoji))
    elif status == "dnd": 
        await client.change_presence(status=Status.dnd,activity=discord.CustomActivity(name=name, emoji=emoji))
    elif status == "idle":
        await client.change_presence(status=Status.idle,activity=discord.CustomActivity(name=name, emoji=emoji))
    elif status == "invisible" : 
        await client.change_presence(status=Status.invisible,activity=discord.CustomActivity(name=name, emoji=emoji))
    print(f"Your Status Changed To {name} {emoji}")
client.run(token)