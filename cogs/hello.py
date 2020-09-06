from discord.ext.commands import Bot, Cog, Context, command


class Echo(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command
    def hello(self, ctx: Context):
        ctx.send("hello")


def setup(bot: Bot) -> None:
    bot.add_cog(Echo(bot))