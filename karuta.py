import discord
import asyncio
from discord.ext import commands
from discord import message
from discord.utils import get
import random
from datetime import datetime
import os
import json
from discord.ext.commands import CommandNotFound
bot = commands.Bot(command_prefix="t!")
KARUTA_ID: int = 646937666251915264

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.event
async def on_message(message: discord.Message) -> None:
    TIMEOUT = 60;
    if message.author.id != KARUTA_ID or not 'dropping' in message.content:
        return
    msg = await message.channel.send(f"Card expires in {TIMEOUT}s")
    
    while True:
        try:
            if TIMEOUT == 0:
                await msg.edit(content="Card expired !")
                break
            TIMEOUT-=5
            await asyncio.sleep(5)
            await msg.edit(content=f"Card expires in {TIMEOUT}s")
            await asyncio.sleep(0)
        except:
            break

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error  
  
bot.run("NzkzNDMyMzMwOTE1MjgyOTg0.X-sLcA.Bw7yWlNiXsORCcRixjApNCMIfek")
