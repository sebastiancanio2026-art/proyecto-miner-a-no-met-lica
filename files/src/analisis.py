import pandas as pd

def analizar_potencial_crecimiento(df):
    """
    Ordena los minerales por potencial de crecimiento.
    """
    ranking = df.sort_values("Potencial_Crecimiento", ascending=False).reset_index(drop=True)
    return ranking