import nextcord
import random
import re
import json
from nextcord.ext import commands

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="*", intents=intents)

bot.remove_command('help')


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.command()
async def help(ctx):
    await ctx.send("This is the correspondent for Smelk Innovations, the company that's real.")


@bot.command()
async def funnyinator(ctx):
    async for message in ctx.channel.history(limit=2):
        input_string = message.content

    with open("../words.json", "r", encoding="utf-8") as input_file:  # Words to be replaced are extracted from JSON file
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

    await ctx.send(" ".join(output_string))


@bot.event
async def on_ready():
    print("Ready")
    print(f"Running in {len(bot.guilds)} servers:")
    for guild in bot.guilds:
        print(guild.name)


with open("TOKEN", "r") as f:
    token = f.read()
bot.run(token)
