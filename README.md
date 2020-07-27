# smart_attendance
Mark attendance with time using face recognition



## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Directory Tree](#directory-tree)
  * [Installation](#installation)
  * [To Do](#to-do)
  * [Bug / Feature Request](#bug---feature-request)
  * [Contribution](#contribution)
  * [Technologies Used](#technologies-used)
  * [Team](#team)


## Demo

![](https://i.imgur.com/jodJyw2.png)



## Overview
A web Application developed via streamlit automating attendance system via face detection. 
Face Detection is done by haar cascade frontal face detector that is a pretrained model for detecting face . 
After that face area is cropped and then doing so create a dataset for all users for training and all images are stored in dataset folder.
After that run 'face_dataset_trainer' file and train model and store that trained matrix in yml fie. After that open streamlit app and 
start predicting using that trained yml file .

## Directory Tree 
```

├── Attendance.csv
├── README.md
├── activation.bat
├── dataset_maker.py
├── face_dataset_trainer.py
├── haarcascade_frontalface_default.xml
├── limitation.txt
├── requirements.txt
├── trainingData.yml
├── webapp.py



```
In above directory structure outputs folder is created only when images and videos is required by user. Facility for choosing this option is given at top of side-bar of application.

## Installation
1. Windows user can double click on activation.bat file to install required package
2. Linux User type following command in commnand line
a) First create a virtual environment 
```bash
python3.7 -m virtualenv venv
```
b) Move to venv directory and activate environment
```bash
cd venv
. bin/activate
```
c) Clone this project 
```bash
git clone https://github.com/pandeynandancse/smart_attendance.git
```

d) Move into cloned directory
```bash
cd smart_attendance
```
e) Now install all requirements
```bash
pip install -r requirements.txt
```
## Run
1. After successfull installation windows user can directly open the link that will be appeared
2. After successful installation open type
```bash
streamlit run app.py
 ```
and then open link 

## To Do
1. Future Work has been listed in [limitation.txt](limitation.txt) file.



## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/pandeynandancse/smart_attendance/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/pandeynandancse/smart_attendance/issues/new). Please include sample queries and their corresponding results.


## Contribution
If you'd like to do some contribution, feel free to do so by opening a pull request [here](https://github.com/pandeynandancse/smart_attendance/pulls). Please include sample queries and their corresponding results.




## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://i.imgur.com/jAyHARm.png" width=170>](https://www.streamlit.io/)
[<img target="_blank" src="https://i.imgur.com/OhpT4U4.jpg" width=170>](https://opencv.org/) 



## Contributor
[![Nandan Pandey](https://qph.fs.quoracdn.net/main-thumb-189737418-200-jmwzsixdznlgemnejuecomukeluqkgzd.jpeg)](https://pandeynandancse.github.io) |
-|
[Nandan Pandey](https://pandeynandancse.github.io) |)



 
