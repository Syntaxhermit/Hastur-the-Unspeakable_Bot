# Hastur's Soul
from discord.ext import commands
import discord, PuzzleBox

hastur = commands.Bot("$")


@hastur.command
async def hello(ctx):
    MA = ctx.author
    MC = ctx.channel
    print("{} said hello".format(MA))
    await MC.send("Hello, {}!".format(MA.name))

@hastur.event
async def on_ready():
    print("Hastur has Risen!")
    print("Logged in as: {}".format(hastur.user.name))

hastur.run(PuzzleBox.HasturToken)
