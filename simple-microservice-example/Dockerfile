# Using lightweight alpine image with preinstalled python 3.6 env
# (default ptyhon 3 docker image)
FROM python:3.6-alpine

#update and install packages
RUN until apk update; do sleep 1; done
RUN  pip install --no-cache-dir pipenv

#Defining working dir and adding source code
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./

COPY cashman ./cashman

#Install API dependencies
RUN pipenv install

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]
