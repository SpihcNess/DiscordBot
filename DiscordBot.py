import discord
from discord.ext import commands as cmd

# CREATION DU TOKEN
token = "OTU2MjA3NTA1MDQ0ODMyMzI2.Yjs3og.KQuny46KaulepOo82AQcXobh3yg"
# CREATION DU CLIENT
client = discord.Client()
# DEFINITION DU PREFIXE DE CHAQUE COMMANDE
bot = cmd.Bot(command_prefix = "!")

# MESSAGE WHEN LE BOT IS EN LIGNE
@client.event
async def on_ready():
    print("client en ligne")
@bot.event
async def on_ready():
    print("bot en ligne")

# MESSAGE WHEN QQUN MET UN MESSAGE PARTICULIER
#@bot.event
#async def on_message(message):
#    if (message.content.lower() == "ping"):
#        await message.channel.send("ta gueule")
#    elif (message.content.lower() == "mais..."):
#        await message.channel.send("**TA GUEULE**")

@bot.command(name = "del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit = number + 1).flatten()
    for message in messages:
        await message.delete()

bot.run(token)