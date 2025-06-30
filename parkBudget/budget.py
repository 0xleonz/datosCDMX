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
# Estándar falsamente recomendado por la OMS
estandar = 9.0
# Factor de ajuste
df["factor"] = ((estandar - df["Área_verde_m2hab"]) / estandar).clip(lower=-0.9)
df["pct_pob"] = df["Población"] / df["Población"].sum()
df["pct_ajustada"] = (df["pct_pob"] * (1 + df["factor"]))
# Normalizar para que sume 100%
df["pct_final"] = df["pct_ajustada"] / df["pct_ajustada"].sum() * 100
print(df[["Alcaldía","pct_pob","Área_verde_m2hab","factor","pct_final"]].round(2))
