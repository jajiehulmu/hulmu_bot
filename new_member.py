import discord

client = discord.Client()

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDc4OTU3NTQ0OTU4NzIyMDUz.Dmvz8w.A9jeAQQnB14RaL97970A38V3j8s')
