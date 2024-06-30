# neon-api-pytest
Neon-API test automation framework in Python

Test Automation framework in python to test Neon database REST API

**Tech Stack:**
Python
pytest
The whole setup is containerized. The dockerfile has everything needed for setting up both python and running tests

**Prerequisites/Setup for docker based run:**
Created a free Neon DB account, acquire an API key
Docker is installed on the local system

**How to Run**

Clone this repo
Save the Neon API key in an environment variable called APIKEY
Navigate to root directory of the repo
Build the docker image with command ==> docker build -t neon-test:1.0 .
Verify docker image is built successfully using docker images command
Run the docker image in a container, which will run the tests and save the test reports locally, in the host machine
docker run -v <TESTOUTPUT_PATH>:/results -e APIKEY=%APIKEY% neon-test:1.0
e.g, docker run --rm -v C:\Data\results:/results -e APIKEY=%APIKEY% neon-test:1.0 in Windows,
docker run --rm -v ~/results:/results -e APIKEY=%APIKEY% neon-test:1.0 in Unix based systems
It is important that the APIKEY environment variable is set in the container, else the tests fail
Change the TESTOUTPUT_PATH to your desired location to save test results
Verify Test results in your set location
What's happening behind the scenes: The Dockerfile uses a python base image, which has python pre-built.
Copy the requirements.test and run the pip install, to setup pytest, the pythong test framework. 

Our docker run command has a -v option, which creates a volume, and this is how we copy the test result reports to the host machine

![image](https://github.com/surya818/neon-api-pytest/assets/7116020/e427150f-78d2-4c3c-a6fb-caa4c73d45ed)


**How to Run: (Alternate way/ Non Docker )** (If you want to just run the tests locally, without using Docker) 

Navigate to the root directory
Enter the command pytest and hit enter, and the tests start running

![image](https://github.com/surya818/neon-api-pytest/assets/7116020/3abe0e3d-82c5-4402-8baa-eaf65796a907)
