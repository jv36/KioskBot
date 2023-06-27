import discord
import requests
from discord import app_commands
from jornais import *



intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name = "jornal", description = "Capas dos jornais, escolhe o teu!", guild=discord.Object(id=562039874924970101))
@app_commands.describe(nomejornal = "Nome do jornal", dia = "Dia desejado", mes = "Mês desejado", ano = "Ano desejado")
async def jornal(interaction, nomejornal : str, dia = None, mes = None, ano = None):
    jornalID = jornais.get(nomejornal)
    cover = f"https://i.prcdn.co/img?file={jornalID}{ano}{mes}{dia}00000000001001&page=1&width=960"
    await interaction.response.send_message(cover)

@tree.command(name = "lista", description = "Lista dos jornais disponíveis", guild=discord.Object(id=562039874924970101))
async def lista(interaction):
    listaa = ""
    for key in jornais:
        lista += {key}

    await interaction.response.send_message(listaa)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=562039874924970101))
    print("Ready!")
e

client.run("TOKEN")