import asyncio
import logging
import time
from contextlib import suppress
from typing import Union
import discord
LOGGING_FORMAT: str = '[%(asctime)-15s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s'
SHOOB_ID: int = 673362753489993749
TIMEOUT: int = 15
WAIT_DIFF: int = 1
BOT_TOKEN: str = "NzkzNDMyMzMwOTE1MjgyOTg0.X-sLcA.Bw7yWlNiXsORCcRixjApNCMIfek"
log: logging.Logger = logging.getLogger('discord')
logging.basicConfig(level=20, format=LOGGING_FORMAT, datefmt='%m/%d | %I:%M:%S')
intents: discord.Intents = discord.Intents().none()
intents.messages: bool = True
intents.guilds: bool = True
bot: discord.Client = discord.Client(intents=intents)
def is_spawn(message: discord.Message) -> Union[bool, None]:
    if message.embeds:
        embed: discord.Embed = message.embeds[0]
        return (embed.title
                and 'Tier' in embed.title
                and embed.image)
def is_claim(message: discord.Message) -> Union[bool, None]:
    if message.embeds:
        embed: discord.Embed = message.embeds[0]
        return embed.description and 'Issue #:' in embed.description
async def counter(embed: discord.Embed, out: discord.Message, timestamp: float) -> None:
    while timestamp - time.time() > 1:
        diff: float = timestamp - time.time()
        embed.description: str = "** <:timer:793427999608274944> | Card Despawns in %ds **" % diff
        try:
            await out.edit(embed=embed)
            await asyncio.sleep(WAIT_DIFF)
        except discord.NotFound:
            break
@bot.event
async def on_ready() -> None:
    log.info("Bot is Online !")
@bot.event
async def on_message(message: discord.Message) -> None:
    if message.author.id != SHOOB_ID or not is_spawn(message):
        return
    timestamp: float = time.time() + TIMEOUT
    diff: float = timestamp - time.time()
    embed: discord.Embed = discord.Embed(color=0x0037c3)
    embed.description: str = "** <:timer:793427999608274944> | Card Despawns in %ds **" % diff
    out: discord.Message = await message.channel.send(embed=embed)
    wait_task: asyncio.Task = bot.loop.create_task(bot.wait_for('message', timeout=30, check=is_claim))
    count_task: asyncio.Task = bot.loop.create_task(counter(embed, out, timestamp))
    done, pending = await asyncio.wait(
            {wait_task, count_task},
            return_when=asyncio.FIRST_COMPLETED
        )
    await out.delete()
    for task in pending:
        task.cancel()
        with suppress(asyncio.CancelledError):
            await task
bot.run(BOT_TOKEN)
