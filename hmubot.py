# hulmu bot By Erithreaj

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')
client = discord.Client()

@bot.event
async def on_ready():
    
    print ("logged in as")
    print (bot.user.name)
    print (bot.user.id)
    print ('-----')
    
@client.event
async def on_member_join(member):
    print("Recognized that a member called " + member.name + " joined")
    await client.send_message(member, "Welcome to the server!")
    print("Sent message to " + member.name)
          
bot.run("NDc4OTU3NTQ0OTU4NzIyMDUz.Dmvz8w.A9jeAQQnB14RaL97970A38V3j8s")
