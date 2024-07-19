import pickle
from sklearn.linear_model import Lasso

class LassoRegressionModel():
    def __init__(self, params):
        super().__init__()
        self.params = params
        self.model = Lasso(
            alpha=self.params.get_param("alpha"),
            max_iter=self.params.get_param("max_iter"),
            tol=self.params.get_param("tol")
        )

    def getTypeModel(self):
        return "Sk"

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_predict):
        self.x_predict = x_predict
        self.y_predict = self.model.predict(x_predict)
        return self.y_predict

    def flops_calculation(self):
        return 'O(1)'

    def model_length(self):
        return len(self.model.coef_) + 1

    def compil(self):
        pass

    def evaluate(self, x_evaluate, y_evaluate):
        self.x_evaluate = x_evaluate
        self.y_evaluate = y_evaluate
        return self.model.score(x_evaluate, y_evaluate)

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.model, file)

    def summary(self):
        return {
            'coefficients': self.model.coef_,
            'intercept': self.model.intercept_
        }