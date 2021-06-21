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

TOKEN = "NzkzNDMyMzMwOTE1MjgyOTg0.X-sLcA.Bw7yWlNiXsORCcRixjApNCMIfek"
BOT_PREFIX = "t!", "T!", ","

bot = commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')

@bot.event
async def on_ready():
    activity = discord.Game(name="t!help", type=3)
    print("Bot is ready!")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command(aliases= ["INVITE"])
async def invite(ctx):

    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        title="**Invite Link**",
        description="[Click here](https://discord.com/oauth2/authorize?client_id=793432330915282984&permissions=519232&scope=bot) to add me in your server.\n\n[Join](https://discord.gg/3x8zmuB68X) our support server to get updated and support."
    )

    embed.set_footer(text="Timer Support")

    await ctx.send(embed=embed, delete_after=10)

@bot.command(aliases= ["HELP"])
async def help(ctx):

    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        title="**Help**",
        description="`t!invite` - Add me to your server.\n`t!ping` - To show the Bot's latency.\n`t!help-cd` - To see reminder commands of cards cooldown.\n`t!help-role` - To see ping role set commands of Shoob, Karuta and Gachapon.\n`t!shoob` - To see Shoob Bot commands.\n`t!karuta` - To see Karuta Bot commands.\n`t!av` - To see Avatar.\n`t!math` - Calculator.\n`t!timer` - To set countdown.\n`t!reminder` - To set reminder.\n`t!weather` - To see weather details.\n`t!reverse` - To reverse a sentence.\n`t!snipe` - To see the previous deleted massege.\n`t!fillers` - Displays the fillers episodes of the anime which you specify ( taken from https://animefillerlist.com/shows/ ).")
    embed.set_footer(text="Timer Support")

    await ctx.send(embed=embed)

@bot.command(aliases= ["help-cd"])
async def helpcd(ctx):

    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        title="**Cooldown Commands**",
        description="`t!cd` - To set T1 cooldown reminder.\n`t!cd2` - To set T2 cooldown reminder.\n`t!cd3` - To set T3 cooldown reminder.\n`t!cd4` - To set T4 cooldown reminder.\n`t!cd5` - To set T5 cooldown reminder.\n`t!cd6` - To set T6 cooldown reminder.\n`t!cdbump` - To set 1hr reminder of Bump.\n`t!cdvote` - To set 12hrs reminder of Vote.\n`t!cd-kdrop` - This command reminds you after 30 minutes for your karuta drop\n`t!cd-gdrop` - This command reminds you after 20 minutes for your gacha drop.\n`t!cd-claim` - This command reminds you after 10 minutes for your karuta / gacha card claim.")
    embed.set_footer(text="Timer Support")

    await ctx.send(embed=embed) 

@bot.command(aliases=["help-role"])
async def helproles(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        title="**Set Ping Roles Commands**",
        description="`t!role shoob` - This command will show you how to set the ping roles for Shoob\n`t!role karuta` - This command will show you how to set the ping role for Karuta.\n`t!role gacha` - This command will show you how to set the ping roles for Gacha.\n`t!ping-roles-shoob` - This command shows what ping role has been setup for which tier in Shoob.\n`t!ping-roles-karuta` - This command shows what ping role has been setup for Karuta.\n`t!ping-roles-gacha` - This command shows what ping role has been setup for Gacha.\n`t!role off` - This command will show you how to off the ping roles.")
    embed.set_footer(text="Timer Support")

    await ctx.send(embed=embed)

