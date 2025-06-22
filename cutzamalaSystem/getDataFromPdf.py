import pdfplumber
import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo PDF
ruta_pdf = "cutzamalaSystem/files/Junio_2025.pdf"  # asegúrate de que esté en el mismo directorio

# Lista para guardar los datos extraídos
parsed_data = []

# Abrir el PDF y procesar línea por línea
with pdfplumber.open(ruta_pdf) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if not text:
            continue
        lines = text.splitlines()
        for line in lines:
            tokens = line.strip().split()
            # Verifica que la línea tenga al menos 12 elementos y que empiece con un número de día
            if len(tokens) >= 12 and tokens[0].isdigit():
                try:
                    dia = int(tokens[0])
                    vv_mm3 = float(tokens[1])
                    vv_pct = float(tokens[2])
                    vb_mm3 = float(tokens[4])
                    vb_pct = float(tokens[5])
                    eb_mm3 = float(tokens[7])
                    eb_pct = float(tokens[8])
                    total_mm3 = float(tokens[10].replace(",", ""))
                    total_pct = float(tokens[11])

                    parsed_data.append({
                        "dia": dia,
                        "villa_victoria_mm3": vv_mm3,
                        "villa_victoria_pct": vv_pct,
                        "valle_bravo_mm3": vb_mm3,
                        "valle_bravo_pct": vb_pct,
                        "el_bosque_mm3": eb_mm3,
                        "el_bosque_pct": eb_pct,
                        "total_mm3": total_mm3,
                        "total_pct": total_pct,
                    })
                except ValueError:
                    continue  # salta líneas con errores de parseo

# Convertir a DataFrame
df = pd.DataFrame(parsed_data)

# Generar columna de fecha
df["fecha"] = pd.to_datetime("2025-06-01") + pd.to_timedelta(df["dia"] - 1, unit="D")

# Exportar como CSV (opcional)
df.to_csv("almacenamiento_cutzamala_junio2025.csv", index=False)

# === GRÁFICA 1: Almacenamiento absoluto ===
plt.figure(figsize=(10, 5))
plt.plot(df["fecha"], df["villa_victoria_mm3"], label="Villa Victoria")
plt.plot(df["fecha"], df["valle_bravo_mm3"], label="Valle de Bravo")
plt.plot(df["fecha"], df["el_bosque_mm3"], label="El Bosque")
plt.title("Almacenamiento absoluto – Presas del Sistema Cutzamala (junio 2025)")
plt.xlabel("Fecha")
plt.ylabel("Volumen (Mm³)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === GRÁFICA 2: Porcentaje de llenado ===
plt.figure(figsize=(10, 5))
plt.plot(df["fecha"], df["villa_victoria_pct"], label="Villa Victoria")
plt.plot(df["fecha"], df["valle_bravo_pct"], label="Valle de Bravo")
plt.plot(df["fecha"], df["el_bosque_pct"], label="El Bosque")
plt.title("Porcentaje de llenado – Presas del Sistema Cutzamala (junio 2025)")
plt.xlabel("Fecha")
plt.ylabel("Porcentaje (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
