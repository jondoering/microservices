# Basic template for creating a microservice-like application with Flask in Python for a trained machine learning model

## Deploying a trained ML model as a container, requires to implement the ML model as instance of class MlAlgorithm

### Dependencies

additional packages need to be included into the virtual environment
by using pipenv. Resolving dependencie is done automatically by using
the virtual environment within the docker container.

### Create Container and run it
created and altered docker file to run Service in a container
- docker build -t <MyMlMicroService> .
- docker run --name <MyMlMicroService> -d -p 5000:5000 <MyMlMicroService>
