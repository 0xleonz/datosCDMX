import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
from datetime import datetime

# argparser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inicio", type=int, help="Año inicial (opcional)")
parser.add_argument("-f", "--fin", type=int, help="Año final (opcional)")
parser.add_argument("-s", "--show", action="store_true", help="Mostrar gráficas al correr")
args = parser.parse_args()

# leer csv
archivo = "cutzamalaSystem/files/almacenamiento.csv"
df = pd.read_csv(archivo)
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

# columnas clave
presas = {
    "VVCMX": "Villa Victoria",
    "VBRMX": "Valle de Bravo",
    "EBLSI": "El Bosque"
}

# definir rango de años
min_anio = df["fecha"].dt.year.min()
max_anio = df["fecha"].dt.year.max()

if args.inicio and args.fin and min_anio <= args.inicio <= args.fin <= max_anio:
    anio_inicio = args.inicio
    anio_fin = args.fin
else:
    anio_fin = max_anio
    anio_inicio = anio_fin - 4

# filtrar por rango de años
df = df[df["fecha"].dt.year.between(anio_inicio, anio_fin)]

# asegurar carpetas
os.makedirs("cutzamalaSystem/figs", exist_ok=True)
os.makedirs("assets", exist_ok=True)

# graficar una por una
for codigo, nombre in presas.items():
    plt.figure(figsize=(10, 5))
    plt.plot(df["fecha"], df[codigo], label=nombre)
    plt.title(f"Almacenamiento absoluto – {nombre} ({anio_inicio}-{anio_fin})")
    plt.xlabel("Fecha")
    plt.ylabel("Volumen (Mm³)")
    plt.grid(True)
    plt.tight_layout()
    
    fname = f"{codigo}_almacenamiento_{anio_inicio}_{anio_fin}.png"
    plt.savefig(f"cutzamalaSystem/figs/{fname}")
    plt.savefig(f"assets/{fname}")
    
    if args.show:
        plt.show()
    plt.close()

# gráfica comparativa (porcentajes relativos)
capacidades = {
    "VVCMX": 185.731,
    "VBRMX": 394.390,
    "EBLSI": 202.400
}

plt.figure(figsize=(10, 5))
for codigo, nombre in presas.items():
    porcentaje = (df[codigo] / capacidades[codigo]) * 100
    plt.plot(df["fecha"], porcentaje, label=nombre)

plt.title(f"Porcentaje de llenado – Presas Cutzamala ({anio_inicio}-{anio_fin})")
plt.xlabel("Fecha")
plt.ylabel("Porcentaje (%)")
plt.grid(True)
plt.legend()
plt.tight_layout()

comparativa_nombre = f"comparativo_porcentajes_{anio_inicio}_{anio_fin}.png"
plt.savefig(f"cutzamalaSystem/figs/{comparativa_nombre}")
plt.savefig(f"assets/{comparativa_nombre}")

if args.show:
    plt.show()
plt.close()
