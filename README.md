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

## 2. Processing Image Data in Python for Deep Learning Applications

- This project will help to learn how to read an image file and how to convert it to an numpy array and also how to resize an image.
- When we use dataset with images those images should be same dimension for the train neural networks, otherwise it cannot be train. 
- And this project we can learn how to convert RGB image into gray scale image. 

- Libraries that can be used for image processing
1. matplotlib.image
2. pillow
3. OpenCV

- In a grayscale image it can be represent using only 1 metrics which represents all the cells with corresponding the white intensity. 255- white, 0 - black
- But RGB images it has 3 metrices those are corresponding to the RED intensity valued metrics, Green intensity valued metrics and Blue intensity valued metrics. 

- **Purpose of doing this**
  - Converting RGB image into grayscale image is help to save the space using only one metrics instead of using 3 metrices. So it will save lot of computation power as well as the time time that has been taking for processing the image. So we can use those grayscale image for neural network. 

  - We cannot do this conversion all the time when the examine a color of a image. So if we are making those images into gray that is meaningless. 
  
## 3. MINST Handwritten Digit Classification
- Dataset -> Image processing -> Train Test Split -> Neural Network -> Evalution of Neural Network 
- Here MNIST dataset we don't need to do image processing part, it is already done in the dataset. So we need to do only divided the training set and the test set.

- Here I have not used Convolution Neural Network which called as CNN, because it is little bit complex and it use for Image Recognition. 
Here we are using RNN because it use to Text Recognition and audio recognition.

- Now the image is turned into a metrics but it cannot be used as inputs to the neural network. So we need to make those values in a single array. Thats why we use Flatten option. 
- I have used 4 layer neural network. 
  - Input Layer
  - Hidden Layer 1 with 50 neurons
  - Hidden Layer 2 with 50 neurons
  - Output Layer with 10 neurons. The reason behind the number of output layer is there should be 10 outputs we are expecting from this images. Which are [0,1,2,3,4,5,6,7,8,9]. Each nueron has responsibilty of the each corresponding number. Thats why I select 10 nuerons for output layer. 
