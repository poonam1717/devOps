FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y 
RUN apt-get install python3-dev -y
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python3" , "/app/app.py"]
EXPOSE 5000
