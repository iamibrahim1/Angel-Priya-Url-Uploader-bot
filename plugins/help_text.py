#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    if update.from_user.id in Config.AUTH_USERS:
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.HELP_USER,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
        )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    if update.from_user.id in (Config.AUTH_USERS & Config.LAZY_DEVELOPER):
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.LAZY_DEVELOPER_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url="https://t.me/+NB9dvtZfvWUyNzRk"),
                        InlineKeyboardButton("⚡️ 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url="https://t.me/real13xx"),
                    ],
                    [InlineKeyboardButton("⭑💢 𝙎𝙤𝙘𝙞𝙖𝙡 💢⭑", url="https://wa.link/mgcx1z")],
                    [InlineKeyboardButton("⭑┗━━┫𝙊𝙬𝙣𝙚𝙧 ┣━━┛⭑", url="https://t.me/hater786")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
    elif update.from_user.id in Config.AUTH_USERS:
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url="https://t.me/+NB9dvtZfvWUyNzRk"),
                        InlineKeyboardButton("⚡️ 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url="https://t.me/real13xx"),
                    ],
                    [InlineKeyboardButton("⭑💢 𝙎𝙤𝙘𝙞𝙖𝙡 💢⭑", url="https://wa.link/mgcx1z")],
                    [InlineKeyboardButton("⭑┗━━┫𝙊𝙬𝙣𝙚𝙧 ┣━━┛⭑", url="https://t.me/hater786")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
    else:
        # logger.info(update) ==         
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.LAZY_START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⭑┗━━┫𝙊𝙬𝙣𝙚𝙧 ┣━━┛⭑", url="https://t.me/hater786")],
                    [
                        InlineKeyboardButton("⚡️ 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url="https://t.me/real13xx"),
                    ],
                    [InlineKeyboardButton("⭑💢 𝙎𝙤𝙘𝙞𝙖𝙡 💢⭑", url="https://wa.link/mgcx1z")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
         
