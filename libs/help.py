import sys
import time
from libs.extras import to_discord_str
from discord import Embed
from libs.config import BotConfig as Config


def print(animation):
    temp_str = "[ BOT ] "
    for i in animation:
        temp_str += i
        time.sleep(0.01)
        sys.stdout.write("\r" + temp_str)
        sys.stdout.flush()
    sys.stdout.write("\n")


class EmbedHelp:
    def __init__(self, parent, accepted_args=None):
        self.parent = parent
        self.accepted_args = accepted_args
        self.prefix = Config().get('prefix')

    async def __call__(self):
        embed = Embed(
            title="Usage"
        )
        if self.accepted_args:
            description = f"[C]{self.prefix}{self.parent.name}"
            for i in self.accepted_args:
                description += f" [{i}]"
                embed.description = to_discord_str(description + "[C]")
                self.accepted_args = ', '.join(self.accepted_args)
                embed.add_field(name="Args", value=to_discord_str(f"[C]{self.accepted_args}[C]"))
        if self.parent.help:
            embed.add_field(name=f"Help", value=to_discord_str(f"[C]{self.parent.help}[C]"))
        if self.parent.aliases:
            embed.add_field(name="Aliases", value=to_discord_str(f"[C]{', '.join(self.parent.aliases)}[C]"))

        return embed

    def __repr__(self):
        print(f"({self.parent}, {self.accepted_args})")

