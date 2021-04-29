import discord
import asyncio
from discord.ext import commands
from discord import message
from discord.utils import get
#import timer

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
        colour=ctx.author.top_role.colour,
        title="**Invite Link**",
        description="[Click here](https://discord.com/oauth2/authorize?client_id=793432330915282984&permissions=379968&scope=bot) to add me in your server.\n\n[Join](https://discord.gg/3x8zmuB68X) our support server to get updated and support."
    )

    embed.set_footer(text="Timer Support")

    await ctx.send(embed=embed, delete_after=10)

@bot.command(aliases= ["HELP"])
async def help(ctx):

    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        title="**Help**",
        description="`t!invite` - Add me to your server.\n`t!about` - About me.\n`t!ping` - To show the Bot's latency.\n`t!helpcd` - To see reminder commands of cards cooldown.\n`t!gift <user>` - To gift cards to someone.\n`t!trade <user>` - To send trades to someone.\n`t!profile` - To see your anime soul profile.\n`t!bump` - Link to directly bump on Animesoul site.\n`t!vote` - Vote shoob.\n`t!fuse` - Link to fuse your cards.\n`t!market` - Go directly to the market.\n`t!mg` - Go to minigames.\n`t!auction` - Go to auction site.\n`t!server` - Check out your server directly by going through this link.\n`t!noti` - To see AS Notifications.\n`t!achivement` - check your achivements on as site.\n`t!cal` - Calculator.\n`t!msg` - Check out dms on animesoul site.\n`t!premium <user>` - Gift the user anime soul premium.\n`t!db` - directly go to AS dashboard.\n`t!assupport` - go to the link of  animeosoul  support.\n`t!inv` - check your inventory.\n`t!bank` - directly go to bank.\n`t!av` - To see Avatar."
    )
    embed.set_footer(text="Timer Support")

    await ctx.send(embed=embed)

@bot.command(aliases= ["hcd", "HELPCD"])
async def helpcd(ctx):

    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        title="**Cooldown Commands**",
        description="`t!cd` - To set T1 cooldown reminder.\n`t!cd2` - To set T2 cooldown reminder.\n`t!cd3` - To set T3 cooldown reminder.\n`t!cd4` - To set T4 cooldown reminder.\n`t!cd5` - To set T5 cooldown reminder.\n`t!cd6` - To set T6 cooldown reminder."
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
@bot.command(aliases= ["ABOUT"])
async def about(ctx):

    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        title="**About**",
        description="This is a Timer Bot. That helps you to claim Shoob cards up to time. So, don't miss any card and enjoy claiming."
    )
    embed.set_footer(text="Timer Support")

    await ctx.send(embed=embed, delete_after=10)

@bot.command(aliases=["cdt1", "cooldown", "cd1", "CD", "CDT1", "COOLDOWN", "CD1", "Cd", "cD"])
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

@bot.command(aliases=["cdt2", "cooldownt2", "CD2", "CDT2", "COOLDOWN2"])
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

@bot.command(aliases=["cdt3", "cooldownt3", "CD3", "CDT3", "COOLDOWN3"])
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

@bot.command(aliases=["cdt4", "cooldownt4", "CD4", "CDT4", "COOLDOWN4"])
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

@bot.command(aliases=["cdt5", "cooldownt5", "CD5", "CDT5", "COOLDOWN5"])
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

@bot.command(aliases=["cdt6", "cooldownt6", "CD6", "CDT6", "COOLDOWN6"])
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

@bot.command(aliases=["gift", "GIFT"])
async def gift_cmd(ctx, member : discord.Member):
    embed = discord.Embed(
        colour=member.top_role.colour,
        description=f"[Click Here](https://animesoul.com/gift/{member.id}) to gift cards to <@{member.id}>."
    )
    await ctx.send(embed=embed)

@gift_cmd.error
async def gift_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color = ctx.author.top_role.colour,
            description=f"[Click Here](https://animesoul.com/gift/{ctx.author.id}) to gift cards to <@{ctx.author.id}>."
        )
    await ctx.send(embed=embed)

@bot.command(aliases=["TRADE"])
async def trade(ctx, member : discord.Member):
    embed = discord.Embed(
        colour=member.top_role.colour,
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
        color = member.top_role.colour,
        title=f"{member}",
        description=f"[Download]({member.avatar_url})"
    )
    embed.set_image(url=f"{member.avatar_url}")
    await ctx.send(embed=embed)

@av_cmd.error
async def av_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color = ctx.author.top_role.colour,
            title=f"{ctx.author}",
            description=f"[Download]({ctx.author.avatar_url})"
        )
    embed.set_image(url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)

@bot.command(name='serverinfo', aliases=['ServerInfo', 'sinfo', 'si', 'SI'])
async def si_cmd(ctx):
    embed = discord.Embed(
        color = ctx.author.top_role.colour,
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
        colour=member.top_role.colour,
        title=f"Profile of {member}",
        description=f"[Click Here](https://animesoul.com/user/{member.id}) to open <@{member.id}>'s AnimeSoul Profile."
    )
    embed.set_footer(text="Timer Support")
    await ctx.send(embed=embed)

@profile_cmd.error
async def profile_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color = ctx.author.top_role.colour,
            title="Your Profile",
            description=f"[Click Here](https://animesoul.com/user/{ctx.author.id}) to open <@{ctx.author.id}>'s AnimeSoul Profile."
        )
    embed.set_footer(text="Timer Support")
    await ctx.send(embed=embed)

@bot.command(aliases=["BUMP"])
async def bump(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/bump) to Bump."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["VOTE"])
async def vote(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://top.gg/bot/673362753489993749/vote) to Vote."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["fuse", "FUSE", "FUSION"])
async def fusion(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/fusion) to open Fusion HQ."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["mr", "MR", "MARKET"])
async def market(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/market) to open Market."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["minigame", "MG"])
async def mg(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/mini-game) to open Mini-Game."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["auc", "AUC"])
async def auction(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/auction) to open Auction."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["sl","sli","server", "SL", "SLI"])
async def server_list(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/servers) to open Server List."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["achiev","achv", "ACHV", "ACHIEVEMENTS"])
async def achievements(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/achievements) to open Your Achievements."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["msg", "MSG"])
async def messages(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/messages) to open Your Website Messages."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["PREMIUM"])
async def premium(ctx, member : discord.Member):
    embed = discord.Embed(
        colour=member.top_role.colour,
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
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/dashboard) to open Your Website Dashboard."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["sup","assupport", "SUP", "SUPPORT"])
async def support(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/support) to open Website Support Section."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["inv", "INV", "INVENTORY"])
async def inventory(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/inventory) to open your Inventory."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["BANK"])
async def bank(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
        description=f"[Click Here](https://animesoul.com/bank) to open your bank."
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["noti", "NOTI"])
async def notification(ctx):
    embed = discord.Embed(
        colour=ctx.author.top_role.colour,
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
   
@bot.command(aliases=["cal","CAL"])
async def calculate(ctx, operation, *nums):
    if operation not in ['+', '-', '*', '/']:
        embed= discord.Embed(
            colour=discord.Colour.red(),
            description=("Please type a valid operation. `Ex: + 25 9`")
        )
        await ctx.send(embed=embed)
    var = f' {operation} '.join(nums)
    await ctx.send(f'> `Result = {eval(var)}`')


bot.run(TOKEN)
