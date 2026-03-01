# 🤖DEEP LEARNING PROJECTS SUMMARIES

## 1. BREAST CANCER CLASSIFICATION
- For creating the neural networks for this project, it will need to import 2 libraries. 
  1. Tensorflow
  2. Keras

**Tensorflow** 
  is deep learning library developed by google. So there are several functions and we can create nueral networks easily by using this library. Pytorch, microsoft cntk which is basically cognition toolkit so these libraries are used for creating deep learning neural networks. But most widely used Tensorflow and PyTorch libraries.

**Keras** is not a standalone library so it is just a wrapper of this tensorflow and keras. 

When tensorflow was released initially it was hard to make neural networks from tensorflow because like the coding part is bit hard, so thats where the keras come to play. It is used tensorflow as its backend and after that the building neural networks become easy because they have created several APIs and functions. So that we can easily build our neural network. 

- random seed is used for  no matter how many times you run your code you will get the same accuracies force so that is the idea of setting the random seed. 

- In this neural network I have used 3 layers. One layer for input layer which has 30 Neurons, for hidden layer has 20 Neurons and the output layer has 2 Neurons. 

- For the hidden layers I have used relu activation function and for the output layers I have used sigmoid activation function. Because sigmoid function is not used in hidden layers.

- Those 2 Neurons represent the Malignant and Benign. Those two neuron gives the predicted values and for the final outcome is based on the maximum value in between those output neurons. 

- For find the maximum value I have used argmax function. 