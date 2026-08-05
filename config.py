"""
=========================================================
Configurações do Projeto
=========================================================
Autor: Gabriel Brito

Este arquivo centraliza os caminhos utilizados
pelo sistema.
=========================================================
"""

import os

# Diretórios principais
BASE_DIR = os.path.dirname(os.path.abspath(_file_))

DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(BASE_DIR, "models")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# Arquivos
DATASET = os.path.join(DATA_DIR, "transacoes.csv")
MODEL = os.path.join(MODEL_DIR, "random_forest.pkl")

# Configurações do projeto
RANDOM_STATE = 42
TEST_SIZE = 0.20
