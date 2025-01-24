# Discord AI Bot

- A versatile Discord bot powered by AI models like Mixtral, Meta-Llama, Claude-3, and GPT-4. This bot allows users to interact with various AI models through a simple /ask command, with optional personality customization.

# 🛠️ Setup Instructions
Clone the Repository:

```
git clone https://github.com/Ramona-Flower/Discord-AI-Bot.git
cd Discord-AI-Bot
```

### Install Dependencies:
```
pip install -r requirements.txt
```
Configure the Bot:

Modify the config.json with the following structure:

```json

{
  "_comment_": "Watermark is if you want to support my creation ! but is not required",

  "bot_token": "YOUR_BOT_TOKEN_HERE",
  "watermark_enabled": true,
  "personality_enabled": true
}
```
### Replace YOUR_BOT_TOKEN_HERE with your Discord bot token.

# Run the Bot:

```
python main.py
```
## ⚙️ Configuration Options
``` 
bot_token: Your Discord bot token (required).

watermark_enabled: Set to true to display a watermark in the bot's responses (default: true).

personality_enabled: Set to true to allow users to specify a personality for the bot (default: false).
``` 
## 🤖 Commands
- ```/ask```: Ask the bot a question.

Parameters:
```
query: Your question.

model: The AI model to use (e.g., Mixtral-8x7B, Meta-Llama-70B).

personality (optional): A custom personality for the bot (if enabled).
```

# ❓ Support
If you have any questions or need help, feel free to open an issue on GitHub or contact the maintainers. I'm not responsible for any of the misuse this program could lead to ❤️

# ⚠️ Important: Do Not Use Replit
#### Replit is not recommended for hosting this bot due to significant security and performance concerns:

## Security Risks:

- Replit exposes your bot's token and other sensitive information publicly, even in private projects.
This makes it easy for malicious actors to steal your bot token and compromise your bot.

- Performance Issues:
Replit is not designed for long-running processes like Discord bots. Your bot may frequently disconnect or crash.

- Free-tier Replit projects sleep after inactivity, causing your bot to go offline.

### Lack of Control:

- Replit provides limited control over the environment, making it difficult to manage dependencies or debug issues.

- 🚀 Recommended Hosting Options
For better security, reliability, and performance, consider using one of the following hosting services:

##  PythonAnywhere
- Why Use It?:
PythonAnywhere is designed for hosting Python applications and provides a stable environment for running Discord bots.

- It offers better security and control over your bot's environment.

### How to Use:
- Upload your bot's code to PythonAnywhere.

- Set up a scheduled task to keep the bot running 24/7. or just click on the button once every 2 weeks/month

- Website: https://www.pythonanywhere.com

## Heroku
 - Why Use It?:
Heroku is a cloud platform that supports long-running processes and is easy to set up.
It provides a free tier for small projects.

- How to Use:
Deploy your bot using Heroku's Git integration.

- Website: https://www.heroku.com

## VPS (Virtual Private Server)
- Why Use It?:
A VPS gives you full control over the server environment, ensuring maximum security and performance.
Popular options include DigitalOcean, Linode, and AWS EC2.

- How to Use:
Set up a Linux server (e.g., Ubuntu).
Install Python and the required dependencies.
Run your bot as a background process using screen or systemd.

### Recommended Providers:
- DigitalOcean

- Linode

- AWS EC2


