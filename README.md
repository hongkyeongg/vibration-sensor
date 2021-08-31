# vibration-sensor
## Introduction
A project to visualize vibration data according to wind strength on the web by collecting vibration data after attaching a vibration sensor to the fan.

## materials
- jetson nano : Vibration data sent from Arduin Required when saving to DB and visualizing vibration data on the web
- fan : vibrating data
- Arduino : Vibration data collection
- vibration sensor : A sensor that measures vibration data(Vibration sensor used wit motion BWT61CL-E.)

![image](https://user-images.githubusercontent.com/88071262/131477452-5436621a-5cca-4d7d-a388-6d89ba47f260.png)

## project flow
<img width="526" alt="Screenshot 2021-08-30 154637" src="https://user-images.githubusercontent.com/88071262/131465653-eeb6a920-981c-4139-a216-21f51125c516.png">


1. After attaching the vibration sensor to the fan, the corresponding vibration data of each x, y, and z axis of acceleration, angular velocity, and angle are collected by using a cable with Arduino.
2. Transfer data from arduino to jetson nano through serial communication and save to s3
3. Run flask server on jetson nano to load data from s3.
4. After saving the data loaded from s3 in the form of an array, it is sent to HTML and JS. 
4-1. Load the trained model and classify the wind strength of the data loaded from s3. After storing the classified data in s3, it is transmitted as HTML and JS.
5. Outputs an asynchronous graph using the last 60 data of the data entered in JS and HTML, and displays the real-time value, maximum value, minimum value, maximum-minimum, standard deviation, skewness, kurtosis, mean of absolute values, and mean of squares. Output the root asynchronously.
6. Loads the data of s3 where the wind strength is classified and outputs it asynchronously.

## process

- Real-time data collection of vibration sensor
: After attaching the vibration sensor to the fan, the corresponding vibration data of each x, y, and z axis of acceleration, angular velocity, and angle are collected by using a cable with Arduino.

![image](https://user-images.githubusercontent.com/88071262/131484470-60551b3f-bde1-41fe-a1ce-987fc814082a.png)


- Receive data from arduino to jetson nano through serial communication

- Data received by jetson nano is stored in s3, and is stored in s3 as
![image](https://user-images.githubusercontent.com/88071262/131484837-ad447c4d-4d7f-4838-976a-5321cbec66e2.png)

- Visualization via web page
: Flask server runs on jetson nano, and Python, HTML, and JS are used to create web pages.
In python, the data stored in s3 is transmitted as HTML and JS, and the latest 60 data are read and visualized through a web page.

: At the top, we created 9 buttons to view the acceleration, angular velocity, and angle for each of the x, y, and z axes.

: At the bottom of the web page, the wind strength for the last 5 seconds predicted using three machine learning models and one deep learning model is output.

![image](https://user-images.githubusercontent.com/88071262/131485049-fe9b97f8-c322-482f-9e0c-2267fb4b3ac4.png)

: When you click the button, real-time data values and graphs are output, and in addition, 9 statistical values ​​for the latest 60 values are output.

![image](https://user-images.githubusercontent.com/88071262/131485189-d6b63ec8-0ddf-4b24-b47b-0a22a4a81790.png)



# model used
## machine learning model training
- For classification, three machine learning methods were trained: GradientBoosting, LinearSVC, and Linear Regression.

### Machine Learning Model Test Results
- As a result of testing the machine learning model, in the case of GradientBossting, both the model using the data collected from the motor position and the model trained with the data collected from the cover position showed high performance. However, it was confirmed that the performance of the model trained with the motor position data in LinearSVC and Linear Regression was not good, while the model using the data collected from the cover position performed well.
- 
- This phenomenon appears to have occurred because the vibration according to the wind strength was better reflected in the cover position than in the motor position of the fan.

### Deep learning model training
- Machine learning performs well on well-refined data or simple data, but its performance deteriorates when there is a lot of data and more complex data. In addition, there is a disadvantage that a person has to manually purify the data. The deep learning model analyzes data by itself through a neural network without human intervention and shows high performance even on complex high-dimensional data.

- For this reason, research to solve various problems that were not previously solved by machine learning using deep learning is being conducted.

- In the case of the machine learning model, the data collected from the cover position was suitable for classification of wind strength, but the data collected from the motor position was not well classified. Therefore, we checked whether the problem is due to the limitations of machine learning or the problem of data through the deep learning model.

- The deep learning model for learning is implemented as follows

![image](https://user-images.githubusercontent.com/88071262/131482632-a016bede-4b62-4219-98fa-a8d6a5fc8e75.png)

#### Deep learning model training results
- Motor position learning and test results
![image](https://user-images.githubusercontent.com/88071262/131482806-4cdcc574-65c7-4692-a2e0-f5b8b78b3e56.png)

- Cover position learning and test results
![image](https://user-images.githubusercontent.com/88071262/131482950-28f4f5ab-7a49-4030-8c8c-8df8f9c71eaa.png)



## result

https://user-images.githubusercontent.com/88071262/131480889-e7406e99-4b89-4079-8f48-c91cbf4bccd1.mp4

- It collects data using a vibration sensor and predicts the wind strength in real time through machine learning and deep learning based on the collected data. The collected data and prediction results are visualized through a web page and a system has been implemented so that users can easily check them.
- Through this, it has been verified that the vibration data is effective in predicting the state of the machine.

