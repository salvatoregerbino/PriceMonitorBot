import os
from dotenv import load_dotenv
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


load_dotenv()
# --- Configurazione del Bot e del Server ---
# Ottieni il token API del tuo bot da una variabile d'ambiente
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Crea l'applicazione Flask e il bot
app = Flask(__name__)
application = ApplicationBuilder().token(BOT_TOKEN).build()

# --- Funzioni del Bot ---
async def start(update: Update, context) -> None:
    """Funzione che gestisce il comando /start"""
    await update.message.reply_text(f'Ciao! Sono il tuo bot per monitorare i prezzi. Invia un URL e un prezzo per iniziare.')

# Aggiungi un handler per il comando /start
application.add_handler(CommandHandler("start", start))

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
    # Quando esegui il file, il server Flask si avvia
    # Lo avviamo in modalità debug per comodità
    app.run(port=5000, debug=True)