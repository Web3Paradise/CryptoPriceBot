from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    """Handler for the /start command."""
    update.message.reply_text("Welcome to CryptoBot! Type /price <crypto_symbol> to get crypto price.")

def get_crypto_price(update: Update, context: CallbackContext) -> None:
    """Handler for the /price command."""
    try:
        crypto_symbol = context.args[0].upper()
        # Fetch crypto data from CoinGecko API
        url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={crypto_symbol}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful status codes
        data = response.json()
        current_price = data[0].get('current_price')  # Use .get() to handle missing keys
        if current_price is not None:
            update.message.reply_text(f"Price of {crypto_symbol}: ${current_price:.2f}")
        else:
            update.message.reply_text(f"Price data not available for {crypto_symbol}")
    except (IndexError, requests.RequestException, ValueError, KeyError):
        update.message.reply_text("Failed to fetch price. Please try again later.")

def main() -> None:
    """Main function to start the bot."""
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("price", get_crypto_price))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
