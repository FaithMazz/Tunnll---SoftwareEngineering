
# Task 2 - Dockerfile and Python Command Line Application

## Overview

The contents of this folder is a Dockerfile and a Python file named 'task2Python.py'.

The Dockerfile can build an image the runs a very simple command line echo of "Hello, Docker".



## How to Run the Dockerfile

First, ensure that you have Docker installed by running the following command in the terminal:

**docker version**

If you do not see information about your docker version, then move to the 'Installing Docker' section below.

If docker is correctly installed on your system, then you need to pull the folder from this repository, then run the following command in the terminal:

**docker build -t insertNameHere .**

This will build the docker image using the name you've given it. You will then need to run the image by entering the following command in ther terminal:

**docker run insertNameHere**



## Installing Docker
*Please note this may not be necessary. Check first to see if you have Docker already installed.*

### using Ubuntu, from package

#### Optional Step - Installing extra packages for Trusty 14.04
This is not required, but Docker strongly recommends it.
To install, enter the following commands in the terminal:

**sudo apt-get update**
**sudo apt-get install \
  linux-image-extra-$(uname -r) \
  linux-image-extra-virtual**
  
Next, you will need to go to this site (https://download.docker.com/linux/ubuntu/dists/).
Select your Ubuntu version, navigate to pool/stable, and download the appropriate .deb file.
Then, install Docker by using the following command, replacing the filler path with your path to the download.

**sudo dpkg -i path/to/package.deb**

Finally, verify that your installation was successful by running the Hello, World Docker image. 
To do this, enter the following command:

**sudo docker run hello-world**
