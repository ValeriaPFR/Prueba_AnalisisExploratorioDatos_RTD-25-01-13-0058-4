import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Carga del conjunto de datos histórico
    df = pd.read_csv('videojuegos.csv')
    
    # ========================================================
    # PARTE 1: Análisis Visual con Seaborn
    # ========================================================
    print("--- Iniciando Parte 1: Análisis Visual con Seaborn ---")
    
    # Configuración de estética base para gráficos de Seaborn
    sns.set_theme(style="ticks")
    
    # 1. Gráfico de Pares (pairplot)
    num_cols = ['Ventas_NA', 'Ventas_EU', 'Ventas_JP', 'Critica_Puntaje', 'Plataforma']
    g = sns.pairplot(df[num_cols], hue='Plataforma', palette='Set2')
    g.fig.suptitle('Gráfico de Pares (Pairplot) de Variables Numéricas por Plataforma', y=1.02, fontsize=14)
    plt.savefig('pairplot_videojuegos.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("[OK] Gráfico 'pairplot_videojuegos.png' exportado con éxito.")
    
    # 2. Gráfico de Violín (violinplot)
    plt.figure(figsize=(8, 5))
    sns.violinplot(data=df, x='Plataforma', y='Critica_Puntaje', palette='Set2')
    plt.title('Distribución de Critica_Puntaje por Plataforma', fontsize=12)
    plt.xlabel('Plataforma')
    plt.ylabel('Puntaje de la Crítica')
    plt.tight_layout()
    plt.savefig('violinplot_critica.png', dpi=300)
    plt.close()
    print("[OK] Gráfico 'violinplot_critica.png' exportado con éxito.")
    
    # 3. Mapa de Calor (heatmap)
    num_df = df[['Ventas_NA', 'Ventas_EU', 'Ventas_JP', 'Critica_Puntaje']]
    corr_matrix = num_df.corr()
    
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr_matrix, annot=True, cmap='Blues', fmt='.3f', square=True, cbar_kws={"shrink": .8})
    plt.title('Matriz de Correlación de Variables Numéricas', fontsize=12)
    plt.tight_layout()
    plt.savefig('heatmap_correlacion.png', dpi=300)
    plt.close()
    print("[OK] Gráfico 'heatmap_correlacion.png' exportado con éxito.\n")

    # ========================================================
    # PARTE 2: Personalización de Gráficos con Matplotlib
    # ========================================================
    print("--- Iniciando Parte 2: Personalización con Matplotlib ---")
    
    # 4. Preparación de Datos
    df['Ventas_Globales'] = df['Ventas_NA'] + df['Ventas_EU'] + df['Ventas_JP']
    ventas_por_genero = df.groupby('Genero')['Ventas_Globales'].mean().reset_index()
    
    # Creación y Personalización del Gráfico de Barras (5 y 6)
    plt.figure(figsize=(10, 6))
    barras = plt.bar(
        ventas_por_genero['Genero'], 
        ventas_por_genero['Ventas_Globales'], 
        color='steelblue', 
        edgecolor='black'
    )
    
    # Títulos y etiquetas de ejes
    plt.title('Promedio de Ventas Globales por Género de Videojuego', fontsize=14, pad=15)
    plt.xlabel('Género', fontsize=12)
    plt.ylabel('Ventas Globales Promedio (Millones de USD)', fontsize=12)
    
    # Límites del eje Y (Holgura superior del 15% por encima del valor máximo)
    max_val = ventas_por_genero['Ventas_Globales'].max()
    plt.ylim(0, max_val * 1.15)
    
    # Inserción de anotaciones numéricas exactas sobre cada barra
    for barra in barras:
        yval = barra.get_height()
        plt.text(
            barra.get_x() + barra.get_width()/2.0, 
            yval + (max_val * 0.02), 
            f'{yval:.2f}', 
            ha='center', 
            va='bottom', 
            fontsize=10, 
            fontweight='bold'
        )
    
    # Almacenamiento final de la visualización personalizada
    plt.tight_layout()
    plt.savefig('ventas_por_genero_personalizado.png', dpi=300)
    plt.close()
    print("[OK] Gráfico 'ventas_por_genero_personalizado.png' exportado con éxito.")
    print("\n--- Procesamiento y EDA Finalizados Exitosamente ---")

if __name__ == "__main__":
    main()