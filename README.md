# DatosCDMX

This repository contains various data analyses addressing environmental, social, and administrative issues in Mexico, focusing on data-driven validation, structural consistency, and geospatial analysis.

## Structure

* `airbnbPrices/`: Data analysis of Airbnb listing prices in Mexico City, covering exploratory analysis, geospatial clustering, feature engineering, and predictive modeling.
* `cutzamalaSystem/`: Analysis of reservoir storage in the Cutzamala System (2020–2024).
* `parkBudget/`: Proposed budget allocation for parks in Mexico City.
* `center/`: Determination of Mexico’s geographic center using different criteria.

---

## Airbnb Prices

![Average Airbnb prices by neighbourhood](assets/placeholder.png)

This project analyzes Airbnb listing prices in Mexico City, relating them to geographic location, proximity to amenities, and socio-economic indicators.

**Dataset**: `airbnb_cdmx_2024_data.csv` located in `data/` folder, including features such as price, room type, neighbourhood, distances to services (supermarket, hospital, subway, park, university, restaurant), and socio-economic indices (income per month, average cost of living, demand index, security index).

**Objectives**:

* Perform exploratory data analysis to characterize price distribution across neighbourhoods and room types.
* Identify price clusters and hotspots using geographic clustering (Folium/GeoPandas).
* Engineer features (log-price, price categories, distances to points of interest, socio-economic interactions).
* Build and evaluate predictive models (linear regression, random forest, XGBoost) to estimate listing prices.

### Key Methodology

1. **Data Loading & Validation**: Read CSV, handle missing values, convert price to log scale.
2. **Exploratory Analysis**: Boxplots by room type and neighbourhood, heatmaps of price density, choropleth maps of average price.
3. **Feature Engineering**: Create `price_category` by quantiles, compute distances using GeoPandas, interaction terms with socio-economic variables.
4. **Modeling**: Split data (80/20), train linear models (Ridge/Lasso), random forest, and XGBoost; compare MAE and RMSE.
5. **Visualization**: Plot feature importances, prediction vs actual prices, and interactive maps.

---

## Cutzamala System

![Comparative percentage chart 2018–2022](assets/comparativo_porcentajes_2018_2022.png)

This analysis covers the absolute storage volume (in millions of m³) and fill percentage of the three main reservoirs in the Cutzamala System: **El Bosque**, **Valle de Bravo**, and **Villa Victoria**, using historical data from 2020 to 2024.

* A Python script downloads and processes data directly from the CONAGUA FTP server.
* Four plots are generated:

  * Individual storage charts for each reservoir.
  * A comparative fill-percentage chart for all three.
* Figures are saved automatically to `assets/` and `cutzamalaSystem/figs/`.
* Use the `-s` flag to display each plot on-screen.

### Usage

```bash
# Download data from CONAGUA FTP
python3 cutzamalaSystem/getDataFromSIH.py
# Generate plots for a specific range
default usage: last four available years
python3 cutzamalaSystem/plot_cutzamala.py -i 2020 -f 2024 -s
```

* `-i, --inicio`: Start year (e.g., 2020).
* `-f, --fin`: End year (e.g., 2024).
* `-s, --show`: Display plots in addition to saving.

---

## Exercise 3: Geographic Center of Mexico

![Map of the three candidate locations](assets/centro-mexico-mapa.png)

We compare three sites claiming to be Mexico’s center: **Cañitas de Felipe Pescador** (Zacatecas), **Tequisquiapan** (Querétaro), and **Aguascalientes** (Aguascalientes). The analysis uses three different approaches: geographic, symbolic, and institutional.

* A Python script downloads and filters the Natural Earth shapefile for Mexico, then plots the three points of interest.
* The resulting map is saved as a PNG in `assets/`.
* Use the `-s`/`--show` flag to display the map on-screen.

### Usage

```bash
# First-time setup: download and prepare the shapefile
python3 center/generaMapa.py --first-run

# Generate and display the map
python3 center/generaMapa.py --show
```

* `--first-run`: Download and prepare the shapefile.
* `-s, --show`: Display the map on-screen.

---
