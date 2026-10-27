from src.carga import cargar_datos
from src.limpieza import limpiar_datos
from src.transformacion import calcular_metricas
from src.analisis import analizar_potencial_crecimiento
from src.reporte import generar_reporte

def main():
    ruta = "datos/minerales_no_metalicos.csv"

    df = cargar_datos(ruta)
    df = limpiar_datos(df)
    df = calcular_metricas(df)

    ranking = analizar_potencial_crecimiento(df)
    print("Ranking de potencial de crecimiento por mineral:")
    print(ranking.to_string(index=False))

    generar_reporte(ranking, "reportes/reporte_minerales.txt")

if __name__ == "__main__":
    main()