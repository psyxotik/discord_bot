from disnake.ext import commands
import disnake

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def info(self):
        
