ets server for deployment
# install nginx
sudo apt-get update -y
sudo apt-get install nginx -y

# creates necessary folders
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# creates index.html file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# creates a symbolic link
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

# change ownership of folder
sudo chown -R ubuntu:ubuntu /data/

# setups config file
echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;
        add_header X-Served-By 246664-web-01;
        error_page 404 /custom_404.html;
        rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;

	location /hbnb_static {
                alias /data/web_static/current/;
        }

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }
}" | sudo tee /etc/nginx/sites-available/default

# restarts server
sudo service nginx restart
