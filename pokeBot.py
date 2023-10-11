import requests
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("listening...")

@bot.command()
async def pokemon(ctx, pokemon: str):
    
    #Build API request.

    base = "https://pokeapi.co/api/v2/"

    url = f"{base}pokemon/{pokemon}"

    response = requests.get(url)

    if response.status_code == 200:
        
        package = response.json()
        
        menu = discord.Embed(
            title=package["name"],
            color = discord.Color.yellow()
        )

        type = package['types'][0]['type']['name']

        #Color embed based on type of pokemon.
        if type == 'normal':
            menu.color = discord.Color(0xA8A77A)
        elif type == 'fire':
            menu.color = discord.Color(0xEE8130)
        elif type == 'water':
            menu.color = discord.Color(0x6390F0)
        elif type == 'electric':
            menu.color = discord.Color(0xF7D02C)
        elif type == 'grass':
            menu.color = discord.Color(0x7AC74C)
        elif type == 'ice':
            menu.color = discord.Color(0x96D9D6)
        elif type == 'fighting':
            menu.color = discord.Color(0xC22E28)
        elif type == 'poison':
            menu.color = discord.Color(0xA33EA1)
        elif type == 'ground':
            menu.color = discord.Color(0xE2BF65)
        elif type == 'flying':
            menu.color = discord.Color(0xA98FF3)
        elif type == 'psychic':
            menu.color = discord.Color(0xF95587)
        elif type == 'bug':
            menu.color = discord.Color(0xA6B91A)
        elif type == 'rock':
            menu.color = discord.Color(0xB6A136)
        elif type == 'ghost':
            menu.color = discord.Color(0x735797)
        elif type == 'dark':
            menu.color = discord.Color(0x705746)
        elif type == 'steel':
            menu.color = discord.Color(0xB7B7CE)
        elif type == 'fairy':
            menu.color = discord.Color(0xD685AD)
        elif type == 'dragon':
            menu.color = discord.Color(0x6F35FC)

        #Build embed view: name of pokemon, weight/height of pokemon, first three attacks of pokemon.
        menu.add_field(name="Index:", value=package["id"], inline=False)
        menu.add_field(name="Weight(hg):", value=package["weight"], inline=False)
        menu.add_field(name="Height(dm):", value=package["height"], inline=False)
        moves=1
        for move in package['moves']:
            menu.add_field(name=f"Move {moves}:", value=move['move']['name'], inline=False)
            moves+=1
            if moves > 3:
                break
        menu.set_image(url=package['sprites']['front_default'])

        await ctx.reply(embed=menu)



    else:
        print("i got nothing")

    
    

bot.run("##############################")
