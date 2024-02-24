# ManagerBeans
Office ai
5001 /ai

# Home
3000 /

# Postgres
5432

# Postgres Admin
8050 - (5432)

# Dashboard
3001 /dash

# docker
workflow

# nginx
80 ()

# authorization (not used)
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

# Postgres
docker run -d --name webapp-postgres --network my-network --network-alias webapp-postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_USER=myuser -e POSTGRES_DB=mydatabase postgres

docker run --name sqltutorial --network my-network -e POSTGRES_PASSWORD=marviniscool -e POSTGRES_USER=myuser -e POSTGRES_DB=maintenance_db -p 5432:5432 -d postgres

docker build -t webapp-postgres .

docker run --name webapp-postgres --network my-network -e POSTGRES_PASSWORD=pass123 -e POSTGRES_USER=myuser -e POSTGRES_DB=maintenance_db -p 5432:5432 -d webapp-postgres


# Postgres Admin (application working)
docker run -d --name webapp-pgadmin --network my-network -p 5050:5050  thajeztah/pgadmin4

# Swarm visualizer
docker swarm init
docker run -it -d -p 8081:8080 --name vis -v /var/run/docker.sock:/var/run/docker.sock dockersamples/visualizer

$$ docker swarm join --token SWMTKN-1-5pefww4sftexv76139ucuvmt3l4nx7c2n9hl25wqqzl5vy9ebs-ddgmadny55ij4l258f56zh23f 192.168.65.3:2377
$$ current node (onld95abuc43tdomv6yy9mvpr) is now a manager.

docker network create -d overlay replication
docker network inspect replication
docker service create --name nginx-container -p 81:80 --network replication --replicas 2 nginx-balancer
docker service create --name webapp-home -p 3000:3000 --network replication --replicas 2 webapp-home

$$ docker service update --replicas 7 sleep-app

docker service rm nginx-container
docker service rm webapp-home

docker kill vis
docker swarm leave --force













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

