import pandas as pd

def calcular_metricas(df):
    """
    Ordena los datos y calcula métricas clave por mineral.
    """
    df = df.sort_values(["Mineral", "Año"]).reset_index(drop=True)

    resumen = (
        df.groupby("Mineral")
        .agg(
            Inicio_Produccion=("Produccion", "first"),
            Fin_Produccion=("Produccion", "last"),
            Inicio_Exportacion=("Exportacion", "first"),
            Fin_Exportacion=("Exportacion", "last"),
            Inicio_Valor=("Valor_Economico", "first"),
            Fin_Valor=("Valor_Economico", "last"),
            Años=("Año", "nunique")
        )
        .reset_index()
    )

    def crecimiento(inicial, final):
        if pd.isna(inicial) or inicial == 0:
            return 0.0
        return ((final - inicial) / inicial) * 100

    resumen["Crecimiento_Produccion"] = resumen.apply(
        lambda row: crecimiento(row["Inicio_Produccion"], row["Fin_Produccion"]), axis=1
    )
    resumen["Crecimiento_Exportacion"] = resumen.apply(
        lambda row: crecimiento(row["Inicio_Exportacion"], row["Fin_Exportacion"]), axis=1
    )
    resumen["Crecimiento_Valor"] = resumen.apply(
        lambda row: crecimiento(row["Inicio_Valor"], row["Fin_Valor"]), axis=1
    )

    resumen["Potencial_Crecimiento"] = (
        resumen["Crecimiento_Produccion"] * 0.5
        + resumen["Crecimiento_Exportacion"] * 0.3
        + resumen["Crecimiento_Valor"] * 0.2
    )

    return resumen