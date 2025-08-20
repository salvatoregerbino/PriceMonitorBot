import logging
from telegram import Update
from telegram.ext import ContextTypes
import requests
from bs4 import BeautifulSoup
import re

# Ottieni il logger configurato in config.py
logger = logging.getLogger(__name__)

def scrape_price(url: str) -> float | None:
    """Estrae il prezzo da un URL di e-commerce generico."""
    logger.info(f"Tentativo di scraping per l'URL: {url}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Lancia un'eccezione per risposte HTTP errate

        soup = BeautifulSoup(response.text, 'html.parser')

        # Pattern comuni per trovare il prezzo. La logica può variare.
        # Cerchiamo elementi con classi o attributi comuni per il prezzo
        price_element = soup.find(
            lambda tag: tag.name in ['span', 'div', 'p', 'b'] and (
                'price' in tag.get('class', []) or
                'amount' in tag.get('class', []) or
                'value' in tag.get('itemprop', '') or
                'current-price' in tag.get('id', '')
            )
        )

        if price_element:
            price_text = price_element.get_text(strip=True)
            # Pulisci il testo per estrarre solo i numeri (gestisci valute, virgole, ecc.)
            price_match = re.search(r'[\d,.]+', price_text)
            if price_match:
                clean_price = price_match.group(0).replace('.', '').replace(',', '.')
                return float(clean_price)

        logger.warning(f"Prezzo non trovato per l'URL: {url}")
        return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Errore durante lo scraping dell'URL {url}: {e}")
        return None
    except Exception as e:
        logger.error(f"Errore imprevisto durante lo scraping: {e}")
        return None


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