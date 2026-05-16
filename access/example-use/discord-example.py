#this is how you can use the quotes, as I am a bot dev of Discord so I am using that way, took an hour or more to make it because there was a little issue I fixed

import discord
import requests
import xmltodict
import random
from discord.ext import commands

intents=discord.Intents.all()
bot=commands.Bot("?",intents=intents)

response=requests.get("https://akirathedarktempest-lgtm.github.io/AnimeQ-XML-File/main/AnimeQ.xml")
dictionary=xmltodict.parse(response.text)
quotes=dictionary["quotes"]
description=quotes["description"]

@bot.event
async def on_ready():
    print("The bot is ready!")
    await bot.tree.sync()

@bot.tree.command()
async def description(interaction:discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    await interaction.followup.send(description)

@bot.command()
async def showQuotes(ctx:commands.Context,name:str):
    name=name.title()
    if "\'" in name:#you all may ask, why this is here...this took me more 45 minutes to solve
        number=name.index("\'")#basically, the problem is, we have one show, a novel ORV also known as Omniscient Reader's Viewpoint
        if name[-1]==name[number]:#and that s in Reader's was becoming capital because of the title method of string, and it was considering it as a seperate word because of ' and i realized it
            pass#at oshi no ko, it worked all well but not at orv, I started thinking what's wrong here
        else:#and we came to this conclusion...and huff, it finally worked...I am exhausted but happy that I SOLVED ANOTHER PROBLEM ON MY OWN! I am a coder for a reason guys...
            name=name.replace(name[number+1],name[number+1].lower())

    show=quotes["show"]
    for i in show:
        if i["name"]==name:
            desc=""
            character=i["character"]
            for i in character:
                if type(i["quote"]) is str:
                    desc+=f"*{i["quote"]} ~ {i["character-name"]}*\n\n"
                elif type(i["quote"]) is list:
                    for z in i["quote"]:
                        desc+=f"*{z} ~{i["character-name"]}*\n\n"
                else:
                    return await ctx.send("Something is wrong at else!")
            embed=discord.Embed(title=f"{name} Quotes!",description=desc)
            return await ctx.send(embed=embed)
        else:
            pass
    await ctx.send("Couldn't find the show from the XML :(")

bot.run('TOKEN')
