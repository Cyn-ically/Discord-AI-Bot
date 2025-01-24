import re
import random
import json 
import sys  
from duckduckai import ask as duckduckai_ask
import discord
from discord import app_commands

CONFIG_FILE = "config.json"

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{CONFIG_FILE}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Configuration file '{CONFIG_FILE}' is not valid JSON.")
        sys.exit(1)

    if "bot_token" not in config:
        print("Error: 'bot_token' is missing in the configuration file.")
        sys.exit(1)

    if "watermark_enabled" not in config:
        config["watermark_enabled"] = True

    if "personality_enabled" not in config:
        config["personality_enabled"] = False

    return config

config = load_config()
BOT_TOKEN = config["bot_token"]
WATERMARK_ENABLED = config["watermark_enabled"]
PERSONALITY_ENABLED = config["personality_enabled"]

REPOSITORY_URL = "https://github.com/Ramona-Flower/Discord-AI-Bot"

SUPPORTED_MODELS = [
    "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    "claude-3-haiku-20240307",
    "gpt-4o-mini"
]

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

bot = MyBot()

def redact_response(response):
    """Redact URLs and mentions from the response."""
    response = re.sub(r'http[s]?://\S+', '<redacted>', response)  
    response = re.sub(r'@\w+', '<redacted>', response)  
    return response

@bot.tree.command(name="ask")
@app_commands.describe(
    query="Your query",
    personality="The personality for the bot to use (optional)"
)
@app_commands.choices(
    model=[
        app_commands.Choice(name="Mixtral-8x7B", value="mistralai/Mixtral-8x7B-Instruct-v0.1"),
        app_commands.Choice(name="Meta-Llama-70B", value="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"),
        app_commands.Choice(name="Claude-3-Haiku", value="claude-3-haiku-20240307"),
        app_commands.Choice(name="GPT-4o-Mini", value="gpt-4o-mini")
    ]
)
async def ask_command(interaction: discord.Interaction, model: app_commands.Choice[str], query: str, personality: str = None):
    """Slash command to interact with DuckDuckAI."""
    await interaction.response.defer() 

    if PERSONALITY_ENABLED and personality:
        query = f"Act as: {personality} and respond to the question in the language of the query.\n\n{query}"

    query = "\n\nDo not use any insult in the output, now respond to this question. : "  +query 

    try:
        response = duckduckai_ask(query, model=model.value, stream=False)
        redacted_response = redact_response(response)

        random_color = discord.Color(random.randint(0, 0xFFFFFF)) 
        if personality:
            personality = personality.capitalize()
        embed = discord.Embed(
            title=f"Response from {model.name} with the {personality} personality" if personality  else f'Response from {model.name}',
            description=redacted_response,
            color=random_color  
        )

        if WATERMARK_ENABLED:
            watermark_text = f"[Created using Discord AI Bot]({REPOSITORY_URL})"
            embed.add_field(name="About", value=watermark_text, inline=False)

        await interaction.followup.send(embed=embed)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {str(e)}", ephemeral=True)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

if __name__ == "__main__":
    bot.run(BOT_TOKEN)
