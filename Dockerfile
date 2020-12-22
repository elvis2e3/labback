FROM python:rc-buster

RUN apt update && apt install -y nginx

COPY requirements.txt /

RUN pip3 install -r requirements.txt

RUN pip3 install gunicorn

COPY configNginx /etc/nginx/sites-available/default

COPY nginx.conf /etc/nginx/nginx.conf

COPY configServer /etc/init.d/configServer

RUN chmod 777 /etc/init.d/configServer

COPY . /app

WORKDIR /app

CMD ["/etc/init.d/configServer", "start"]
