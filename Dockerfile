# python version-OS
FROM python:3.8-slim-buster

# setup working directory in container
WORKDIR  /flask-loan-app

RUN python3 -m pip install --upgrade pip

# copy requirement.txt to containers requirement.txt 
COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt 

# copy current folder content to container folder 
COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

# host can we changed to any ip address
# run docker command
# docker run -d -p 5000:500 name -> first one is local machine port: second is port of container
# docker image ls -> for all image
# docker image name rm -f -> to delete image
# docker tag localrepo gaurav20/new-repo:latest
# docker push gaurav20/reponame:latest