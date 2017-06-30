
# Task 3
## Single Page site with Django, containerized with Docker

### Overview
The contents of this folder are the Django application files for the site, and a Dockerfile.

The Dockerfile can be used to build and run an image (using both Django and Gunicorn) that produces a multi-device compatible site.
It is almost identical to the Google Developer Fundamentals site here (https://developers.google.com/web/fundamentals/getting-started/your-first-multi-screen-site/?hl=en),
with slight changes and a live display of date and time. 

### How to Run the Dockerfile

First, ensure that you have Docker installed by running the following command:

**docker version**

If you do not see information about your Docker version, please continue in the 'Installing Docker' section below.

If Docker is installed, you must next pull this folder into your own repository, navigate to it, and run the following command in the terminal:

**docker build -t insertnamehere .**

This will build a Docker image as per the Dockerfile instructions, and give it the name you entered in "insertnamehere". Names must be entirely lowercase.
Next, to run the image, you will need to run the following command in the terminal:

**docker run -it -p 8000:8000 insertnamehere**

This will run the image (by the name you gave it) and map it to 127.0.0.1:8000

### Accessing the Site

Once you have successfully completed the steps above, leave the image running in the terminal.
Then, open your preferred web  browser and type in 127.0.0.1:8000 or localhost:8000 into the addressbar.
This will open the site running on the image.

### Installing Docker

*Please note this may not be necessary. Check to see if you already have Docker installed first, with **docker version**.*

I would recommend going to the official Docker site and following the instructions for your specific set up and OS.

The installing site can be found [here](https://docs.docker.com/engine/installation/#supported-platforms)
