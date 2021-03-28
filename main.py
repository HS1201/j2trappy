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


@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("Joining!")
    else:
        await ctx.send("Oi! You're not in a voice channel! You must be in a voice channel to run this command.")


@client.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel :(")
    else:
        await ctx.send("I'm not in a voice channel!")

client.run(UltronToken)
