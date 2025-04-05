import discord
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_meme():
    try:
        response = requests.get('https://meme-api.com/gimme')
        response.raise_for_status()
        json_data = response.json()
        return json_data.get('url', 'No meme found.')
    except requests.RequestException as e:
        print(f"API Error: {e}")
        return "Couldn't fetch a meme at the moment 😢"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$meme'):
            meme_url = get_meme()
            await message.channel.send(meme_url)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_BOT_TOKEN'))
