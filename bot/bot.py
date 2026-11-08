import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

load_dotenv('/app/.env')
TOKEN = os.getenv('DISCORD_TOKEN')

logging.basicConfig(
    filename='/app/logs/bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')
    logging.info(f'Bot iniciado: {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'🏓 Pong! Latencia: {round(bot.latency * 1000)}ms')
    logging.info(f'Comando ping usado por {ctx.author}')

@bot.command()
async def estado(ctx):
    ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f'✅ Sistema activo\n🕐 Hora: {ahora}')
    logging.info(f'Comando estado usado por {ctx.author}')

@bot.command()
@commands.has_permissions(administrator=True)
async def info(ctx):
    servidor = ctx.guild
    await ctx.send(
        f'📊 **Servidor:** {servidor.name}\n'
        f'👥 **Miembros:** {servidor.member_count}\n'
        f'📅 **Creado:** {servidor.created_at.strftime("%Y-%m-%d")}'
    )

bot.run(TOKEN)
