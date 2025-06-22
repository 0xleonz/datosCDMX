#import "../curp/datos.typ": *
#import "@preview/codly:1.3.0": *
#import "@preview/codly-languages:0.1.1": *

#show: codly-init.with()

#codly(languages: codly-languages)

= Ejercicio 2. Presupuesto para parques

Se tiene un fondo destinado al presupuesto para parques de la Ciudad de México (una suma fija de capital).

== a) ¿Qué factores tomarías en cuenta para la distribución porcentual de este fondo entre las 16 alcaldías?

Algunos de los factores a considerar para la distribución del presupuesto entre las alcaldías podrían incluir:
- Superficie de áreas verdes existentes y su estado de conservación.
- Necesidades identificadas en planes de desarrollo urbano o solicitudes ciudadanas.
- Índices de marginación o rezago social.
- Población total de cada alcaldía.
- Densidad poblacional y demanda de espacios recreativos.
- Número y tamaño de parques actuales.
- Disponibilidad de terreno público para nuevos proyectos.

== b) Determina el porcentaje que asignarías a cada alcaldía.
Para esto vamos a considerar solamente que la asignación se basa en la población de cada alcaldía, y los metros de área verde por habitante. Un analisis mas detallado incluiría los factores mencionados en a) y alguna funcion de valuacion. Usando datos disponibles. Y considerando lo siguiente.// citas
```python
import pandas as pd

# Datos INEGI 2020 (población) y Sedema 2017 (área verde m²/hab)
datos = {
    "Alcaldía": ["Álvaro Obregón", "Azcapotzalco", "Benito Juárez", "Coyoacán",
                 "Cuajimalpa", "Cuauhtémoc", "Gustavo A. Madero", "Iztacalco",
                 "Iztapalapa", "Magdalena Contreras", "Miguel Hidalgo",
                 "Milpa Alta", "Tláhuac", "Tlalpan", "Venustiano Carranza", "Xochimilco"],
    "Población": [759137, 432205, 434153, 614447, 217686, 545884, 1173351,
                  404695, 1835486, 247622, 414470, 152685, 392313, 699928,
                  443704, 442178],
    "Área_verde_m2hab": [6.6, 9.9, 2.2, 15.0, 10.3, 3.6, 6.7, 5.0, 5.4, 5.5,
                          15.4, 2.2, 8.4, 9.6, 13.6, 5.0]
}
df = pd.DataFrame(datos)
# Estándar recomendado por la OMS
estandar = 9.0
# Factor de ajuste
df["factor"] = ((estandar - df["Área_verde_m2hab"]) / estandar).clip(lower=-0.9)
df["pct_pob"] = df["Población"] / df["Población"].sum()
df["pct_ajustada"] = (df["pct_pob"] * (1 + df["factor"]))
# Normalizar para que sume 100%
df["pct_final"] = df["pct_ajustada"] / df["pct_ajustada"].sum() * 100
print(df[["Alcaldía","pct_pob","Área_verde_m2hab","factor","pct_final"]].round(2))

```

El presupuesto que asignaria a cada delegacion es:

#table(
  columns: (1fr, auto, auto, auto, auto),
  inset: 8pt,
  align: horizon,
  table.header(
    [*Alcaldía*], [*% Población*], [*m²/hab*], [*Factor*], [*% Ajustado*],
  ),
  [Álvaro Obregón], [0.08], [6.6], [0.27], [9.02],
  [Azcapotzalco], [0.05], [9.9], [-0.10], [3.65],
  [Benito Juárez], [0.05], [2.2], [0.76], [7.15],
  [Coyoacán], [0.07], [15.0], [-0.67], [1.92],
  [Cuajimalpa], [0.02], [10.3], [-0.14], [1.75],
  [Cuauhtémoc], [0.06], [3.6], [0.60], [8.19],
  [Gustavo A. Madero], [0.13], [6.7], [0.26], [13.82],
  [Iztacalco], [0.04], [5.0], [0.44], [5.48],
  [Iztapalapa], [0.20], [5.4], [0.40], [24.10],
  [Magdalena Contreras], [0.03], [5.5], [0.39], [3.23],
  [Miguel Hidalgo], [0.05], [15.4], [-0.71], [1.12],
  [Milpa Alta], [0.02], [2.2], [0.76], [2.51],
  [Tláhuac], [0.04], [8.4], [0.07], [3.92],
  [Tlalpan], [0.08], [9.6], [-0.07], [6.13],
  [Venustiano Carranza], [0.05], [13.6], [-0.51], [2.03],
  [Xochimilco], [0.05], [5.0], [0.44], [5.99],
)


== c) ¿Cómo tomarías en cuenta el ejercicio del presupuesto de este fondo por parte de cada alcaldía en años pasados para la asignación de los siguientes años?

Para asignaciones futuras, consideraría:

- Reportes de transparencia y auditorías públicas.
- Participación ciudadana y quejas recibidas.
- Porcentaje del presupuesto que se uso en años anteriores.
- Impacto medible de los proyectos que fueron realizados (número de beneficiarios, calidad mejorada del parque y en general como se atendieron los factores que de a)).

== d) ¿Cómo evaluarías a futuro si la asignación realizada fue adecuada?

- Encuestas de satisfacción ciudadana por alcaldía.
- Aumento en uso o visitas a parques.
- Comparación de indicadores ambientales antes y después (vegetación, sombra, temperatura).
- Revisión del cumplimiento de metas físicas y financieras.
- Reportes de mantenimiento y conservación.
- Proporción del presupuesto realmente ejercido vs. lo asignado.

#pagebreak()
