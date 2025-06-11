# pulling the docker image 
FROM python:3.12-slim

# define the working directory
WORKDIR backend

# copy all project files to backend/app
COPY . backend

# update pip
RUN pip install --upgrade pip 

# install all requiremnts 
RUN pip install -r backend/requirements.txt

# expose flask port
EXPOSE 5000

# run flask app
CMD [ "python" "backend/app/main.py"]