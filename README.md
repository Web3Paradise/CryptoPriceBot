# CryptoPriceBot
Telegram bot to display crypto price
# Building a Crypto Telegram Bot with CoinGecko Integration
Prerequisites:
Ensure you have Python 3.7 or higher installed on your system.
Create a Telegram Bot:
Start by creating a bot on Telegram using the BotFather. Follow these steps:
1) Open Telegram and search for @BotFather.
Type /newbot and follow the instructions.
Save the API token provided by BotFather.  
2) Install the necessary Python packages:
   pip install python-telegram-bot requests
   3) We’ll use the CoinGecko API to fetch real-time crypto data. Specifically, we’ll make a GET request to the /coins/markets endpoint to get data like current price, market cap, volume, and price change percentage.
   4) Run the Python script. Your bot should now respond to /start and /price <crypto_symbol> commands.
5) Remember to replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token and the Coingecko api with your API
