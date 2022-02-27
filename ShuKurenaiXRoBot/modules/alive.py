#This Module Made By @AASFCYBERKING
#kanged with credits
#I Really Hardworked For This Module
#So Plz Give Credits
import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from ShuKurenaiXRoBot.events import register
from ShuKurenaiXRoBot import telethn as borg
from ShuKurenaiXRoBot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins

edit_time = 5
""" =======================SHU====================== """
file1 = "https://telegra.ph/file/1addac20ddebf7e6263e9.jpg"
file2 = "https://telegra.ph/file/65ff3335b58bd6a77b88e.jpg"
file3 = "https://telegra.ph/file/80d0fb8e77504577ad6b6.jpg"
file4 = "https://telegra.ph/file/27c128a3ba4517e147283.jpg"
file5 = "https://telegra.ph/file/199cfe7a146b6a805f2da.jpg"
""" =======================SHU====================== """

BUTTON = [[Button.url("sᴜᴘᴘᴏʀᴛ🚑", "https://t.me/Blaze_Support"), Button.url("ᴜᴘᴅᴀᴛᴇs💖", "https://t.me/THE_BLAZE_NETWORK")]]


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    await yes.delete()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    pm_caption = "** ♡ I,m ShuKurenai **\n\n"
    pm_caption += f"**♡ My Uptime :** `{uptime}`\n\n"
    pm_caption += f"**♡ Telethon Version :** `{version.__version__}`\n\n"
    pm_caption += "**♡ My Master :** [HARSHA](https://t.me/harshahero)\n"
    BUTTON = [[Button.url("ᴜᴘᴘᴏʀᴛ🚑", "https://t.me/Blaze_Support"), Button.url("Updates💖", "https://t.me/THE_BLAZE_NETWORK")]]
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption, buttons=BUTTON)
    

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2, buttons=BUTTON) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file2, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file3, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file5, buttons=BUTTON)
