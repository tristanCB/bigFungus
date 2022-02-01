# Setting up webapp
Purchased domain [bigfungus.ca](https://bigfungus.ca)

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

# To dos
Create products on stripe and link them with the ones in .py script
db itegraation? probably will go with alchemy SQL
set environment variables