@bot.command(aliases=["SHOOB", "Shoob"])
async def shoob(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"`t!shoob-guide` - Displays the Shoob Guide(officially owned by Shoob Owners and Management)\n`t!gift <user>` - To gift cards to someone.\n`t!trade <user>` - To send trades to someone.\n`t!profile` - To see your anime soul profile.\n`t!bump` - Link to directly bump on Animesoul site.\n`t!vote shoob` - Vote shoob.\n`t!fuse` - Link to fuse your cards.\n`t!market` - Go directly to the market.\n`t!mg` - Go to minigames.\n`t!auction` - Go to auction site.\n`t!server` - Check out your server directly by going through this link.\n`t!noti` - To see AS Notifications.\n`t!achivement` - check your achivements on as site.\n`t!msg` - Check out dms on animesoul site.\n`t!premium <user>` - Gift the user anime soul premium.\n`t!db` - directly go to AS dashboard.\n`t!assupport` - go to the link of  animeosoul  support.\n`t!inv` - check your inventory.\n`t!bank` - directly go to bank."
    )
    embed.set_footer(text="Timer Support")

    await ctx.send(embed=embed)

@bot.command(aliases=["KARUTA", "Karuta"])
async def karuta(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"`t!karuta-guide` - Displays the Guide Of Karuta(officially owned by Craig and Karuta Management)\n`t!upgrade` - Know the effort of the card after it will be upgraded.\n`t!vote karuta` - Vote Karuta.\n`t!injured` - Know the effort of your card when it will be healed from its injury.\n`t!dye` - Know the Math behind how Dyes and Frames amplify the effort of your cards."
    )
    embed.set_footer(text="Timer Support")

    await ctx.send(embed=embed)

@bot.command(aliases= ["PING"])
async def ping(ctx):
    if round(bot.latency * 1000) <= 50:
        embed=discord.Embed(description=f"**Ping : `{round(bot.latency *1000)} ms`**", color=0x44ff44)
    elif round(bot.latency * 1000) <= 100:
        embed=discord.Embed(description=f"**Ping : `{round(bot.latency *1000)} ms`**", color=0xffd000)
    elif round(bot.latency * 1000) <= 200:
        embed=discord.Embed(description=f"**Ping : `{round(bot.latency *1000)} ms`**", color=0xff6600)
    else:
        embed=discord.Embed(description=f"**Ping : `{round(bot.latency *1000)} ms`**", color=0x990000)
    await ctx.send(embed=embed, delete_after=10)

@bot.command(aliases=["cd-t1","cdt1", "cooldown", "cd1", "CD", "CDT1", "COOLDOWN", "CD1", "Cd", "cD"])
async def cd(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you when your `T1 Cooldown` will over."
    )
    await ctx.send(embed=embed)
    seconds=110
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, your `T1 Cooldown` has over.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["cd-t2","cdt2", "cooldownt2", "CD2", "CDT2", "COOLDOWN2"])
async def cd2(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you when your `T2 Cooldown` will over."
    )
    await ctx.send(embed=embed)
    seconds=590
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, your `T2 Cooldown` has over.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["cd-t3","cdt3", "cooldownt3", "CD3", "CDT3", "COOLDOWN3"])
async def cd3(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you when your `T3 Cooldown` will over."
    )
    await ctx.send(embed=embed)
    seconds=1790
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, your `T3 Cooldown` has over.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["cd-t4","cdt4", "cooldownt4", "CD4", "CDT4", "COOLDOWN4"])
async def cd4(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you when your `T4 Cooldown` will over."
    )
    await ctx.send(embed=embed)
    seconds=7190
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, your `T4 Cooldown` has over.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["cd-t5","cdt5", "cooldownt5", "CD5", "CDT5", "COOLDOWN5"])
async def cd5(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you when your `T5 Cooldown` will over."
    )
    await ctx.send(embed=embed)
    seconds=21590
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, your `T5 Cooldown` has over.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["cd-t6","cdt6", "cooldownt6", "CD6", "CDT6", "COOLDOWN6"])
async def cd6(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you when your `T6 Cooldown` will over."
    )
    await ctx.send(embed=embed)
    seconds=86390
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, your `T6 Cooldown` has over.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["cd-gdrop"])
async def cdgdrop(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you after 20 mins."
    )
    await ctx.send(embed=embed)
    seconds=1200
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, you can now use `gg` commands.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["cd-kdrop"])
async def cdkdrop(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you after 30 mins."
    )
    await ctx.send(embed=embed)
    seconds=1800
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, you can now use `kd` commands.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["cd-claim"])
async def cdclaim(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you after 10 mins."
    )
    await ctx.send(embed=embed)
    seconds=600
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, you now can claim cards.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["br", "brem", "rb", "rembump", "cdb", "cdbump"])
async def bumprem(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you after 1 hour."
    )
    await ctx.send(embed=embed)
    seconds=3600
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, you can `Bump` now.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["vr", "vrem", "rv", "remvote", "cdv", "cdvote"])
async def voterem(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        description=f"Alright {ctx.author.mention}, I will remind you after 12 hours."
    )
    await ctx.send(embed=embed)
    seconds=43200
    await asyncio.sleep(seconds)
    await ctx.send(f"Hi {ctx.author.mention}, you can `Vote` now.")
    return
    await ctx.send(embed=embed)

