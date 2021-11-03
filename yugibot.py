import discord

TOKEN = 'OTA1NDU4NDQxODMxNzI3MTU1.YYKX4w.4YTfqhI3qVg7lCqM4LWEWDBDFxs'

client = discord.Client()

@client.event
async def on_ready():
    print("We have Logged in as {0.user}".format(client))



@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return
    
    if message.channel.name == 'yugi':
        if user_message.lower() == 'hello':    
            await message.channel.send(f'Hello {username}! :D')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f"Bye {username}! :(")
            return
        if user_message.lower() == "fuck you":
            await message.channel.send(f"No fuck you {username}! >:[")
            return
        if user_message.lower() == "cool":
            await message.channel.send(f"I know! xd")
            return
        if user_message.lower() == "<@!905458441831727155>":
            await message.channel.send("Hello I'm under development rn so Stop mentioning me! >:[")
            return
        if user_message.lower() == "help":
            await message.channel.send("```So far this is the commands \nHello, Bye, fuck you, cool\n\n\nI am not finish being built yet  >:[```")
            return
client.run(TOKEN)
