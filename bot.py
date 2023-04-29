import discord
from discord.ext import commands
import os
import json

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix = "!", intents=intents, case_insensitive=True)

TOKEN_filepath = "private/token.txt"
TOKEN = open(TOKEN_filepath, "r").readlines()[0]

mainChannel_filepath = "private/mainChannel.txt"
mainChannel = open(mainChannel_filepath, "r").readlines()[0]

@bot.event
async def on_ready():
    print(f"{bot.user} is now running!")
    channel = bot.get_channel(mainChannel)
    await channel.send("`Bot is up and running.`")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    ctx = await bot.get_context(message)

def runBot():
    bot.run(TOKEN)


