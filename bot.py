import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} logou com sucesso!')

@bot.command(name='cl')
async def clear_messages(ctx, amount: int = 50):
    if ctx.guild is not None:
        await ctx.send("❌ Apenas em DM!")
        return
    
    deleted = 0
    async for message in ctx.channel.history(limit=100):
        if message.author == ctx.author and deleted < amount:
            await message.delete()
            deleted += 1
    
    await ctx.send(f'✅ Apagadas {deleted}!', delete_after=3)

bot.run('MTM1NTMxODgxMTEyNDgzMDI2OA.G04Uzb.GYe0x19lNPqIOa8NYkBkSooAT-KECDOFE4yCjU')