#imports required dependicies for discord
import discord
from discord.ext import commands

#import the bottoken
from apikeys import *

#importing dependices of playing yt songs
import yt_dlp

#these options configure ffmpeg to process audio and youtube-dl to download the best audio format froma single video
FFMEG_OPTIONS = {'options':'-vn'}
YDL_OPTIONS = {'format' : 'bestaudio' , 'noplaylist' : True}

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.voice_states = True

#call the bot when ! is used
client = commands.Bot(command_prefix ='!', intents=intents) 

#bot is ready to receive commands
@client.event
async def on_ready(): 
    print("Fanum tax the ohio rizzler")
    print("---------------------------")

#ctx takes the input from the user
@client.command()
async def hello(ctx):
    await ctx.send("Wop wop wop wop wop ima do my stuff")

@client.command()
async def goodbye(ctx):
    await ctx.send("they not like us they not like us")

@client.command()
async def rick(ctx):
    await ctx.send("fuck you")

#when an event function detects something it would something else
@client.event
async def on_member_join(member):
    channel = client.get_channel(1268621896358957180)
    await channel.send("hello")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1268621896358957180)
    await channel.send("seeeeyuhhhh")

#if user in a voice chat and uses this command the bot will join
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("get in a voice channel jittleyang")

#makes the bot leave voice chat if it is in one
@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("i need to futtulatugan else where fonem")
    else:
        await ctx.send("i aint even in a voice chat dumbass")

@client.command()
async def __init__(self, client):
        self.client = client
        self.queue = []

@client.command()
async def play(self, ctx, * , search):
    voice_channel = ctx.author.voice.channel if ctx.author.voice else None
    if not voice_channel:
        return await ctx.send("get in the call dumbass")
    if not ctx.voice_client:
        await voice_channel.connect()
    
    async with ctx.typing():
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info (f"ytsearch:{search}", download = False)
            if 'entries' in info:
                info = info['entries'][0]
            url = info['url']
            title = info['title']
            self.queue.append((url,title))
            await ctx.send(f'Added to queue: **{title}**')
    if not ctx.voice_client.is_playing():
        await self.play_next(ctx)

#this plays the next song that is queued
    @client.commands
    async def play_next(self, ctx):
        if self.queue:
            url,title - self.queue.pop(0)
            source = await discord.FFmpegAudio.from_probe(url, **FFMEG_OPTIONS)
            ctx.voice_client.play(source, after=lambda _:self.client.loop.create_task(self.play_next(ctx)))
            await ctx.send(f'Now playing **{title}**')
        elif not ctx.voice_client.is_playing():
            await ctx.send("play some space panda will ya")

#this th the skip command
    @client.commands()
    async def skip(ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("This song is some ass play the next one")

client.run(bottoken)


