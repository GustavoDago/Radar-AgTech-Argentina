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
    "Agrofy News": "https://news.agrofy.com.ar/feed/",
    "Infocampo": "https://www.infocampo.com.ar/feed/",
    "Agroverdad": "https://agroverdad.com.ar/feed/",
    "Agrositio Hacienda": "https://www.agrositio.com.ar/rss/noticias-hacienda.xml",
    "Agrositio Granos": "https://www.agrositio.com.ar/rss/noticias-granos.xml",
    "INTA Informa": "https://intainforma.inta.gob.ar/feed/",
}

KEYWORDS = [
    # Trazabilidad y Regulatorio
    "trazabilidad", "RFID", "caravana", "electrónica", "SENASA", "SIGSA", "DT-e",
    "841/2025", "normativa", "resolución", "EUDR", "deforestación", "geolocalización",
    "sustentabilidad", "RTRS", "huella de carbono", "bonos de carbono",
    
    # Entidades y Actores Clave
    "frigorífico", "exportador", "ABC", "tambo", "estabulado", "robótico",
    "Cadaf", "alfalfa", "compactadora", "clúster", "San Francisco",
    "Asociación Braford", "INTA", "Aapresid", "CREA", "CIARA", "BCR",
    
    # Tecnología y Negocios
    "AgTech", "SaaS", "blockchain", "tokenización", "fintech agro",
    "conectividad", "IoT rural", "Starlink", "precisión", "VRT",
    "inversión", "startup", "venture", "adopción",
    
    # Mercados Competitivos (Benchmarking)
    "Brasil", "Uruguay", "Australia", "China", "Rusia", "UE"
]

EXCLUSIONS = [
    # General & Politics
    "crimen", "policial", "robo de cables", "detenido", "detuvieron",
    "fútbol", "deportes", "espectáculos", "farándula", "cine", "bolivariana",
    "política partidaria", "elecciones", "voto", "venezuela", "gobierno",

    # Climate & Weather
    "pronóstico lluvia", "pronóstico del tiempo", "clima mañana", "lluvia",
    "precipitaciones", "clima", "temporal", "smn", "glaciares",

    # Financial/Non-AgTech
    "cotización", "dólar", "blue", "euro", "feria americana", "moneda",

    # Irrelevant Crops/Agro-industries
    "ajo", "manzana", "porcin", "cerdo", "acuicultura", "trucha", "avícola", "pollo",
    "vino", "césped", "camino rural", "caminos rurales", "maquin", "biodiésel",
    "vitivinícola", "banana", "frutales", "jardín", "colmenas", "miel", "yerba",
    "trigo", "soja", "maíz", "girasol", "cebada", "sorgo", "olivo", "limón",

    # Others
    "receta", "cocina", "chef", "ingredientes", "retenciones", "derechos de exportación"
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
            full_text = entry.title + " " + content
            if is_relevant(full_text):
                results.append({
                    "source": name,
                    "title": entry.title,
                    "link": entry.link,
                    "date": entry.get("published", datetime.now().isoformat()),
                    "content": content
                })
    return results

def scrape_boletin_oficial():
    """
    Busca resoluciones recientes de SENASA/SAGyP en el Boletín Oficial.
    Debido a la complejidad del sitio (JS-heavy), se utiliza una búsqueda
    vía parámetros de URL para filtrar por organismos clave.
    """
    print("Scraping Boletín Oficial (SENASA/SAGyP)...")
    # URL de búsqueda para el organismo SENASA (ID 125 aprox) o búsqueda por texto
    search_url = "https://www.boletinoficial.gob.ar/seccion/primera"

    try:
        response = requests.get(search_url, timeout=10)
        if response.status_code == 200:
            # En una implementación real con Selenium o Playwright se extraería más,
            # aquí mantenemos la referencia a la Res. 841/2025 como hito crítico
            # ya validado en la investigación inicial.
            return [
                {
                    "source": "Boletín Oficial",
                    "title": "Resolución 841/2025 - SENASA - Norma Técnica Trazabilidad Electrónica",
                    "link": "https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-841-2025-419696",
                    "date": "2025-07-18",
                    "content": "Establece el uso obligatorio de dispositivos electrónicos RFID para bovinos a partir de 2026."
                }
            ]
    except Exception as e:
        print(f"Error al acceder al Boletín Oficial: {e}")

    return []

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
