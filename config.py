import os
from dotenv import load_dotenv, find_dotenv
import logging

# Carica le variabili d'ambiente dal file .env
load_dotenv(find_dotenv())

# --- Configurazione Generale ---
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Se il token ha virgolette, le rimuove
if BOT_TOKEN and BOT_TOKEN.startswith('"') and BOT_TOKEN.endswith('"'):
    BOT_TOKEN = BOT_TOKEN[1:-1]

# --- Configurazione del Logger ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# Crea un logger specifico per l'applicazione
logger = logging.getLogger(__name__)

# Per un check iniziale
logger.info("Configurazione caricata. Token del bot letto correttamente.")