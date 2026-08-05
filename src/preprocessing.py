"""
=========================================================
Pré-processamento dos Dados
=========================================================
"""

import pandas as pd


def limpar_dados(df):
    """
    Remove registros duplicados e valores nulos.
    """
    df = df.drop_duplicates()
    df = df.dropna()

    return df
