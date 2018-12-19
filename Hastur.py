# Hastur's Soul
import discord
import PuzzleBox
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
@bot.command()
async def hello(ctx):
    await ctx.send("I didn't really want to talk to you anyways")
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(PuzzleBox.HasturToken)
