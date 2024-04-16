from disnake.ext import commands
import disnake


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def avatar(self, interaction, member: disnake.Member = None):
        user = member or interaction.author
        embed = disnake.Embed(title='Avatar', color=0x314fe8)
        embed.set_image(url=user.display_avatar.url)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))