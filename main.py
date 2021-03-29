import discord
from discord.ext import commands
from apikeys import *

intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix='>', intents=intents)


@client.event
async def on_connect():
    print('Connecting to servers...')
    print('Connecting to servers...')
    print('Connecting to servers...')


@client.event
async def on_ready():
    print('--------------------')
    print('  Ultron activated')
    print('--------------------')
    await client.change_presence(activity=discord.Game(name="> = prefix"))


@client.command()
async def test(ctx):
    await ctx.send('Bot rewrite in progress...')


@client.event
async def on_member_join(member):
    channel = client.get_channel(823234745408290888)
    await channel.send('Hello!')


@client.event
async def on_message(message):
    testMessage1 = message.content
    f = open("chatlog.txt", "a")
    f.write(testMessage1 + "\n")
    f.close()


client.run(UltronToken)
