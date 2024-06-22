FROM python:3.8.0-buster
COPY . var/opt/
WORKDIR /var/opt/
RUN apt-get update
RUN pip install flask
RUN pip install pusher
RUN chmod 777 miapp.py
EXPOSE 5000
CMD [ "python3", "miapp.py"]