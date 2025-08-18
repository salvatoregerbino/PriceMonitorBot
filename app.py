import os
from dotenv import load_dotenv
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bs4 import BeautifulSoup
import requests
import json
import logging

load_dotenv()

# Configura il logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- Configurazione del Bot e del Server ---
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Crea l'applicazione Flask e il bot
application = ApplicationBuilder().token(BOT_TOKEN).build()

# Funzione per lo scraping (da implementare nella Fase 2)
def scrape_price(url):
    """Simula lo scraping del prezzo da un URL"""
    logging.info(f"Simulando lo scraping per {url}")
    # Qui inseriremo la logica di web scraping nella fase successiva
    return 99.99 # Valore di esempio

# --- Funzioni del Bot ---

async def start(update: Update, context) -> None:
    """Funzione che gestisce il comando /start"""
    await update.message.reply_text(
        "Ciao! Sono il tuo bot per monitorare i prezzi. "
        "Usa /monitora <URL> <prezzo> per iniziare a tracciare un prodotto."
    )

async def monitora(update: Update, context) -> None:
    """Gestisce il comando /monitora"""
    if len(context.args) != 2:
        await update.message.reply_text("Formato errato. Usa /monitora <URL> <prezzo>.")
        return

    url = context.args[0]
    try:
        prezzo_desiderato = float(context.args[1])
    except ValueError:
        await update.message.reply_text("Il prezzo deve essere un numero.")
        return

    # Qui implementeremo la logica per salvare i dati su GitHub (Fase 2)
    # Per ora, simuliamo il salvataggio
    logging.info(f"Richiesta di monitoraggio per {url} al prezzo di {prezzo_desiderato}")
    await update.message.reply_text(f"Ho iniziato a monitorare {url} al prezzo di {prezzo_desiderato}€.")

async def list_products(update: Update, context) -> None:
    """Gestisce il comando /list per elencare i prodotti monitorati"""
    # Qui implementeremo la logica per leggere i dati da GitHub (Fase 2)
    # Per ora, restituiamo un messaggio di esempio
    await update.message.reply_text("Ecco i prodotti che stai monitorando:")
    # Aggiungeremo qui l'elenco dei prodotti nella fase successiva

# --- Connessione tra Comandi e Funzioni ---
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("monitora", monitora))
application.add_handler(CommandHandler("list", list_products))

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