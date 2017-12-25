import discord
import asyncio
from discord.ext import commands
from bot_music import Music
from bot_mp3 import Youtube2Mp3
from bot_lyrics import Lyrics

cosmic = commands.Bot(command_prefix='$')

@cosmic.event
async def on_ready():
    print('Logged in as')
    
@cosmic.command()
async def hello(message:str):
    await cosmic.say("Hello hehe "+message)

cosmic.add_cog(Music(cosmic))
cosmic.add_cog(Youtube2Mp3(cosmic))
cosmic.add_cog(Lyrics(cosmic))

f = open('token.txt','r')
token=f.read().strip()
f.close()

try:
    cosmic.run(token)
except:
    print("make sure you provided valid token")
    exit()
    