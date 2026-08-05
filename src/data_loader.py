"""
=========================================================
Módulo: Carregamento de Dados
=========================================================
Autor: Gabriel Brito

Responsável por carregar o conjunto de dados
utilizado pelo sistema de detecção de fraudes.
=========================================================
"""

import pandas as pd
from config import DATASET


def carregar_dados():
    """
    Carrega o dataset de transações bancárias.

    Returns:
        pandas.DataFrame
    """
    try:
        dados = pd.read_csv(DATASET)
        print(f"✔️ Dataset carregado com sucesso! ({len(dados)} registros)")
        return dados

    except FileNotFoundError:
        print("❌ Arquivo de dados não encontrado.")
        return pd.DataFrame()

    except Exception as erro:
        print(f"Erro ao carregar os dados: {erro}")
        return pd.DataFrame()
