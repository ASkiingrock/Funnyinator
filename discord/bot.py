import datetime
import nextcord
import random
import re
import json
import wordfile_downloader
from nextcord.ext import commands

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="*", intents=intents)

bot.remove_command('help')


@bot.event
async def on_message(message):
    if isinstance(message.channel, nextcord.channel.DMChannel) and not message.author.bot:
        devs = []
        with open("DISCORD_IDS", "r") as f:
            for disc_id in f.readlines():
                devs.append(bot.get_user(int(disc_id)))

        if message.author not in devs:
            for dev in devs:
                await dev.send(f"Hi! I received a message from {message.author.name}:")
                await dev.send(f"\"{message.content}\"")
            await message.channel.send("Thank you so much for the message. I've forwarded it to the developers.")

    await bot.process_commands(message)


@bot.command()
async def help(ctx):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S %d/%m")

    await ctx.send("This is the correspondent for Smelk Innovations, the company that's real.")
    embed = nextcord.Embed(colour=nextcord.Colour.yellow())
    embed.set_author(name="Smelk")
    embed.add_field(name="*funnyinator", value="Make any message funny in one command")
    embed.add_field(name="*suggest", value="Send a helpful suggestion to the devs")
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)


@bot.command()
async def funnyinator(ctx):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S %d/%m")
    print(f"[{timestamp}] {ctx.author.name} used Funnyinator in #{ctx.channel.name}")

    if ctx.message.reference:
        referenced_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        input_string = referenced_message.content
    else:
        async for message in ctx.channel.history(limit=2):
            input_string = message.content

    with open("words.json", "r", encoding="utf-8") as input_file:  # Words to be replaced are extracted from JSON file
        words = json.load(input_file)

    words_list = words["replacements"].keys()  # The list of words to be replaced

    replaced_string = input_string
    for word in words_list:
        replaced_string = replaced_string.lower()
        replaced_string = re.sub(f"\\b{word}\\b", words["replacements"][word], replaced_string)

    output_string = replaced_string.split(" ")
    for word_count, word in enumerate(output_string):
        if random.randint(1, 25) == 1 and "\n" not in word:  # Add in random 'funny' word given 1/25 chance
            funny_word = random.choice(words["funny_words"])
            output_string[word_count] += f" {funny_word}"
    try:
        await ctx.send(" ".join(output_string))
    except nextcord.errors.HTTPException:
        # Split between messages when too long
        output_string_a = output_string[:len(output_string)//2]
        output_string_b = output_string[len(output_string)//2:]
        await ctx.send(" ".join(output_string_a))
        await ctx.send(" ".join(output_string_b))


@bot.command()
async def suggest(ctx, *, suggestion):
    await ctx.send("Your suggestion has be sent out to Smelk Innovations Developers, thank you.")

    devs = []
    with open("DISCORD_IDS", "r") as f:
        for disc_id in f.readlines():
            devs.append(bot.get_user(int(disc_id)))

    for dev in devs:
        await dev.send(f"Hey there, you've got one suggestion from {ctx.author.name}:")
        await dev.send(f"\"{suggestion}\"")


@bot.command()
async def redownload(ctx):
    devs = []
    with open("DISCORD_IDS", "r") as f:
        for disc_id in f.readlines():
            devs.append(bot.get_user(int(disc_id)))

    if ctx.author in devs:
        await ctx.author.send("Redownloading files")
        wordfile_downloader.download()


@bot.event
async def on_ready():
    print("Ready")
    print(f"Running in {len(bot.guilds)} servers:")
    for guild in bot.guilds:
        print(f"- {guild.name}")


with open("TOKEN", "r") as f:
    token = f.read()
bot.run(token)
