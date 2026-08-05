"""
=========================================================
Sistema de Detecção de Fraudes Bancárias
=========================================================

Autor: Gabriel Brito
Versão: 1.0

Descrição:
Este projeto utiliza técnicas de Machine Learning para
identificar possíveis fraudes em transações bancárias.
O sistema realiza o carregamento dos dados, pré-processamento,
treinamento do modelo e avaliação dos resultados.

Tecnologias utilizadas:
- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib

Objetivo:
Auxiliar instituições financeiras na identificação
de transações suspeitas, reduzindo perdas financeiras
e aumentando a segurança dos clientes.

=========================================================
"""

from src.data_loader import carregar_dados

def main():
    print("========================================")
    print(" Sistema de Detecção de Fraudes Bancárias")
    print(" Desenvolvido por Gabriel Brito")
    print("========================================\n")

    dados = carregar_dados()
    print("Primeiras transações carregadas:")
    print(dados.head())

if _name_ == "_main_":
    main()
