# 🐳 DOCKER SHORT NOTES!

Dockerfile ~ *Think of it as recipe*


Docker image ~ *Think of it as blueprint*


Docker container ~ *This is now the box*

![Must Know Docker Concepts](must-know-docker-concepts.png)

## 📘 Table of Contents
1. [Dockerfile](#dockerfile)
2. [Docker Images CLI Commands](#docker-images-cli-commands)
3. [Docker Containers CLI Commands](#docker-containers-cli-commands)
4. [Docker Volumes CLI Commands](#docker-volumes-cli-commands)
5. [Docker Networks CLI Commands](#docker-networks)
6. [Docker Registry CLI Commands](#docker-registry--cli-commands)
7. [Docker Compose CLI Commands](#docker-compose-cli-commands)
8. [Docker Login CLI Commands](#docker-login-cli-commands)
9. [Docker System Cleanup and Troubleshooting](#docker-system-cleanup-and-troubleshooting)
## Dockerfile

- Must be named as **"Dockerfile"** in your project folder

### Structure

```Dockerfile
# Base image to build this image from
FROM <image_id>
# Example:
FROM python:3.10-slim

# Executes commands to modify container’s file system state
RUN <command>             # shell form
RUN ["executable", "param1", "param2"]   # exec form
# Example:
RUN apt-get update && apt-get install -y curl # Reduce image size by cleaning temp files

# Information about the image creator
MAINTAINER <name>

# Adds searchable metadata to the image
LABEL <key>=<value>
# Example:
LABEL maintainer="you@example.com"
LABEL version="1.0" description="Simple Flask App"

# Defines build-time variables (only available during build)
ARG <name>[=<default value>]
# Example:
ARG APP_VERSION=1.0

# Defines environment variables (available at runtime)
ENV <key>=<value>
# Example:
ENV APP_ENV=production

# Add files or remote URLs (auto-extracts archives)
ADD <src> <dest>          # can fetch URLs and auto-extract archives
# Example:
ADD https://example.com/file.tar.gz /app/

# Copies files/directories into the image
COPY <src> <dest>         # simple copy (does NOT support URLs)
# Example:
COPY . /app

# Mounts a directory to be shared with host/other containers
VOLUME ["<path>"]

# Exposes a port to be used at runtime
EXPOSE <port>
# Example:
EXPOSE 8080

# Sets the working directory for subsequent instructions
WORKDIR <path>
# Example:
WORKDIR /app

# Specifies the user to run commands as
USER <username>[:<group>]

# Defines the signal sent to stop the container
STOPSIGNAL <signal>

# Sets environment variable for all future CMD/ENTRYPOINT
SHELL ["executable", "parameters"]

# Defines the default command to execute when container starts
ENTRYPOINT ["executable", "param1", "param2"]
# Example:
ENTRYPOINT ["python", "app.py"]

# Defines the default command (can be overridden)
CMD ["executable","param1","param2"]   # exec form
# or
CMD <command>                          # shell form
# Example:
CMD ["python", "app.py"]
CMD echo "Hello, Lagat!"

```

## Docker Images CLI Commands

```bash
# 🐳 Build an Image from a Dockerfile
docker build -t <image_name> .

# 🧹 Build an Image from a Dockerfile without using the cache
docker build -t <image_name> . --no-cache

# 📋 List all local images
docker images

# ❌ Delete a specific image
docker rmi <image_name>

# 🧼 Remove all unused images
docker image prune

```

## Docker Containers CLI Commands

```bash
# 🐳 Create and run a container from an image, with a custom name
docker run --name <container_name> <image_name>

# 🌐 Run a container and publish a container’s port(s) to the host
docker run -p <host_port>:<container_port> <image_name>

# 🏃 Run a container in the background (detached mode)
docker run -d <image_name>

# ▶️ Start or ⏹️ Stop an existing container
docker start <container_name> # (You can also use container IDs)
docker stop <container_name> # (You can also use container IDs)

# 🗑️ Remove a stopped container
docker rm <container_name>

# 💻 Open an interactive shell inside a running container
docker exec -it <container_name> sh # (Use 'bash' instead of 'sh' if available)

# 📜 Fetch and follow the logs of a container
docker logs -f <container_name>

# 🔍 Inspect detailed information about a container
docker inspect <container_name> # (You can also use container IDs)


# 📋 List currently running containers
docker ps

# 📦 List all containers (running and stopped)
docker ps --all

# 📊 View live resource usage stats for containers
docker container stats
```

## Docker Volumes CLI Commands

```bash
# 📦 Create a new named volume
docker volume create <volume_name>

# 🧾 List all volumes
docker volume ls

# 🔍 Inspect detailed information about a volume
docker volume inspect <volume_name>

# 🗑️ Remove a specific volume
docker volume rm <volume_name>

# 🧹 Remove all unused volumes
docker volume prune

# 🧰 Mount a volume when running a container
docker run -v <volume_name>:<container_path> <image_name>
# Example:
# docker run -v my_data:/app/data nginx

# 🪟 Bind mount a local directory to a container directory
docker run -v <host_path>:<container_path> <image_name>
# Example:
# docker run -v $(pwd):/usr/src/app python:3.9
```

## Docker Networks CLI Commands

```bash
# 🧱 Create a user-defined bridge network
docker network create <network_name>

# 📋 List all Docker networks
docker network ls

# 🔍 Inspect detailed information about a network
docker network inspect <network_name>

# 🔗 Connect a container to a specific network
docker network connect <network_name> <container_name>

# 🔗 Disconnect a container from a specific network
docker network disconnect <network_name> <container_name>

# 🗑️ Remove a specific network
docker network rm <network_name>

# 🧹 Remove all unused networks
docker network prune

# 🐳 Run a container and attach it directly to a specific network
docker run --network <network_name> --name <container_name> <image_name>

# 🔧 Example: Create a custom network and connect containers
docker network create my_network
docker run -d --name db --network my_network mysql
docker run -d --name web --network my_network nginx
```

## Docker Registry CLI Commands

```bash
# ⬇️ Pull an image from a registry (default: Docker Hub)
docker pull <image_name>:<tag>
# Example:
# docker pull nginx:latest

# 🏷️ Tag an existing local image for a registry
# Format: docker tag <source_image> <registry_url>/<repository>/<image>:<tag>
docker tag <image_name>:<tag> <registry_url>/<repo>/<image_name>:<tag>
# Example (for local registry):
# docker tag nginx:latest localhost:5000/nginx:latest
# Example (for Docker Hub):
# docker tag myapp:latest your_dockerhub_username/myapp:latest

# 🚀 Push an image to a registry
docker push <registry_url>/<repo>/<image_name>:<tag>
# Example:
# docker push your_dockerhub_username/myapp:latest

# 🔐 Log in to a registry
docker login <registry_url>
# Example (for Docker Hub):
# docker login
# Then enter your username and password or personal access token

# 🧱 Run your own private registry
# Pull the official registry image and run it as a container
docker run --name my-registry -p 5000:5000 --restart=always -d registry:2

# 🕵️ Verify it's running
docker ps

# 🔁 Push and pull to your local private registry
# Tag the image for localhost:5000 (your local registry)
docker tag nginx:latest localhost:5000/nginx:latest

# Push it to the private registry
docker push localhost:5000/nginx:latest

# Pull it back from the local registry
docker pull localhost:5000/nginx:latest

# 📂 Check what’s stored in your local registry
curl -X GET http://localhost:5000/v2/_catalog

# 🧹 Delete unused images and clean the registry
docker image prune
docker container prune
docker volume prune
```

## Docker Compose CLI Commands

```bash
# 🚀 Create and start all containers defined in docker-compose.yml
docker compose up

# 🕶️ Run in detached mode (background)
docker compose up -d

# 🧹 Stop and remove containers, networks, and volumes created by `up`
docker compose down

# 📋 View the running services (containers)
docker compose ps

# ⏸️ Stop containers without removing them
docker compose stop

# ▶️ Start containers that were stopped
docker compose start

# 🔁 Restart all services
docker compose restart

# 🧾 View logs from all services
docker compose logs

# 👀 Follow logs in real-time
docker compose logs -f

# 🏗️ Build or rebuild images defined in the Compose file
docker compose build

# 💬 Run a one-time command inside a running service container
docker compose exec <service_name> <command>
# Example:
# docker compose exec web ls /app

# 🗑️ Remove stopped service containers
docker compose rm

# 🧹 Remove all unused data (containers, images, volumes)
docker system prune

# 🧩 Example docker-compose.yml

# version: "3.8"
# services:
#   web:
#     image: nginx
#     ports:
#       - "8080:80"
#   db:
#     image: mysql:5.7
#     environment:
#       MYSQL_ROOT_PASSWORD: example
```

![Docker-compose cheat sheet](docker-compose-cheat-sheet.png)

## Docker Login CLI Commands

```bash
# 🔐 Login into Docker Hub
docker login -u <username>
# Example:
# docker login -u lagatjepkorir

# 🚀 Publish (push) an image to Docker Hub
docker push <username>/<image_name>
# Example:
# docker push lagatjepkorir/webapp-color

# 🔍 Search Docker Hub for an image
docker search <image_name>
# Example:
# docker search nginx

# ⬇️ Pull an image from Docker Hub
docker pull <image_name>
# Example:
# docker pull nginx:latest
```

## Docker System Cleanup and Troubleshooting

```bash
# 🗑️ Remove all stopped containers
docker container prune

# 🧼 Remove all unused images
docker image prune -a

# 🌐 Remove unused networks
docker network prune

# 💾 Remove unused volumes
docker volume prune

# ⚠️ Remove EVERYTHING unused (containers, images, networks, volumes)
docker system prune -a --volumes

# 📊 Check Docker disk usage
docker system df

# 🧠 Show Docker info and environment details
docker info
docker version
```

-----------------------------------------

💡 **Pro Tip:** Use `docker compose` (v2 syntax) instead of `docker-compose` — it’s the newer, integrated version.

🧠 Always tag your images (`:latest`, `:v1`, etc.) to avoid confusion during deployment.

🚀 *Happy Coding!*