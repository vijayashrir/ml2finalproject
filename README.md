# Image Recognition

I've build a python code that you build your own Image Classifier as a beginner and also train your images and to make predection.

# Info

This is a python program made by Rohan Thomas(me), I'm a 14 yrs and my areas of Intrest is Machine Learning, AI, Deep-Learning, Neural Networks etc. Here in this program I've used TensorFlow and Keras and the Neural Network used here is Convolutional Neural Networks

# Pre-requistes

TensorFlow: 
```
$ sudo pip install tensorflow 
```
Keras:
```
$ pip install keras 
```

# To Run the code

After you downalod the code unzip the file and create new 2 folders in the repository one is "dataset_image" and predicit.

# Dataset

open the folder which you have created "Dataset_image" then create a sub-folder on the images that you wanted to recognize by the machine. Eg. If you want to make a classify Cat and Dog. Create a folder named Cat and put the images of Cat from the Internet, then create a folder named the dog and put the images of Dog there. By using ImageNet you will get 1000s of images of different varieties of things.

# Training

Ones you prepared your dataset it is the time to train. Open terminal or command prompt in the folder the run the "file train.py" by (python train.py)

# Prediction

Ones you completed the training then come back to the same the repo and put the image you wanted to predict. If you wanted to predict cat (Take your phone and click an image of a cat then share it to the computer then put the file in predict folder. Open terminal in the folder and type "python predict.py" Magic Happens.

# Useful Links

TensorFlow: https://tensorflow.org

Keras: https://keras.io

# Common errors

[errorno 29] Not a directory: 'Dataset_image/.DS_Store' Go to load_data.py file the find label=label[1:] and make it as comment #label=label[1:]. If you are using Ubuntu you should comment it and if you are using a mac you should not comment it. If you find any more bug report me in rtfbuse@gmail.com# Tensorflow-image-classifier
