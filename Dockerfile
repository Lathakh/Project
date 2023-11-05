# to create docker image  
# set of instruction 
# we see the docker image in dockerhub
FROM python:3.8-slim-buster  # it fetching image python3 from dockerhub 
WORKDIR /service
COPY requirements.txt .
COPY . ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python3","app.py"]