@bot.command(aliases=["gift", "GIFT"])
async def gift_cmd(ctx, member : discord.Member):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/gift/{member.id}) to gift cards to <@{member.id}>."
    )
    await ctx.send(embed=embed)

@gift_cmd.error
async def gift_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color = random.randint(0, 0xFFFFFF),
            description=f"[Click Here](https://animesoul.com/gift/{ctx.author.id}) to gift cards to <@{ctx.author.id}>."
        )
    await ctx.send(embed=embed)

@bot.command(aliases=["TRADE"])
async def trade(ctx, member : discord.Member):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        title="**Trade**",
        description=f"[Click Here](https://animesoul.com/trade/{member.id}) to send trades to <@{member.id}>."
    )
    embed.set_footer(text="Timer Support")
    await ctx.send(embed=embed)

@trade.error
async def trade_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed= discord.Embed(
            colour=discord.Colour.red(),
            description=("Please mention an user.")
        )
        await ctx.send(embed=embed)

@bot.command(name='avatar',aliases=["av", "AV", "AVATAR"])
async def av_cmd(ctx, member: discord.Member):
    embed = discord.Embed(
        color = random.randint(0, 0xFFFFFF),
        title=f"{member}",
        description=f"[Download]({member.avatar_url})"
    )
    embed.set_image(url=f"{member.avatar_url}")
    await ctx.send(embed=embed)

@av_cmd.error
async def av_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color = random.randint(0, 0xFFFFFF),
            title=f"{ctx.author}",
            description=f"[Download]({ctx.author.avatar_url})"
        )
    embed.set_image(url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)

@bot.command(name='serverinfo', aliases=['ServerInfo', 'sinfo', 'si', 'SI'])
async def si_cmd(ctx):
    embed = discord.Embed(
        color = random.randint(0, 0xFFFFFF),
        title=f"{ctx.guild.name}"
    )
    embed.set_image(url=f"{ctx.guild.icon_url}")
    embed.add_field(name="Region", value=f"`{ctx.guild.region}`")
    embed.add_field(name="Member Count", value=f"`{ctx.guild.member_count}`")
    embed.set_footer(icon_url=f"{ctx.guild.icon_url}", text=f"Guild ID: {ctx.guild.id}")
    await ctx.send(embed=embed)

@bot.command(name='profile', aliases=['p', 'P', 'PROFILE'])
async def profile_cmd(ctx, member : discord.Member):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        title=f"Profile of {member}",
        description=f"[Click Here](https://animesoul.com/user/{member.id}) to open <@{member.id}>'s AnimeSoul Profile."
    )
    embed.set_footer(text="Timer Support")
    await ctx.send(embed=embed)

@profile_cmd.error
async def profile_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color = random.randint(0, 0xFFFFFF),
            title="Your Profile",
            description=f"[Click Here](https://animesoul.com/user/{ctx.author.id}) to open <@{ctx.author.id}>'s AnimeSoul Profile."
        )
    embed.set_footer(text="Timer Support")
    await ctx.send(embed=embed)

