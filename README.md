# vibration-sensor
## Introduction
A project to visualize vibration data according to wind strength on the web by collecting vibration data after attaching a vibration sensor to the fan.

## materials
- jetson nano : Vibration data sent from Arduin Required when saving to DB and visualizing vibration data on the web
- fan : vibrating data
- Arduino : Vibration data collection
- vibration sensor : A sensor that measures vibration data

![image](https://user-images.githubusercontent.com/88071262/131477452-5436621a-5cca-4d7d-a388-6d89ba47f260.png)

## project flow
<img width="526" alt="Screenshot 2021-08-30 154637" src="https://user-images.githubusercontent.com/88071262/131465653-eeb6a920-981c-4139-a216-21f51125c516.png">


- 1.After attaching the vibration sensor to the fan, the corresponding vibration data of each x, y, and z axis of acceleration, angular velocity, and angle are collected by using a cable with Arduino.
- 2. Transfer data from arduino to jetson nano through serial communication and save to s3
- 3. Run flask server on jetson nano to load data from s3.
- 4. After saving the data loaded from s3 in the form of an array, it is sent to HTML and JS.
- 4-1. Load the trained model and classify the wind strength of the data loaded from s3. After storing the classified data in s3, it is transmitted as HTML and JS.
- 5. Outputs an asynchronous graph using the last 60 data of the data entered in JS and HTML, and displays the real-time value, maximum value, minimum value, maximum-minimum, standard deviation, skewness, kurtosis, mean of absolute values, and mean of squares. Output the root asynchronously.
- 6. Loads the data of s3 where the wind strength is classified and outputs it asynchronously.


## model used

After classifying the wind strength using (cover_DL,cover_GB,cover_LinearSVC,cover_LR,motor_DL,motor_GB,motor_LinearSVC,motor_LR), the result of (high, medium, low) is output.

## result

https://user-images.githubusercontent.com/88071262/131480889-e7406e99-4b89-4079-8f48-c91cbf4bccd1.mp4

