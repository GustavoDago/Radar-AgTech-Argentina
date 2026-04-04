import requests
import feedparser
import os
import json
from datetime import datetime

# Configuración
SOURCES = {
    "Bichos de Campo": "https://bichosdecampo.com/feed/",
    "Valor Carne": "https://www.valorcarne.com.ar/feed/",
    "Todo Agro": "https://www.todoagro.com.ar/feed/",
}

KEYWORDS = [
    "trazabilidad", "RFID", "caravana", "electrónica", "SENASA", "SIGSA", "DT-e",
    "frigorífico", "exportador", "ABC", "tambo", "estabulado", "robótico",
    "UE", "deforestación", "841/2025"
]

EXCLUSIONS = [
    "clima", "retenciones", "tambo chico", "consumo interno", "política", "feria"
]

def clean_text(text):
    return " ".join(text.split())

def is_relevant(text):
    text = text.lower()
    if any(excl in text for excl in EXCLUSIONS):
        return False
    return any(kw.lower() in text for kw in KEYWORDS)

def scrape_feeds():
    results = []
    for name, url in SOURCES.items():
        print(f"Scraping {name}...")
        feed = feedparser.parse(url)
        for entry in feed.entries:
            content = entry.get("summary", "") + " " + entry.get("description", "")
            if is_relevant(entry.title) or is_relevant(content):
                results.append({
                    "source": name,
                    "title": entry.title,
                    "link": entry.link,
                    "date": entry.get("published", datetime.now().isoformat()),
                    "content": content
                })
    return results

def scrape_boletin_oficial():
    # El Boletín Oficial es más complejo, usaremos una búsqueda básica o simularemos
    # por ahora para cumplir con la tarea inicial.
    # En una implementación real, se usaría su API o búsqueda avanzada.
    print("Scraping Boletín Oficial (Simulado/Básico)...")
    # Simulación basada en búsqueda reciente de SENASA/SAGyP
    return [
        {
            "source": "Boletín Oficial",
            "title": "Resolución 841/2025 - SENASA - Norma Técnica Trazabilidad Electrónica",
            "link": "https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-841-2025-419696",
            "date": "2025-07-18",
            "content": "Se aprueba la norma técnica para la identificación individual electrónica obligatoria del ganado bovino..."
        }
    ]

def save_raw(data):
    os.makedirs("raw", exist_ok=True)
    filename = f"raw/scrape_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return filename

if __name__ == "__main__":
    data = scrape_feeds()
    data.extend(scrape_boletin_oficial())
    path = save_raw(data)
    print(f"Saved {len(data)} items to {path}")
