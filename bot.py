import discord
from discord.ext import commands
import get_model

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Здравствуй, я {bot.user}.')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def save(ctx):
    if ctx.message.attachments != []:
        # for-each 
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            await attachment.save(filename)
            result = get_model.detect_object(filename)
            await ctx.send("Файл успешно сохранён")
            await ctx.send(result)

bot.run("MTIxMzQwNTc4MDE5MjAwNjE3NA.GAxF7P.IuRyKGoa1m_1kUsQiyUBOjuh3HC0y4KpgwsFSo")