@bot.command(aliases=["BUMP"])
async def bump(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/bump) to Bump."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["fuse", "FUSE", "FUSION"])
async def fusion(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/fusion) to open Fusion HQ."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["mr", "MR", "MARKET"])
async def market(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/market) to open Market."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["minigame", "MG"])
async def mg(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/mini-game) to open Mini-Game."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["auc", "AUC"])
async def auction(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/auction) to open Auction."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["sl","sli","server", "SL", "SLI"])
async def server_list(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/servers) to open Server List."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["achiev","achv", "ACHV", "ACHIEVEMENTS"])
async def achievements(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/achievements) to open Your Achievements."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["msg", "MSG"])
async def messages(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/messages) to open Your Website Messages."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["PREMIUM"])
async def premium(ctx, member : discord.Member):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        title="**Premium**",
        description=f"[Click Here](https://animesoul.com/premium/gift/{member.id}) to gift AS Premium to <@{member.id}>."
    )
    embed.set_footer(text="Timer Support")
    await ctx.send(embed=embed)

@premium.error
async def premium_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed= discord.Embed(
            colour=discord.Colour.red(),
            description=("Please mention an user.")
        )
        await ctx.send(embed=embed)


@bot.command(aliases=["dash", "db", "DB", "DASH"])
async def dashboard(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/dashboard) to open Your Website Dashboard."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["sup","assupport", "SUP", "SUPPORT"])
async def support(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/support) to open Website Support Section."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["inv", "INV", "INVENTORY"])
async def inventory(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/inventory) to open your Inventory."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["BANK"])
async def bank(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/bank) to open your bank."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["noti", "NOTI"])
async def notification(ctx):
    embed = discord.Embed(
        colour=random.randint(0, 0xFFFFFF),
        description=f"[Click Here](https://animesoul.com/notifications) to open your AS Notifications."
    )
    await ctx.send(embed=embed)

@bot.event
async def on_message(ctx):
    
    if ctx.content.startswith(f"<@!{bot.user.id}>") and len(ctx.content) == len(
        f"<@!{bot.user.id}>"
    ):
        
        await ctx.channel.send(f"Hi <@{ctx.author.id}>, My prefix is `t!`")

    await bot.process_commands(ctx)
   
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@bot.command()
async def weather(ctx, message):
	embed = discord.Embed(colour = random.randint(0, 0xFFFFFF),
	                      timestamp=ctx.message.created_at,
	                      title=f"Weather in {message}")
	embed.set_image(
	    url=
	    f"https://api.cool-img-api.ml/weather-card?location={message}&background=https://cdn.discordapp.com/attachments/819395525820416000/847131557440782417/black-blur.png"
	)
	await ctx.send(embed=embed)

@weather.error
async def weather_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed= discord.Embed(
        colour=discord.Colour.red(),
        description=(f"```weather <location name>```\nInvalid arguments provided: Not enough arguments passed.")
        )
        await ctx.send(embed=embed)

@bot.command(aliases=["rm", "remindme", "remind"])
async def reminder(ctx,seconds, * ,messages):
    try:
        try:
            time = int(seconds)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
            time = int(seconds[:-1]) * convertTimeList[seconds[-1]]
        if time > 21600:
            embed= discord.Embed(
            colour=discord.Colour.red(),
            description=("I can\'t set reminders over 6 hrs long.")
            )
            await ctx.send(embed=embed)
            return
        if time <= 0:
            embed= discord.Embed(
            colour=discord.Colour.red(),
            description=("Reminders don\'t go into negatives.")
            )
            await ctx.send(embed=embed)
            return
        if time >= 3600:
            embed= discord.Embed(
            colour=discord.Colour.red(),
            description=(f"Set a reminder in {time//3600} hours {time%3600//60} minutes {time%60} seconds from now.")
            )
            await ctx.send(embed=embed)
        elif time >= 60:
            embed= discord.Embed(
            colour=discord.Colour.red(),
            description=(f"Set a reminder in {time//60} minutes {time%60} seconds from now.")
            )
            await ctx.send(embed=embed)
        elif time < 60:
            embed= discord.Embed(
            colour=discord.Colour.red(),
            description=(f"Set a reminder in {time} seconds from now.")
            )
            await ctx.send(embed=embed)
        while True:
            time -= 1
            if time == 0:
                break
            await asyncio.sleep(1)
        await ctx.send(f"**Reminder** {ctx.author.mention}: {messages}")
    except:
        embed= discord.Embed(
        colour=discord.Colour.red(),
        description=(f"```reminder <Time:Duration> <Message:Text>```\nInvalid arguments provided: Not enough arguments passed.")
        )
        await ctx.send(embed=embed)

