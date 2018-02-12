#Trainingsproject to create a microservice-like application

Following the example in :


#Done
##created folder cashman
Mainfolder of the prohect
##Created project python env with pipenv
> pipenv --three

created files Pipfile wich contains details about our project

##Created bootstrap.sh
> touch bootstrap.sh
> chmod +x bootstrap.sh
facilitates stat up process of the application

##Created model package to encpsulate data in classes

## Created dockerfile to dockerize app in a container

created and altered docker file

> docker build -t cashman .
> docker run --name cashman -d -p 5000:5000 cashman
