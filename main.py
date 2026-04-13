import os
import asyncio
from telegram import Bot

# Get your token and ID from GitHub Secrets
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def send_poll():
    bot = Bot(token=TOKEN)
    print("Sending daily poll...")
    
    await bot.send_poll(
        chat_id=CHAT_ID,
        question="How much time did you study?",
        options=[
            "11- (Bad baby 😕)",
            "11-12 (not bad 😴)",
            "12-13 (Good Girl 🙂‍↔️)",
            "13+ (Shoiii 😍)"
        ],
        is_anonymous=False,
        # This line ensures only one option can be picked
        allows_multiple_answers=False 
    )

if __name__ == "__main__":
    asyncio.run(send_poll())
