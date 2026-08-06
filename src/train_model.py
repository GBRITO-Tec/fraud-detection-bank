"""
Treinamento do Modelo de Detecção de Fraudes Bancárias
Autor: Gabriel Brito
"""

from sklearn.ensemble import IsolationForest


def train_model(X_train):
    """
    Treina o modelo de detecção de anomalias.

    Parâmetros:
        X_train (DataFrame): Dados de treinamento.

    Retorna:
        model: Modelo treinado.
    """

    model = IsolationForest(
        n_estimators=100,
        contamination=0.02,
        random_state=42
    )

    model.fit(X_train)

    print("Modelo treinado com sucesso!")

    return model
