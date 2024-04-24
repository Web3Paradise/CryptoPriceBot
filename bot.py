from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to CryptoBot! Type /price <crypto_symbol> to get crypto price.")

def get_crypto_price(update: Update, context: CallbackContext) -> None:
    try:
        crypto_symbol = context.args[0].upper()
        # Fetch crypto data from CoinGecko API
        url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={crypto_symbol}"
        response = requests.get(url)
        data = response.json()
        current_price = data[0]['current_price']
        update.message.reply_text(f"Price of {crypto_symbol}: ${current_price:.2f}")
    except IndexError:
        update.message.reply_text("Please provide a valid crypto symbol. Example: /price BTC")

def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("price", get_crypto_price))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
