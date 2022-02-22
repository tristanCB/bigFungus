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
db itegration? probably will go with alchemy SQL
set environment variables
Look into either using https://github.com/cscortes/htmxflask/blob/master/ACTIVESEARCH/templates/index.html or Ajax with flask to optimize page loading
    Somewhat optimized page loading with lazy loading and more selective sql queries.
Write staging script

To Run:
    conda create --name bigFungus python=3.8 --file spec-file.txt