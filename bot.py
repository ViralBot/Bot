#!/usr/bin/env python
"""
Bot runner.
"""
import os

from discordbot.bot import DiscordBot
from discordbot.consts import bot_config

if __name__ == "__main__":
    bot = DiscordBot(command_prefix=bot_config["bot"]["command_prefix"], description="")
    bot.filename = os.path.basename(__file__)
    bot.run()
