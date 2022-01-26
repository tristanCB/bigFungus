https://stackoverflow.com/questions/14972792/nginx-nginx-emerg-bind-to-80-failed-98-address-already-in-use
UBUNTU AWS free tier
open https and http

# Setting up webapp
Purchased domain
Launched EC2 ubuntu server with open ports on https and http
    > sudo apt install nginx
    > sudo apt install certbot
    > sudo apt install python3-pip
    > sudo certbot --nginx -d DOMAINNAIME

pip install requirements

ensure flask app does running
place nginx conf file in nginx / sites-enabled
restart nginx

NGINX --> GUNICORN --> running app

