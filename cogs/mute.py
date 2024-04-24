import datetime

import disnake
from disnake.ext import commands


class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.slash_command(description="Замутить участника")
    async def timeout(self, interaction, member: disnake.Member, time: str, reason: str):
        try:
            time = datetime.datetime.now() + datetime.timedelta(minutes=(int(time)))
            await member.timeout(reason=reason, until=time)
            cool_time = disnake.utils.format_dt(time, style='R')
            embed= disnake.Embed(title='Timeout', description=f'{member.mention} has been timed out untill {cool_time}',
                                 color=disnake.Color.green())
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except disnake.Forbidden as e:
            # Handle permissions error
            await interaction.response.send_message(f"Bot doesn't have the required permissions: {e}")

    @commands.has_permissions(kick_members=True)
    @commands.slash_command(description="Размутить участника")
    async def untimeout(self, interaction, member: disnake.Member):
        await member.timeout(reason=None, until=None)
        await interaction.response.send_message(f'Untimed out {member.mention}', ephemeral=True)

def setup(bot):
    bot.add_cog(Timeout(bot))