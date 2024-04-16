import disnake
from disnake.ext import commands

class InteractiveEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message = None
        self.yes_users = []
        self.no_users = []

    @commands.command()
    async def create_embed(self, ctx):
        embed = disnake.Embed(title="Interactive Embed", description="React with ✅ or ❌")
        self.message = await ctx.send(embed=embed)
        await self.message.add_reaction("✅")
        await self.message.add_reaction("❌")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.bot.user or reaction.message.id != self.message.id:
            return

        if str(reaction.emoji) == "✅":
            if user not in self.yes_users:
                self.yes_users.append(user)
                if user in self.no_users:
                    self.no_users.remove(user)
            await self.update_embed()
        elif str(reaction.emoji) == "❌":
            if user not in self.no_users:
                self.no_users.append(user)
                if user in self.yes_users:
                    self.yes_users.remove(user)
            await self.update_embed()

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user == self.bot.user or reaction.message.id != self.message.id:
            return

        if str(reaction.emoji) == "✅":
            if user in self.yes_users:
                self.yes_users.remove(user)
            await self.update_embed()
        elif str(reaction.emoji) == "❌":
            if user in self.no_users:
                self.no_users.remove(user)
            await self.update_embed()

    async def update_embed(self):
        embed = disnake.Embed(title="Interactive Embed", description="React with ✅ or ❌")
        if self.yes_users:
            embed.add_field(name="Yes", value='\n'.join(user.display_name for user in self.yes_users), inline=True)
        if self.no_users:
            embed.add_field(name="No", value='\n'.join(user.display_name for user in self.no_users), inline=True)
        await self.message.edit(embed=embed)

def setup(bot):
    bot.add_cog(InteractiveEmbed(bot))
