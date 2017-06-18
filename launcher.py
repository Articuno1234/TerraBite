try:
    import discord
    from discord.ext.commands import Bot
except ImportError:
        print("Discord.py is not installed!")
try:
    import logging
except ImportError:
        print("Logging is not installed")
try:
    import config
except ImportError:
        print("A file is out of place: config.py was not found!")
import os
import signal
import sys
import platform
import time
import random

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
description = '''Python'''
bot = Bot(command_prefix=config.PREFIX) # Sets the client and sets the prefix
@bot.command(pass_context=True)
async def game(ctx, game=None):
    """Set TerraBite's Game"""
    server = ctx.message.server
    author = ctx.message.author
    current_status = server.me.status if server is not None else None
    game = game.strip()
    await bot.change_presence(game=discord.Game(name=game),
status=current_status)
    await bot.say("__D__o__n__e! :smile:")
    await bot.whisper("Game was set to **{}**\n__**Terms & Conditions**__\nYou have just changed TerraBite's Game to **{}** if you __**ARE NOT**__ a TerraBite staff we will make an exception :smile:".format(game, game))
    await bot.say("Check your DM! :bookmark_tabs: ")
    print("Game was set to '({})' by ({})".format(game, author))
@bot.command(pass_context=True)
async def invite(ctx, game=None):
    """Invite TerraBite.py"""
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Invite :smile:', value=("[Invite Here!](https://discordapp.com/oauth2/authorize?client_id=325183067297939456&scope=bot&permissions=-1)"))
    await bot.say(embed=em)
@bot.command(pass_context=True)
async def ping(ctx):
    """Pong."""
    em = discord.Embed(color=0x0BFCF2)
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    em.add_field(name='Ping :ping_pong: ', value=(str(round((t2-t1)*1000)) + "ms"))
    em.set_thumbnail(url= "https://discordapp.com/assets/f73a8294c3ac519665af224d98bf411e.svg")
    await bot.say(embed = em)
@bot.command(pass_context=True)
async def roll(ctx):
    """1. 2. 3. 4. 5. 6."""
    r = ["You rolled a 1", "You rolled a 2", "You rolled a 3", "You rolled a 4", "You rolled a 5", "You rolled a 6"]
    await bot.say(random.choice(r))
@bot.command(pass_context=True)
async def shutdown(ctx):
    """Shutsdown"""
    await bot.say("Shutting down...")
    sys.exit(1)
@bot.command(pass_context=True)
async def play(ctx, URL=None):
    """Play a song"""
    author = ctx.message.author
    server = ctx.message.server
    voice_channel = author.voice_channel
    await voice_channel(voice_channel)

@bot.command(pass_context=True)
async def lenny(ctx):
    """( ͡° ͜ʖ ͡°)"""
    RLEN = ["( ͡° ͜ʖ ͡°)", "(⌐□_□)", "(づ◔ ͜ʖ◔)づ", "^‿^", "⤜(ʘ_ʘ)⤏", "ಠ_ಠ", "¯\_ツ_/¯", "(⏒ᴥ⏒)", "( ͡°╭͜ʖ╮ ͡°)", "⎝◕◞ ◕⎠", "ᘳ ͡° ͜ʖ ͡°ᘰ", "ᕙ(⌐■ ͜ʖ■)ᕗ", "୨ ͡⎚ ʖ̯ ͡⎚୧", "乁(σ ε σ)ㄏ", "乁(σ ε σ)ㄏ", "(╭☞σ ͜つσ)╭☞", "¯\_ಠ ͜つಠ_/¯", "(╯ º ‿ º ）╯︵ ┻━┻", "( ͡°▾ ͡°)", "(⊜ ʖ̯⊜)", "ლ(◉ᗜ◉ლ)", "	¯\_ᵔ ͜ʖᵔ_/¯", "ʢ◉ᴥ◉ʡ", "´• ل͜ •`"]
    await bot.say("All Lennys are from <http://textsmili.es> :smile: (`Will take 1sec to load`)")
    time.sleep(1)
    await bot.say(random.choice(RLEN))

users = len(set(bot.get_all_members()))
servers = len(bot.servers)
channels = len([c for c in bot.get_all_channels()])
@bot.command(pass_context=True)
async def info(ctx):
    """Play a song"""
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Bot Owner', value=(config.OWNER))
    em.add_field(name='Server Count', value=(len(bot.servers)))
    em.add_field(name='User Count', value=(len(set(bot.get_all_members()))))
    em.add_field(name='Description', value=("TerraBite is a W.I.P Discord Bot\n[Website](https://terrabite.cf/)"))
    em.set_footer(text='Version {}'.format(discord.__version__))
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/321206777175605251/325812728683954176/tb.py.png")
    await bot.say(embed = em)
def windows_startup():
    print("Operating System is " + platform.system())
    print("Starting Bot For Windows System")
    print("Starting Bot")
    signal.signal(signal.SIGINT, sig_handler)
    bot.run(config.TOKEN)
    clear_screen()
    print("Terrabite Discord Bot by: Oskikiboy, Motasim, Cringy Adam, Haxmat, Blackberry Pi and Codefox")
    print("\nTerraBite (system) Loaded!")

def linux_startup():
    print("Operating System is " + platform.system())
    print("Starting Bot")
    signal.signal(signal.SIGINT, sig_handler)
    bot.run(config.TOKEN)
    print("Terrabite Discord Bot by: Oskikiboy, Motasim, Cringy Adam, Haxmat, Blackberry Pi and Codefox")
    print("\nTerraBite (system) Loaded!")
    
def mac_startup():
    print("Operating System is " + platform.system())
    print("Starting Bot")
    signal.signal(signal.SIGINT, sig_handler)
    bot.run(config.TOKEN)
    print("Terrabite Discord Bot by: Oskikiboy, Motasim, Cringy Adam, Haxmat, Blackberry Pi and Codefox")
    print("\nTerraBite (system) Loaded!")

if len(sys.argv) > 1:
    if sys.argv[1] == "install":
        print("Installing Dependencies")
        os.system("npm install")
        print("Installing PM2")
        os.system("npm install -g pm2")
        bot.run(config.TOKEN)
clear_screen()
print("""                                                                                          
    __    ____  ___    ____  _____   ________             
   / /   / __ \/   |  / __ \/  _/ | / / ____/             
  / /   / / / / /| | / / / // //  |/ / / __               
 / /___/ /_/ / ___ |/ /_/ // // /|  / /_/ /  _    _    _  
/_____/\____/_/  |_/_____/___/_/ |_/\____/  (_)  (_)  (_) 
                                                                                                                                                                                                                                                                                                                              
""")
time.sleep(5)
clear_screen()

def sig_handler(signal, frame):
    print("Shutting Down")
    os.system("pm2 kill")
    sys.exit(0)

print("Checking Operating System")

if platform.system() == "Windows":
          windows_startup()
elif platform.system() == "Linux":
          linux_startup()
elif platform.system() == "macosx":
          mac_startup()
          
else:
          print("Unknown Operating System. Please use either Linux, Mac or Windows")

print("The Bot is Running. Press CTRL+C to Exit")
