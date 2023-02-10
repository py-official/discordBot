import disnake
from disnake.ext import commands
from aternosPlugin import Start, Stop
from objCreator import CreateEmbed


bot = commands.Bot(command_prefix="~", help_command=None, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f"Successful!!\nBot {bot.user} is ready to work!")

@bot.command()
async def start(ctx):
    await ctx.send(embed=CreateEmbed(Start()))

@bot.command()
async def stop(ctx):
    await ctx.send(embed=CreateEmbed(Stop()))
    

def runBot():
    print("Try to start discord bot")
    try:
        bot.run(token)
    except:
        print("Error of starting bot")    
