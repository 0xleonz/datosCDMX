// #import "../cutzamalaSystem/datos.typ": *
#import "@preview/codly:1.3.0": *
#import "@preview/codly-languages:0.1.1": *
#show: codly-init.with()
#codly(languages: codly-languages)

= Ejercicio 1. Sistema Cutzamala

Se analizaron los datos históricos de almacenamiento diario (en millones de metros cúbicos, Mm³) de las presas principales del Sistema Cutzamala entre los años 2018 y 2022. Los datos se obtuvieron del Sistema Nacional de Información del Agua (SINA), publicados por la CONAGUA.@sina

== a) Consigue los datos de almacenamiento diario porcentual y absoluto de los años 2020 a 2024 de las 3 presas principales del Sistema Cutzamala: Villa Victoria, Valle de Bravo y El Bosque (incluye los datos en un archivo adjunto en el correo).

Se utilizaron los registros históricos publicados por CONAGUA a través de su FTP institucional (`ftp://sih.conagua.gob.mx`), específicamente para las presas:
- *Villa Victoria* (`VVCMX`)
- *Valle de Bravo* (`VBRMX`)
- *El Bosque* (`EBLSI`)

Sin embargo, durante el desarrollo del ejercicio el servidor no respondía: se intentó acceso mediante `ping`, `telnet` y navegadores sin éxito (respuesta `ECONNRESET`). Pero encontre un data set en Kraggle@dataset disponible aqui #link("https://www.kaggle.com/code/edehoyos/niveles-de-presas-en-mexico")[dataset niveles-de-presas-en-mexico].

Se incluye un script reutilizable para automatizar la descarga cuando el servicio vuelva a estar disponible:

```bash
python3 cutzamalaSystem/getDataFromSIH.py
```

== b) Genera una gráfica del almacenamiento absoluto para cada presa en ese periodo.

El procesamiento de los datos se realizó con Python, y se limitaron al periodo entre *2018 y 2022* para el análisis.

#figure(
image("../cutzamalaSystem/figs/VVCMX_almacenamiento_2018_2022.png", width: 80%),
caption: [Villa Victoria – Almacenamiento diario en Mm³ (2018–2022)],
)

#figure(
image("../cutzamalaSystem/figs/VBRMX_almacenamiento_2018_2022.png", width: 80%),
caption: [Valle de Bravo – Almacenamiento diario en Mm³ (2018–2022)],
)

#figure(
image("../cutzamalaSystem/figs/EBLSI_almacenamiento_2018_2022.png", width: 80%),
caption: [El Bosque – Almacenamiento diario en Mm³ (2018–2022)],
)

```python
# Fragmento del código que genera las gráficas individuales
for codigo, nombre in presas.items():
    plt.plot(df["fecha"], df[codigo], label=nombre)
    plt.savefig(f"{codigo}_almacenamiento_{anio_inicio}_{anio_fin}.png")
```

== c) Genera una gráfica donde muestres el almacenamiento porcentual de las 3 presas en ese periodo (las tres curvas en la misma gráfica).

#figure(
image("../cutzamalaSystem/figs/comparativo_porcentajes_2018_2022.png", width: 80%),
caption: [Comparativo porcentual de llenado (2018–2022)],
)

```python
# Calcular porcentaje de llenado con base en la capacidad
porcentaje = (df[codigo] / capacidades[codigo]) * 100
```

== d) ¿Qué puedes concluir a partir de la última gráfica?

Se observan tendencias similares entre las tres presas, lo que sugiere una operación coordinada del sistema. En general:

- *Valle de Bravo* mantiene los niveles más altos.
- *El Bosque* y *Villa Victoria* presentan mayor variabilidad.
- Se notan caídas sostenidas en periodos secos y recuperaciones parciales en temporadas de lluvia.
- En general se nota una caida sostenida 

Estas fluctuaciones reflejan la dependencia del sistema en periodos de captación y muestran vulnerabilidades ante eventos prolongados de baja precipitación.

#pagebreak()
