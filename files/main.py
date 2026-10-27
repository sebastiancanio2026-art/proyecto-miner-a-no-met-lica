from src.carga import cargar_todos_los_datos
from src.limpieza import limpiar_datos_produccion
from src.transformacion import transformar_a_formato_largo
from src.analisis import analizar_dataset
from src.reporte import generar_grafico_produccion

def main():
    print("Iniciando pipeline de análisis para Minería No Metálica...")
    
    # 1. Carga
    df_prod_raw, df_exp_fis, df_exp_val = cargar_todos_los_datos()
    
    # 2. Limpieza
    df_prod_limpio = limpiar_datos_produccion(df_prod_raw)
    
    # 3. Análisis Inicial
    analizar_dataset(df_prod_limpio, nombre="Producción Minería No Metálica")
    
    # 4. Transformación
    df_prod_long = transformar_a_formato_largo(df_prod_limpio, id_col='PRODUCTO', var_name='AÑO', value_name='PRODUCCION_TM')
    
    # 5. Reporte y Visualización
    generar_grafico_produccion(df_prod_long)
    
    print("\n¡Pipeline ejecutado exitosamente!")

if __name__ == "__main__":
    main()