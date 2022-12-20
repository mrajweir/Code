from discord.ext import commands
import discord
import json

with open("discord-properties.json", "r") as f:
    discord_properties = json.load(f)

client = discord.Client()
bot = commands.Bot(command_prefix="!")

@bot.command(name="graph")
async def test_test(ctx):
        await ctx.send("Gonna make you a graph, gonna cook it up _real_ nice...")

bot.run(discord_properties["token"])