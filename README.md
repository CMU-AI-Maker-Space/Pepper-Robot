# Pepper-Robot
This repository contains the code for the Pepper robot in the AI Maker Space at Carnegie Mellon University.

The official documentation for the Pepper robot can be found [here](http://doc.aldebaran.com/2-4/home_pepper.html).
The official documentation for the NAOqi Python SDK can be found [here](http://doc.aldebaran.com/2-4/index_dev_guide.html).

## Getting Started
1. Clone the repository
2. Set up the virtual environment
3. Install the required packages
4. Run the required code

### Clone the repository
```bash
git clone https://github.com/CMU-AI-Maker-Space/Pepper-Robot
```

### Set up the virtual environment

#### Install Python 2.7

More information can be found [here](https://www.python.org/downloads/release/python-2718/)

```bash
sudo apt-get install python2.7
```

#### Install pip
```bash
sudo apt-get install python-pip
```

#### Install virtualenv
```bash
pip install virtualenv
```

#### Create the virtual environment

More information can be found [here](https://docs.python-guide.org/dev/virtualenvs/) and here [here](https://stackoverflow.com/questions/65685217/how-to-create-a-python-2-7-virtual-environment-using-python-3-7)

```bash
virtualenv -p python2.7 venv
```

#### Activate the virtual environment
```bash
source venv/bin/activate
```

### Install the required packages
```bash
pip install -r requirements.txt
```

### Run the required code
```bash
python <file_name>.py
```

## Face Recognition

This code was adapted from [here](https://blogemtech.medium.com/pepper-facial-recognition-43e24b10cea2)

This is still a work in progress. The code is not fully functional yet.

## Read Images from Camera

This code was adaper from the NAOqi Documentation

This code can be used to extract images from the head camera on the robot

## Interaction

This code was adapted from the NAOqi Documentation

Other custom interactions can be defined as methods like say_welcome() in interact.py

## Tablet Control

In progress