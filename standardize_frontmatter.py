import os
import re

key_map = {
    "type": "tipo",
    "sources": "fuentes",
    "confidence": "confianza",
    "last_update": "ultima_actualizacion",
    "date": "fecha"
}

val_map = {
    "entity": "entidad",
    "concept": "concepto",
    "opportunity": "oportunidad",
    "daily_summary": "resumen_diario",
    "high": "alta",
    "medium": "media",
    "low": "baja"
}

def standardize_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return False

    parts = content.split("---")
    if len(parts) < 3:
        return False

    frontmatter_text = parts[1]
    rest = "---".join(parts[2:])

    lines = frontmatter_text.splitlines()
    new_lines = []
    modified = False

    for line in lines:
        if ":" in line:
            # Split into key and value
            k, v = line.split(":", 1)
            k_stripped = k.strip()

            # Map key
            new_k = key_map.get(k_stripped, k_stripped)
            if new_k != k_stripped:
                modified = True

            # Clean and map value if key is tipo or confianza
            v_stripped = v.strip()

            # Handle inline list values or single values
            if new_k in ["tipo", "confianza"]:
                # strip potential quotes
                quote_char = ""
                unquoted_v = v_stripped
                if v_stripped.startswith("'") and v_stripped.endswith("'"):
                    quote_char = "'"
                    unquoted_v = v_stripped[1:-1]
                elif v_stripped.startswith('"') and v_stripped.endswith('"'):
                    quote_char = '"'
                    unquoted_v = v_stripped[1:-1]

                new_v = val_map.get(unquoted_v, unquoted_v)
                if new_v != unquoted_v:
                    modified = True
                    v_stripped = f"{quote_char}{new_v}{quote_char}"

            # Preserve spacing in key
            key_space_match = re.match(r"^(\s*)", k)
            key_space = key_space_match.group(1) if key_space_match else ""

            new_line = f"{key_space}{new_k}: {v_stripped}"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if modified:
        new_frontmatter = "\n".join(new_lines)
        # Ensure it has leading/trailing newlines matching or correct structure
        if not new_frontmatter.endswith("\n") and frontmatter_text.endswith("\n"):
            new_frontmatter += "\n"
        if not new_frontmatter.startswith("\n") and frontmatter_text.startswith("\n"):
            new_frontmatter = "\n" + new_frontmatter

        new_content = "---" + new_frontmatter + "---" + rest
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

def run_standardization():
    count = 0
    for root, dirs, files in os.walk("wiki"):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                if standardize_file(filepath):
                    print(f"Standardized: {filepath}")
                    count += 1
    print(f"Finished standardizing frontmatter in {count} files.")

if __name__ == "__main__":
    run_standardization()
