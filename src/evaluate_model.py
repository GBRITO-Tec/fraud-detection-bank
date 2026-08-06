"""
Avaliação do Modelo de Detecção de Fraudes Bancárias
Autor: Gabriel Brito
"""

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)
import matplotlib.pyplot as plt
import seaborn as sns


def evaluate_model(y_true, y_pred):
    """
    Avalia o desempenho do modelo.
    """

    print("\n========== RESULTADOS ==========")

    print(f"Acurácia: {accuracy_score(y_true, y_pred):.4f}")

    print("\nRelatório de Classificação:")
    print(classification_report(y_true, y_pred))

    cm = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Normal", "Fraude"],
        yticklabels=["Normal", "Fraude"]
    )

    plt.title("Matriz de Confusão")
    plt.xlabel("Predição")
    plt.ylabel("Valor Real")
    plt.tight_layout()
    plt.show()
