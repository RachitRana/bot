import asyncio
from telegram import Bot
import subprocess
import time

bot = Bot(token='6704929353:AAFl1FiJyq3aQ39JFP_nFRRtrcCytdYR5IM')
chat_id = '1299724072'

async def send_to_telegram(content):
    await bot.send_message(chat_id=chat_id, text=content)

if __name__ == "__main__":
    while True:
        # Your content to be sent (in this case, "hello")
        content = "hello"
       
        loop = asyncio.get_event_loop()
        loop.run_until_complete(send_to_telegram(content))
        loop.close()
       
        # Wait for 15 seconds before sending the next update
        time.sleep(15)
