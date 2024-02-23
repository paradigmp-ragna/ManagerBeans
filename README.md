# ManagerBeans
Office ai
5001 /ai

# Home
3000 /

# Postgres
5432 /pg

# Postgres Admin
8050 - (5432)

# Dashboard
3001 /dash

# docker
workflow

# nginx
80 ()

# authorization
5000 /auth

# Node JS
5003 /node

# Task
5002 /task

# React Flow
3002 /flow

# docker visualizer
8080 ()

# Chat Bot
3003 /chat

# temp
File storage or artifact storage



# Nginx
docker build -t nginx-balancer .
docker run -d --name nginx-container -p 81:80 --network my-network nginx-balancer

# Home
docker build -t webapp-home .
docker run -d --name webapp-home -p 3000:3000 --network my-network webapp-home










events {
    worker_connections 1024;
}

http {
    server {
        listen 80;

        location / {
            proxy_pass http://webapp-home;
        }

        location /login {
            proxy_pass http://webapp-home;
        }

        location /register {
            proxy_pass http://webapp-home;
        }

        location /auth {
            proxy_pass http://webapp-auth;
        }

        location /pg {
            proxy_pass http://webapp-postgres;
        }
    }
}

