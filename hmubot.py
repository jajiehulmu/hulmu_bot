# hulmu bot By Erithreaj

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    
    print ("Ready when you are Jajie")
    print ("I am running on" + bot.user.name)
    print ("with the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! x555")

@bot.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
    
bot.run("NDc4OTU3NTQ0OTU4NzIyMDUz.Dmvz8w.A9jeAQQnB14RaL97970A38V3j8s")
