from disnake.ext import commands
import disnake


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(ban_members=True)
    @commands.slash_command(description="Забанить участника")
    async def ban(self, interaction, user: disnake.User, *, reason=None):
        await interaction.guild.ban(user, reason=reason)
        await interaction.response.send_message(f'Bannned {user.mention}', ephemeral=True)

    @commands.has_permissions(ban_members=True)
    @commands.slash_command(description="Разбанить участника")
    async def unban(self, interaction, user:disnake.User):
        await interaction.guild.unban(user)
        await interaction.response.send_message(f'Unbannned {user.mention}', ephemeral=True)


def setup(bot):
    bot.add_cog(Ban(bot))