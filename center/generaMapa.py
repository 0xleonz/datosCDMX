#!/usr/bin/env python3

import os
import argparse
import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
import requests
import zipfile

SHAPE_URL = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
SHAPE_DIR = "data/ne_110m_admin_0_countries"
SHAPE_PATH = f"{SHAPE_DIR}/ne_110m_admin_0_countries.shp"

LUGARES = {
    "Aguascalientes": (-102.29, 21.88),
    "Cañitas de Felipe Pescador": (-102.68, 23.58),
    "Tequisquiapan": (-99.89, 20.52),
}

def descargar_shapefile():
    print("Descargando shapefile de Natural Earth...")
    os.makedirs(SHAPE_DIR, exist_ok=True)
    zip_path = f"{SHAPE_DIR}.zip"

    # Descargar el archivo zip
    with requests.get(SHAPE_URL, stream=True) as r:
        r.raise_for_status()
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    # Extraer
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(SHAPE_DIR)

    os.remove(zip_path)
    print("Shapefile descargado y extraído.")

def generar_mapa(mostrar=False):
    # Leer shapefile de países
    world = gpd.read_file(SHAPE_PATH)
    mexico = world[world["ADMIN"] == "Mexico"]

    # Crear puntos
    puntos = gpd.GeoDataFrame(
        geometry=[Point(lon, lat) for lon, lat in LUGARES.values()],
        index=LUGARES.keys(),
        crs="EPSG:4326"
    )

    # Graficar
    fig, ax = plt.subplots(figsize=(8, 10))
    mexico.plot(ax=ax, color='white', edgecolor='black')
    puntos.plot(ax=ax, color='red', markersize=50)

    for nombre, (lon, lat) in LUGARES.items():
        ax.text(lon + 0.3, lat, nombre, fontsize=9)

    ax.set_xlim(-107, -86)
    ax.set_ylim(14, 33)
    ax.set_title("Ubicaciones en el centro de México")
    ax.axis("off")

    salida = "assets/centro-mexico-mapa.png"
    plt.savefig(salida, dpi=300, bbox_inches="tight")
    print(f"Mapa guardado como {salida}")

    if mostrar:
        plt.show()
    else:
        plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera un mapa de México con ubicaciones marcadas.")
    parser.add_argument("--first-run", action="store_true", help="Descargar shapefile necesario")
    parser.add_argument("-s", "--show", action="store_true", help="Mostrar mapa tras generarlo")
    args = parser.parse_args()

    if args.first_run:
        descargar_shapefile()

    if not os.path.exists(SHAPE_PATH):
        print("Shapefile no encontrado. Ejecuta con --first-run primero.")
        exit(1)

    generar_mapa(mostrar=args.show)

