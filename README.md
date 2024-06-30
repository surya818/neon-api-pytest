# neon-api-pytest
Neon-API test automation framework in Python

Test Automation framework in python to test <a href=https://api-docs.neon.tech/reference/getting-started-with-neon-api> Neon database REST API </a>

**Tech Stack:**
Python </br>
pytest</br>
The whole setup is containerized. The dockerfile has everything needed for setting up both python and running tests</br>
And finally, we used an alpine python docker image and the size is close to 70 MB as compared to python base image which is around 10 times bigger

**Prerequisites/Setup for docker based run:**
</br>Created a free <a href=https://neon.tech/>Neon DB account</a>, acquire an API key</br>
Docker is installed on the local system</br>

**How to Run**

</br>- Clone this repo</br>
- Save the Neon API key in an environment variable called APIKEY</br>
- Navigate to root directory of the repo</br>
- Build the docker image with command ==> docker build -t neon-test:1.0 .</br>
- Verify docker image is built successfully using docker images command</br>
- Run the docker image in a container, which will run the tests and save the test reports locally, in the host machine</br>
_docker run -v <TESTOUTPUT_PATH>:/results -e APIKEY=%APIKEY% neon-test:1.0</br>
e.g, docker run --rm -v C:\Data\results:/results -e APIKEY=%APIKEY% neon-test:1.0 in Windows,</br>
docker run --rm -v ~/results:/results -e APIKEY=%APIKEY% neon-test:1.0 in Unix based systems</br>_
- It is important that the APIKEY environment variable is set in the container, else the tests fail</br>
- Change the TESTOUTPUT_PATH to your desired location to save test results</br>
- Verify Test results in your set location</br>
- What's happening behind the scenes: The Dockerfile uses a python base image, which has python pre-built.</br>
- Copy the requirements.test and run the pip install, to setup pytest, the pythong test framework. </br>

- Our docker run command has a -v option, which creates a volume, and this is how we copy the test result reports to the host machine

![image](https://github.com/surya818/neon-api-pytest/assets/7116020/e427150f-78d2-4c3c-a6fb-caa4c73d45ed)


**How to Run: (Alternate way/ Non Docker )** (If you want to just run the tests locally, without using Docker) 

</br>- Navigate to the root directory</br>
- Enter the command pytest and hit enter, and the tests start running</br>

![image](https://github.com/surya818/neon-api-pytest/assets/7116020/3abe0e3d-82c5-4402-8baa-eaf65796a907)