@reminder.error
async def reminder_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed= discord.Embed(
        colour=discord.Colour.red(),
        description=(f"```reminder <Time:Duration> <Message:Text>```\nInvalid arguments provided: Not enough arguments passed.")
        )
        await ctx.send(embed=embed)

@bot.command()
async def timer(ctx, *, timeInput):
    try:
        try:
            time = int(timeInput)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
            time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
        if time > 21600:
            embed= discord.Embed(
            colour=discord.Colour.red(),
            description=(f"I can\'t do timers over 6 hrs long.")
            )
            await ctx.send(embed=embed)
            return
        if time <= 0:
            embed= discord.Embed(
            colour=discord.Colour.red(),
            description=(f"Timers don\'t go into negatives.")
            )
            await ctx.send(embed=embed)
            return
        if time >= 3600:
            embed= discord.Embed(
            colour=discord.Colour.red(),
            description=(f"Timer: {time//3600} hours {time%3600//60} minutes {time%60} seconds")
            )
            msg = await ctx.send(embed=embed)
        elif time >= 60:
            embed= discord.Embed(
            colour=discord.Colour.red(),
            description=(f"Timer: {time//60} minutes {time%60} seconds")
            )
            msg = await ctx.send(embed=embed)
        elif time < 60:
            embed= discord.Embed(
            colour=discord.Colour.red(),
            description=(f"Timer: {time} seconds")
            )
            msg = await ctx.send(embed=embed)
        while True:
            try:
                await asyncio.sleep(1)
                time -= 1
                if time >= 3600:
                    embed1= discord.Embed(
                    colour=discord.Colour.red(),
                    description=(f"Timer: {time//3600} hours {time %3600//60} minutes {time%60} seconds")
                    )
                    await msg.edit(embed=embed1)
                elif time >= 60:
                    embed1= discord.Embed(
                    colour=discord.Colour.red(),
                    description=(f"Timer: {time//60} minutes {time%60} seconds")
                    )
                    await msg.edit(embed=embed1)
                elif time < 60:
                    embed1= discord.Embed(
                    colour=discord.Colour.red(),
                    description=(f"Timer: {time} seconds")
                    )
                    await msg.edit(embed=embed1)
                if time <= 0:
                    embed1= discord.Embed(
                    colour=discord.Colour.red(),
                    description=(f"Ended!")
                    )
                    await msg.edit(embed=embed1)
                    break
            except:
                break
    except:
        embed= discord.Embed(
        colour=discord.Colour.red(),
        description=(f"Alright, first you gotta let me know how I\'m gonna time **{timeInput}**....")
        )
        await ctx.send(embed=embed)

@timer.error
async def timer_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed= discord.Embed(
        colour=discord.Colour.red(),
        description=(f"```timer <Time:Duration>```\nInvalid arguments provided: Not enough arguments passed.")
        )
        await ctx.send(embed=embed)

@bot.command(aliases=["reverse"])
async def rev(ctx, *, var):
	stuff = var[::-1]
	embed = discord.Embed(description = stuff, colour = random.randint(0, 0xFFFFFF))
	embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
	await ctx.message.delete()
	await ctx.send(embed = embed)

@rev.error
async def rev_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed= discord.Embed(
            colour=discord.Colour.red(),
            description=("Please type a sentence to reverse.")
        )
        await ctx.send(embed=embed)

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@bot.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

@bot.command()
async def snipe(message):
    if snipe_message_content==None:
        await message.channel.send("There is nothing to snipe.")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_author(name= f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        return

bot.run(TOKEN)
