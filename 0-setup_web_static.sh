#!/usr/bin/env bash
#create some files

#install and restart nginx
sudo apt-get update > /dev/null
sudo apt-get install -y nginx > /dev/null 2>&1


sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "abdiwoli page " > /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current || true
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/^server {/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default



sudo systemctl restart nginx
