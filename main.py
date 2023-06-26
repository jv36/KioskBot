import discord
from discord import app_commands
from jornais import *


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name = "jornal", description = "Capas dos jornais, escolhe o teu!", guild=discord.Object(id=12417128931))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=Your guild id))
    print("Ready!")

client.run("TOKEN")