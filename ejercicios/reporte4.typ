#import "../curp/datos.typ": *
#import "@preview/codly:1.3.0": *
#import "@preview/codly-languages:0.1.1": *
#show: codly-init.with()

#codly(languages: codly-languages)
= Ejercicio 4. CURP

Se analizó el archivo `curp_sucio.txt`, que contiene múltiples registros de CURP, para identificar aquellos que cumplen con la estructura oficial definida por la RENAPO.

== a) CURPs válidas

Se detectaron #validas CURPs válidas y #invalidas inválidas.
```python
regex = re.compile(
    r"^[A-Z]{4}" # 4 letras: iniciales del nombre y apellidos
    r"\d{2}(0[1-9]|1[0-2])([0-2][0-9]|3[01])"# FechaNacimiento: AAMMDD
    r"[HM]" # Sexo: H (hombre) o M (mujer)
    r"(AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|"   # Entidad federativa
    r"JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|"
    r"TC|TS|TL|VZ|YN|ZS)"
    r"[B-DF-HJ-NP-TV-Z]{3}" # Consonantes internas del nombre
    r"[A-Z\d]\d$"           # Homoclave: 1 letra o número y 1 dígito
)

# Filtrar CURPs válidas
curps_validas = [curp for curp in curps if regex.match(curp)]
```


== b) Personas por entidad federativa
#figure(
  image("../curp/fig_entidades.png", width: 80%),
  caption: [Distribución por entidad federativa (CURPs válidas)],
)

== c) Fechas de cumpleaños más comunes
Los tres cumpleaños mas comunes son:
- 04-18 con 21 personas
- 10-27 con 20 personas
- 05-14 con 17 personas

```python
# Extraer fechas de nacimiento (posición 4 a 10) y contar por mes y día (MM-DD)
fechas = [curp[6:10] for curp in curps_validas]  # MMDD
cumples = Counter(f"{f[:2]}-{f[2:]}" for f in fechas)
numFechas = 3
top_fechas = cumples.most_common(numFechas)

```
== d) ¿Los datos parecen reales?

No, la distribución debería ser proporcional a la cantidad
de personas viviendo en cada entidad federativa.

== Como se puede mejorar este proceso a partir de este punto?

Se puede mejorar el proceso de validación y análisis de CURPs mediante la
implementación de un sistema automatizado que realice las siguientes acciones:
- *Verificación de datos*: Implementar un sistema que cruce los CURPs con
  bases de datos oficiales para confirmar la existencia de las personas y sus
  datos asociados.
- *Análisis estadístico*: Desarrollar herramientas que permitan analizar la
  distribución de CURPs por entidad federativa y detectar patrones inusuales.
- *Reporte automatizado*: Generar informes automáticos en pdf mediante typst.

#pagebreak()
