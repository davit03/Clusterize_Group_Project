from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt


class Model:
    def __init__(self, model, params):
        self.data = None
        self.predictions = None
        self.model = model(**params)

    def fit_predict(self, df):
        self.data = df
        self.predictions = self.model.fit_predict(self.data)

    def silhouette_coef(self):
        return silhouette_score(self.data, self.predictions)

    def get_results(self):
        return self.silhouette_coef(), self.get_picture()

    def get_picture(self):
        if self.data.shape[1] > 3:
            return None
        plt.scatter(self.data[:, 0], self.data[:, 1], c=self.predictions, cmap='viridis')
        plt.title('Cluster Predictions with' + type(self.model).__name__)
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.colorbar(label='Cluster')
        file_name = type(self.model).__name__ + "_predictions.png"
        plt.savefig(file_name)
        return plt
