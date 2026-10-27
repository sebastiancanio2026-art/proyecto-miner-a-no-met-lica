import pandas as pd

def limpiar_datos(df):
    """
    Normaliza columnas, elimina filas vacías y convierte tipos.
    """
    df.columns = [
        col.strip()
        .lower()
        .replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace(" ", "_")
        for col in df.columns
    ]

    columnas_renombradas = {
        "ano": "Año",
        "anio": "Año",
        "mineral": "Mineral",
        "produccion": "Produccion",
        "exportacion": "Exportacion",
        "valor_economico": "Valor_Economico",
        "valor_economico_": "Valor_Economico",
        "valor_económico": "Valor_Economico",
    }

    df = df.rename(columns=columnas_renombradas)

    df = df.dropna(subset=["Año", "Mineral", "Produccion", "Exportacion", "Valor_Economico"]).copy()

    df["Año"] = df["Año"].astype(int)
    df["Produccion"] = pd.to_numeric(df["Produccion"], errors="coerce")
    df["Exportacion"] = pd.to_numeric(df["Exportacion"], errors="coerce")
    df["Valor_Economico"] = pd.to_numeric(df["Valor_Economico"], errors="coerce")

    df = df.dropna(subset=["Produccion", "Exportacion", "Valor_Economico"]).reset_index(drop=True)

    return df