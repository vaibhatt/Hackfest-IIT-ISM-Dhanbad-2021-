# Team Hackoverflow

Submission for HackFest 2021

## Problem Statement
Aid for the blind

## The Idea
Our idea is to develop a product using hardware + software pipeline which would aid the blind in knowing about their surrondings.The most common problem faced by the blind  people is the inefficiency in understanding the surrondings .This often leads to major/minor accidents which sometimes become fatal.Our idea proposes to solve this problem using technology.

## Implementation details

We propose to solve the problem by using the conept of image captioning along with a basic tect to speech code.
The real time image being displayed onto a server by an IOT device will be fetched by the webapp, upon proper command from the user.This fetched image will then be transfered onto the pre-trained and pre-loaded ML code present in the sever connected to the web-app.The code will then output an MP3 sound file. This marks the completion of chain of events for one image.Similarly for other images also the same pipeline will be followed.

## About the dataset
Dataset used : Flickr8k dataset

download the dataset from here:
https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip

## Description of ML Pipeline
THE ML PIPELINE STARTS WITH THE USE OF THE PRE-TRAINED AND OPEN-SOURCE INCEPTION NET MODEL, TRAINED IN IMAGENET DATASET.THIS ACTS AS OUR IMAGE ENCODER MODEL.NEXT COMES THE RNN BASED LSTM MODEL HAVING TWO INPUTS.ONE THE ENCODED IMAGES BEING OUTPUT BY THE PREVIOUS MODEL AND ANOTHER THE PRE-BUILD GLOVE EMBEDDING GENERATED WORD VECTORS.THE MODEL THEN HAS TO OUTPUT THE PREDICTED CAPTIONS. THE PREDICTED CAPTIONS ARE CONVERTER TO SOUND BY USING gtts LIBRARY IN PYTHON

## Technologies Used

* Python, HTML, CSS ,JUPYTER NOTEBOOK
* ML/DL libraries : Tensorflow  / keras, n umpy , pandas etc.
* Flask, Jinja2 Templating Engine
* IP Webcam Config

## Screenshots

![front](https://github.com/vaibhatt/Hackfest-IIT-ISM-Dhanbad-2021-/blob/master/screenshot/Screenshot%20(2).png)

-----------

![back](https://github.com/vaibhatt/Hackfest-IIT-ISM-Dhanbad-2021-/blob/master/screenshot/Screenshot%20(3).png)

## Advantages
* The equipment used is cost efficient .
* The equipment is durable because of its wireless nature and can be used in all weather conditions.
* Materials used in the equipment are easily available.
* It can be easily used by a blind person.
* By using this method we will reduce the human assistance required by a blind person to a great extent and thus make him/her independent.

## Future Plans
* To make the product more efficient and product ready, the model has to be trained on a larger and more diverse dataset
* An app has to be build instead of webapp to make it accessible to the blind through his/her phone.
* Camera hardware devices such as ESP32 camera module can be used in order to click the image in real time.

## Team

- [Abhibhaw Asthana](https://github.com/abhibhaw)
- Pritish Samal
- Suyash Shrivastava
- Vaibhav Bhatt
- Vatsal Ojha
