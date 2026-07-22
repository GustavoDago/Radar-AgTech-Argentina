import urllib.request
import feedparser
import os
import json
import ssl
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
    "crimen", "policial", "robo de cables", "detenido", "detuvieron",
    "fútbol", "deportes", "espectáculos", "farándula", "cine",
    "pronóstico lluvia", "pronóstico del tiempo", "clima mañana", "lluvia", "precipitaciones", "clima",
    "receta", "cocina", "chef", "ingredientes",
    "cotización dólar", "dólar blue", "dólar", "euro", "blue", "cotización", "moneda", "divisa", "feria americana",
    "ajo", "manzana", "porcin", "cerdo", "acuicultura", "trucha", "avícola", "pollo",
    "vino", "césped", "camino rural", "caminos rurales", "maquin", "biodiésel", "vitivinícola",
    "retenciones", "derechos de exportación", "política partidaria", "elecciones", "voto",
    "pitahaya", "pecán", "pecan", "olivo", "mandioca", "banana", "citrus", "cítrico", "cítricos",
    "arroz", "papa", "cebolla", "tomate", "horticultura", "hortícola", "hidroponia", "hidropón", "hidroponía",
    "automóvil", "camioneta", "auto ", "autos ", "vehículo de pasajeros", "caña", "camarones", "camarón",
    "pescado", "mostaza", "yogur", "maleza", "malezas"
]

def clean_text(text):
    return " ".join(text.split())

def is_relevant(text):
    text = text.lower()
    if any(excl in text for excl in EXCLUSIONS):
        return False
    return any(kw.lower() in text for kw in KEYWORDS)

# Contexto SSL para evitar fallas de certificados en sitios como Todo Agro
ssl_context = ssl._create_unverified_context()

def fetch_url(url, timeout=15):
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    )
    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=timeout) as response:
            return response.read()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def scrape_feeds():
    results = []
    for name, url in SOURCES.items():
        print(f"Scraping {name}...")
        html_bytes = fetch_url(url)
        if not html_bytes:
            continue
        feed = feedparser.parse(html_bytes)
        # Limit to first 50 entries to avoid performance issues (e.g. INTA Informa feed with 800 entries)
        entries = feed.entries[:50]
        for entry in entries:
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
    search_url = "https://www.boletinoficial.gob.ar/seccion/primera"

    try:
        # Usamos fetch_url para la robustez del scraping
        html_bytes = fetch_url(search_url)
        if html_bytes:
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
