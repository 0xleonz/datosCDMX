import re
import argparse
from collections import Counter
import matplotlib.pyplot as plt

# Configurar argumentos CLI
parser = argparse.ArgumentParser(
    description="Analiza CURPs desde un archivo y genera estadísticas. Usa --typst para exportar datos para Typst."
)
parser.add_argument(
    "--typst",
    action="store_true",
    help="Genera archivo datos.typ para ser importado en un reporte Typst.",
)
args = parser.parse_args()

# Leer archivo usando context manager para asegurar cierre automático del recurso
with open("curp/curp_sucio.txt", encoding="utf-8") as f:
    curps = [line.strip() for line in f if line.strip()]

# Expresión regular de CURP válida según la RENAPO (Registro Nacional de Población)
# Fuente: https://www.gob.mx/curp
regex = re.compile(
    r"^[A-Z]{4}"                                 # 4 letras: iniciales del nombre y apellidos
    r"\d{2}(0[1-9]|1[0-2])([0-2][0-9]|3[01])"     # Fecha de nacimiento: AAMMDD
    r"[HM]"                                       # Sexo: H (hombre) o M (mujer)
    r"(AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|"   # Entidad federativa (abreviatura oficial)
    r"JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|"
    r"TC|TS|TL|VZ|YN|ZS)"
    r"[B-DF-HJ-NP-TV-Z]{3}"                      # Consonantes internas del nombre
    r"[A-Z\d]\d$"                                # Homoclave: 1 letra o número y 1 dígito
)

# Filtrar CURPs válidas
curps_validas = [curp for curp in curps if regex.match(curp)]

# Extraer entidades (posición 11 a 13 de la CURP)
entidades = [curp[11:13] for curp in curps_validas]
conteo_entidades = Counter(entidades)

# Extraer fechas de nacimiento (posición 4 a 10) y contar por mes y día (MM-DD)
fechas = [curp[6:10] for curp in curps_validas]  # MMDD
cumples = Counter(f"{f[:2]}-{f[2:]}" for f in fechas)
numFechas = 10
top_fechas = cumples.most_common(numFechas)

# --- Graficar cantidad de CURPs válidas por entidad federativa
plt.figure(figsize=(12, 6))
plt.bar(conteo_entidades.keys(), conteo_entidades.values(), color="steelblue")
plt.title("CURPs válidas por entidad federativa")
plt.xlabel("Entidad federativa")
plt.ylabel("Número de personas")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Guardar figuras tanto para el reporte como para el readme
plt.savefig("curp/fig_entidades.png")
plt.savefig("assets/fig_entidades.png")
plt.close()

# --- Mostrar fechas de cumpleaños más comunes
print(f"{numFechas} fechas de cumpleaños más comunes:")
for fecha, count in top_fechas:
    print(f"{fecha} - {count} personas")

print("\nResumen:")
print(f"Total de CURPs válidas: {len(curps_validas)}")
print(f"Total de CURPs inválidas: {len(curps) - len(curps_validas)}")

# Para el reporteo automatico con typst
# Guardar archivo con datos para Typst
if args.typst:
    with open("curp/datos.typ", "w", encoding="utf-8") as f:
        f.write(f"// Variables generadas automáticamente\n")
        f.write(f"#let curps_validas = {len(curps_validas)}\n")
        f.write(f"#let curps_invalidas = {len(curps) - len(curps_validas)}\n")

        for i, (fecha, count) in enumerate(top_fechas, 1):
            f.write(f"#let top_fecha_{i} = \"{fecha} — {count} personas\"\n")
import re
import argparse
from collections import Counter
import matplotlib.pyplot as plt

# Configurar argumentos CLI
parser = argparse.ArgumentParser(
    description="Analiza CURPs desde un archivo y genera estadísticas. Usa --typst para exportar datos para Typst."
)
parser.add_argument(
    "--typst",
    action="store_true",
    help="Genera archivo datos.typ para ser importado en un reporte Typst.",
)
args = parser.parse_args()

# Leer archivo usando context manager para asegurar cierre automático del recurso
with open("curp/curp_sucio.txt", encoding="utf-8") as f:
    curps = [line.strip() for line in f if line.strip()]

# Expresión regular de CURP válida según la RENAPO (Registro Nacional de Población)
# Fuente: https://www.gob.mx/curp
regex = re.compile(
    r"^[A-Z]{4}"                                 # 4 letras: iniciales del nombre y apellidos
    r"\d{2}(0[1-9]|1[0-2])([0-2][0-9]|3[01])"     # Fecha de nacimiento: AAMMDD
    r"[HM]"                                       # Sexo: H (hombre) o M (mujer)
    r"(AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|"   # Entidad federativa (abreviatura oficial)
    r"JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|"
    r"TC|TS|TL|VZ|YN|ZS)"
    r"[B-DF-HJ-NP-TV-Z]{3}"                      # Consonantes internas del nombre
    r"[A-Z\d]\d$"                                # Homoclave: 1 letra o número y 1 dígito
)

# Filtrar CURPs válidas
curps_validas = [curp for curp in curps if regex.match(curp)]

# Extraer entidades (posición 11 a 13 de la CURP)
entidades = [curp[11:13] for curp in curps_validas]
conteo_entidades = Counter(entidades)

# Extraer fechas de nacimiento (posición 4 a 10) y contar por mes y día (MM-DD)
fechas = [curp[6:10] for curp in curps_validas]  # MMDD
cumples = Counter(f"{f[:2]}-{f[2:]}" for f in fechas)
numFechas = 3
top_fechas = cumples.most_common(numFechas)

# --- Graficar cantidad de CURPs válidas por entidad federativa
plt.figure(figsize=(12, 6))
plt.bar(conteo_entidades.keys(), conteo_entidades.values(), color="steelblue")
plt.title("CURPs válidas por entidad federativa")
plt.xlabel("Entidad federativa")
plt.ylabel("Número de personas")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Guardar figuras tanto para el reporte como para el readme
plt.savefig("curp/fig_entidades.png")
plt.savefig("assets/fig_entidades.png")
plt.close()

# --- Mostrar fechas de cumpleaños más comunes
print(f"{numFechas} fechas de cumpleaños más comunes:")
for fecha, count in top_fechas:
    print(f"{fecha} - {count} personas")

print("\nResumen:")
print(f"Total de CURPs válidas: {len(curps_validas)}")
print(f"Total de CURPs inválidas: {len(curps) - len(curps_validas)}")

# Para el reporteo automatico con typst
# Guardar archivo con datos para Typst
if args.typst:
    with open("curp/datos.typ", "w", encoding="utf-8") as f:
        f.write(f"// Variables generadas automáticamente\n")
        f.write(f"#let curps_validas = {len(curps_validas)}\n")
        f.write(f"#let curps_invalidas = {len(curps) - len(curps_validas)}\n")

        for i, (fecha, count) in enumerate(top_fechas, 1):
            f.write(f"#let top_fecha_{i} = \"{fecha} — {count} personas\"\n")

