from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

from config import BOT_TOKEN, logger
from bot_handlers import start_command, monitora_command, list_products_command

# Crea l'applicazione Flask e il bot
app = Flask(__name__)
application = ApplicationBuilder().token(BOT_TOKEN).build()

# --- Connessione tra Comandi e Funzioni ---
application.add_handler(CommandHandler("start", start_command))
application.add_handler(CommandHandler("monitora", monitora_command))
application.add_handler(CommandHandler("list", list_products_command))

# --- Gestione del Webhook ---
@app.route("/")
def hello():
    return "Ciao, il bot è in ascolto!"

@app.route('/telegram', methods=['POST'])
async def webhook():
    """Endpoint che riceve gli aggiornamenti da Telegram"""
    update = Update.de_json(request.get_json(), application.bot)
    await application.process_update(update)
    return "ok"

if __name__ == '__main__':
    logger.info("Avvio del server Flask...")
    app.run(port=5000, debug=True)