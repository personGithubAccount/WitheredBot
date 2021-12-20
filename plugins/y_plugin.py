import re
from requests import get
from discord.ext import commands
from discord import Embed
from .help_func import embed_help, msgf


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yt(self, ctx, *args):
        """Search The Youtube"""
        args = " ".join(args).replace(" ", "-")
        if args.strip() == "":
            await ctx.send(
                embed=await (embed_help(self.yt, accepted_args=['Search'])))
        else:
            message = await ctx.send(embed=Embed(title="Youtube", description=f"searching for `{args}`"))
            request_yt = get(
                f"https://www.youtube.com/results?search_query={args}"
            )
            yt_link = re.findall(r"watch\?v=(\S{11})", request_yt.content.decode())
            await message.delete()
            await ctx.send(
                content=msgf(
                    f"[Q/][H]https://www.youtube.com/watch?v={yt_link[0]}[H]"
                ), embed=None
            )


def setup(bot) -> dict:
    return {"Object": Init(bot), "name": "YouTube", "description": "Adds Ability to Search Youtube videos"}
