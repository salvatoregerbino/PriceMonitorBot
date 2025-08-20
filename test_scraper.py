from bot_handlers import scrape_price

# Esempio di URL da testare.
# Sostituisci questo URL con un URL di un prodotto di un e-commerce reale.
# Assicurati che il sito non abbia protezioni avanzate contro lo scraping.
test_url = "https://www.bricofer.it/vernici/9216610/"

prezzo = scrape_price(test_url)

if prezzo:
    print(f"Il prezzo estratto è: {prezzo}")
else:
    print("Non è stato possibile estrarre il prezzo.")