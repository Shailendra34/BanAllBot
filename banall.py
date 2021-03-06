from client import Var
import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


hero = TelegramClient(None, Var.API_KEY, Var.API_HASH)
hero.start(bot_token=Var.TOKEN)

print("ššš¼ššššš š½š¼šš¼šš š½šš šššššš....") 

"""
šššššš šš š¾šššš¼ššæš ššš.... 
"""

Lund = []
for x in Var.OWNER_ID: 
    Lund.append(x)


@hero.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in Lund:
        start = datetime.now()
        text = "šš¤š£š...."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**š'š¢ š¼šš©šš«šš„\nšš©šš§š© ššŖšš šš£š š¼š£š® šš§š¤šŖš„** \n\n **__į¢į¾įį¶š__** `{ms}` ms")

"""
 ššššš¼šš š¾šššš¼ššæš.... 
"""
@hero.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in Lund:
        text = "š šš¢ š§šššš® š©š¤ ššŖšš  š©šš§ššš©šš šš§š¤šŖš„šØ...."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await hero.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

"""
 š½š¼šš¼šš š¾šššš¼ššæ... 
"""
 
@hero.on(events.NewMessage(pattern="^/banall"))
async def testing(event):
  if event.sender_id in Lund:
   if not event.is_group:
        Reply = f"šš¤š¤š ššØš ššššØ š¾š¢š šš£ šš§š¤šŖš„..."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       veer = await event.get_chat()
       veerA = await event.client.get_me()
       admin = veer.admin_rights
       creator = veer.creator
       if not admin and not creator:
           await event.reply("š šæš¤š£'š© ššš«š šØšŖššššššš£š© š§šššš©šØ...")
           return
       await event.reply("**šš©šš§š©šš ššŖšš šš£š š©šššØ šš§š¤šŖš„...**")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == veerA.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


print("šššš«š š¾š¤š¢š¢šš£š šš¤š¤š£ š¾šŖš§š§šš£š©š”š® š¼š¢ š½šŖšØš®") 
print("ššš¼ššššæ ššš¾š¾šššššššš...") 
hero.run_until_disconnected()
