import os
from datetime import datetime
from scraper import scrape_feeds, scrape_boletin_oficial, save_raw

# Directorios de la Wiki
DAILY_DIR = "wiki/daily"
ENTITIES_DIR = "wiki/entities"
CONCEPTS_DIR = "wiki/concepts"
OPPORTUNITIES_DIR = "wiki/opportunities"

def create_daily_note(data):
    os.makedirs(DAILY_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{DAILY_DIR}/{today}.md"

    content = f"---\ndate: {today}\ntype: daily_summary\n---\n\n# Resumen Diario de Inteligencia AgTech - {today}\n\n"

    # Agrupar por fuente
    grouped_data = {}
    for item in data:
        source = item["source"]
        if source not in grouped_data:
            grouped_data[source] = []
        grouped_data[source].append(item)

    for source, items in grouped_data.items():
        content += f"## Fuente: {source}\n"
        for entry in items:
            content += f"- **[{entry['title']}]({entry['link']})**\n"
            # Extraer posibles backlinks basados en palabras clave
            backlinks = []
            if "841/2025" in entry["title"] or "841/2025" in entry["content"]:
                backlinks.append("[[Resolucion SENASA 841-2025]]")
            if any(kw in (entry["title"] + entry["content"]).lower() for kw in ["tambo", "leche", "estabulado", "robotizado", "robótico"]):
                backlinks.append("[[Zonas Nucleo Adaptacion Tecnologica]]")
            if any(kw in (entry["title"] + entry["content"]).lower() for kw in ["sigsa", "rfid", "fallas", "problemas", "bienestar animal"]):
                backlinks.append("[[Pain Points de Trazabilidad]]")
            if "hereford" in (entry["title"] + entry["content"]).lower():
                backlinks.append("[[Asociacion Hereford Argentina]]")
            if any(kw in (entry["title"] + entry["content"]).lower() for kw in ["frigorífico", "exportador", "abc"]):
                backlinks.append("[[Consorcio de Frigorificos ABC]]")

            if backlinks:
                content += f"  - Temas Relacionados: {', '.join(set(backlinks))}\n"
        content += "\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename

def run_automation():
    print("Iniciando automatización diaria...")
    # 1. Scrapping
    data = scrape_feeds()
    data.extend(scrape_boletin_oficial())

    # 2. Guardar Raw
    raw_path = save_raw(data)
    print(f"Datos raw guardados en: {raw_path}")

    # 3. Generar Nota Diaria
    daily_path = create_daily_note(data)
    print(f"Nota diaria generada en: {daily_path}")

if __name__ == "__main__":
    run_automation()
