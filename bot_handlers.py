import logging
from telegram import Update
from telegram.ext import ContextTypes

# Ottieni il logger configurato in config.py
logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Funzione che gestisce il comando /start"""
    logger.info(f"Comando /start ricevuto da {update.effective_user.name}")
    await update.message.reply_text(
        "Ciao! Sono il tuo bot per monitorare i prezzi. "
        "Usa /monitora <URL> <prezzo> per iniziare a tracciare un prodotto."
    )

async def monitora_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Gestisce il comando /monitora"""
    logger.info(f"Comando /monitora ricevuto da {update.effective_user.name}")
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
    logger.info(f"Richiesta di monitoraggio per {url} al prezzo di {prezzo_desiderato}")
    await update.message.reply_text(f"Ho iniziato a monitorare {url} al prezzo di {prezzo_desiderato}€.")

async def list_products_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Gestisce il comando /list per elencare i prodotti monitorati"""
    logger.info(f"Comando /list ricevuto da {update.effective_user.name}")
    # Qui implementeremo la logica per leggere i dati da GitHub (Fase 2)
    await update.message.reply_text("Ecco i prodotti che stai monitorando:")