import discord
import chat_exporter
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

############################discord commands###################################

client = commands.Bot(command_prefix="r ") #set a trigger for the bot to listen to, here it is "r "

@client.event
async def on_ready(): #on starting bot, sets ACTIVITY to "playing with my life"
    print("ready")
    chat_exporter.init_exporter(client)
    await client.change_presence(activity=discord.Game(name="with my life"))

@client.command()
async def hello(ctx): #when someone says "r hello", MENTIONS them and sends a gif
    await ctx.send(ctx.author.mention+" hey there partner")
    await ctx.send("https://tenor.com/bnOPP.gif")
    
@client.command()
async def word(ctx): #when someone says "r word", REPLIES to the message with a gif
    await ctx.reply("https://tenor.com/view/rdr2-rdr-red-dead-redemption-red-dead-redemption2-this-is-a-certified-gif-19692248")

def search(query):
    with YoutubeDL({"format": "bestaudio", "noplaylist": "True"}) as ydl:
        try:
            requests.get(query)
        except:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"][0]
        else:
            info = ydl.extract_info(query, download=False)
    return (info, info["formats"][0]["url"])

@client.command()
async def yt(ctx, *, query=None): # type "r yt *song name*" to search youtube and play best match in voice chat
    if query:
        FFMPEG_OPTS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }
        video, source = search(query)
        voice = get(client.voice_clients, guild=ctx.guild)

        channel = ctx.author.voice.channel #find voice channel of song requestor

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        if not voice.is_playing():
            voice.play(
                discord.FFmpegPCMAudio(source, **FFMPEG_OPTS, executable="__"), #insert path for ffmpeg application (inside bin of folder included in repository)
                after=lambda e: print("done", e),
            )
            voice.is_playing()
            text = 'Now playing: ' + query
            await ctx.send(text)
        else:
            await ctx.send(f"song playing already")
    else:
        await ctx.send("no song included")


client.run("__") #insert discord bot token

