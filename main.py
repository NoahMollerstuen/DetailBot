import discord
import json
import datetime
import random

with open("secret.json") as f:
    token = json.load(f)["token"]

with open("detail.json") as f:
    detail_data = json.load(f)

with open("quotes.txt", encoding="utf-8") as f:
    quotes = f.readlines()


class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        weekday = datetime.datetime.now().weekday()
        today_data = detail_data[weekday]
        channel_id = today_data["channel_id"]
        today_users = today_data["user_ids"]
        channel = self.get_channel(channel_id)
        msg = " ".join([f"<@{u}>" for u in today_users])
        msg += " Remember to do your detail tonight!\n"
        msg += random.choice(quotes)
        await channel.send(msg)
        await self.close()


intents = discord.Intents.default()
client = Client(intents=intents)
client.run(token)
