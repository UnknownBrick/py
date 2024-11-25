import discord
import random

intents = discord.Intents.default() 
intents.message_content = True
client = discord.Client(intents=intents)

def headsortails():
    return random.randint(1,2)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')
@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith('ping'):
        await msg.channel.send("pong")
    elif msg.content.startswith("headsortails"):
        await msg.channel.send(headsortails)
    else: 
        await msg.channel.send(msg.content)
client.run("MTMwNTU5MTk3MjQ5NjUzOTY4OQ.Ga3IiS.1kKXLBOpNRF19elZCKF7yIAZNjnTFiuCeDFc0A")
