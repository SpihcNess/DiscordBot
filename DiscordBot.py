class DiscordBot(object):
    name = ""

    # Setters

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

    # Functions