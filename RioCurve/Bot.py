import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import graph

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='graph')
async def nine_nine(ctx, role: str):
    g = graph.Graph(role)
    graph_path = g.generate()
    await ctx.send(file=discord.File(graph_path))

bot.run(TOKEN)


"""
Possible structures

By role
By class
By spec
By faction
By server
"""