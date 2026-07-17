# Prueba: Análisis Exploratorio de Datos (EDA)

Este repositorio contiene el desarrollo técnico, los scripts de procesamiento y las visualizaciones correspondientes a la prueba de análisis exploratorio de datos aplicado a un catálogo histórico de videojuegos (`videojuegos.csv`).

El objetivo fundamental de este proyecto es aplicar técnicas de análisis visual y estadístico para identificar patrones de consumo regionales, contrastar perfiles de calificación por plataforma y evaluar la relación entre la opinión de la crítica especializada y el éxito comercial de los títulos.

---

## 📋 Estructura del Proyecto

El repositorio se organiza de la siguiente manera:

*   **`videojuegos.csv`**: Base de datos de origen con registros de ventas regionales (Norteamérica, Europa, Japón) y evaluaciones de la crítica especializada.
*   **`prueba_analisis_exploratorio_datos.py`**: Script automatizado en Python que realiza la carga de datos, el procesamiento estadístico y la generación de gráficos de alta definición utilizando las librerías Seaborn y Matplotlib.
*   **`pairplot_videojuegos.png`**: Gráfico de pares generado para evaluar simultáneamente la interacción cruzada de todas las variables numéricas segmentadas por plataforma.
*   **`violinplot_critica.png`**: Gráfico de violín que contrasta los rangos, medianas y la densidad de las calificaciones de la prensa según el hardware.
*   **`heatmap_correlacion.png`**: Mapa de calor con anotaciones numéricas que calcula y visualiza la matriz de correlación de Pearson.
*   **`ventas_por_genero_personalizado.png`**: Gráfico de barras pulido y personalizado con Matplotlib que detalla el promedio exacto de ventas globales por género de videojuego.

---

## 💻 Ejecución y Salida de la Terminal

Al ejecutar el script técnico en la terminal de VSCode, el flujo de procesamiento se completa de manera secuencial y exporta de forma exitosa todas las piezas gráficas requeridas al directorio local.

```text
--- Iniciando Parte 1: Análisis Visual con Seaborn ---
[OK] Gráfico 'pairplot_videojuegos.png' exportado con éxito.
c:\...\prueba_analisis_exploratorio_datos.py:28: FutureWarning: 
Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0.
  sns.violinplot(data=df, x='Plataforma', y='Critica_Puntaje', palette='Set2')
[OK] Gráfico 'violinplot_critica.png' exportado con éxito.
[OK] Gráfico 'heatmap_correlacion.png' exportado con éxito.

--- Iniciando Parte 2: Personalización con Matplotlib ---
[OK] Gráfico 'ventas_por_genero_personalizado.png' exportado con éxito.

--- Procesamiento y EDA Finalizados Exitosamente ---
