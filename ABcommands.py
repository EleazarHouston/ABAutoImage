from discord.ext import commands
import discord
import os
import json
import accessStableDiffusion

async def ping(ctx, userInput):
    response = ""
    userInput = userInput.replace("!", "")
    i = 0
    while i < len(userInput):
        if userInput[i:i+4] == "ping":
            response += "Pong"
            i += 4
        elif userInput[i:i+4] == "pong":
            response += "Ping"
            i += 4
        else:
            i += 1
    response += "!"
    response = response.strip()
    await ctx.send(response)

async def cmd_ping(ctx):
    await ctx.send("Pong!")

async def cmd_pong(ctx):
    await ctx.send("Ping!")


async def handle_command(ctx, bot):
    userInput = ctx.message.content.lower()
    print(f"{ctx.author}: {userInput}")
    if ("ping" in userInput or "pong" in userInput) and userInput[0] == "!":
        print("ping or pong found!")
        try:
            await ping(ctx, userInput)
        except Exception as e:
            error_message= f"An error occurred while processing your command: \"{str(e)}\""
            print(e)
    if userInput in commandDict:
        try:
            await commandDict[userInput](ctx, bot)
        except Exception as e:
            error_message= f"An error occurred while processing your command: \"{str(e)}\""
            await ctx.send(error_message)

async def cmd_generate(ctx, bot):
    member = ctx.author
    if any(role.name.lower() == "admin".lower() for role in member.roles):
        await ctx.send("Warning: This is still in alpha")
        accessStableDiffusion.getSDiffImage()
    else:
        await ctx.send("Error: You are not an admin.")

commandDict = {
    "!generate": cmd_generate
}