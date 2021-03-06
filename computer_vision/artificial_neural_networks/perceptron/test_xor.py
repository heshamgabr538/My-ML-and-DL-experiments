from computer_vision.artificial_neural_networks.perceptron.perceptron import Perceptron
import numpy as np

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

perceptron = Perceptron(2,alpha=0.001)

perceptron.fit(x, y,epochs=2000)
for (data, target) in zip(x, y):
    prediction = perceptron.predict(data)
    print(f"[TESTING] data={data}, ground-truth={target}, prediction={prediction}")
