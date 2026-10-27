import os

def generar_reporte(ranking, ruta_salida):
    """
    Genera un archivo de texto con el resumen final.
    """
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

    mineral_lider = ranking.iloc[0]
    mensaje = f"""
Reporte de análisis: minerales no metálicos
==========================================

Mineral con mayor potencial de crecimiento:
- {mineral_lider['Mineral']}
- Crecimiento producción: {mineral_lider['Crecimiento_Produccion']:.2f}%
- Crecimiento exportación: {mineral_lider['Crecimiento_Exportacion']:.2f}%
- Crecimiento valor económico: {mineral_lider['Crecimiento_Valor']:.2f}%
- Potencial total: {mineral_lider['Potencial_Crecimiento']:.2f}%

Top 5 minerales por potencial:
"""
    for i, fila in ranking.head(5).iterrows():
        mensaje += (
            f"{i + 1}. {fila['Mineral']} | "
            f"Potencial: {fila['Potencial_Crecimiento']:.2f}% | "
            f"Producción: {fila['Crecimiento_Produccion']:.2f}% | "
            f"Exportación: {fila['Crecimiento_Exportacion']:.2f}%\n"
        )

    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(mensaje)

    print(f"Reporte generado en: {ruta_salida}")