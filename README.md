# Docker exercises

- Exercise 0 - Install Docker
- Exercise 1 - Basic Dockerfile
- Exercise 2 - Environment variables and exposing ports

## Useful commands

|                                 Description                                 	|                                 Command                                 	|
|:---------------------------------------------------------------------------:	|:------------------------------------------------------------------------:	|
|                           List running containers                           	|                                `docker ps`                               	|
|                            List downloaded images                           	|                             `docker image ls`                            	|
|           Remove unused images (will free up a lot of disk space!)          	|                          `docker image prune -a`                         	|
|                                Build an image                               	|                     `docker build . -t imagename:tag`                    	|
|                               Run a container                               	|                    `docker run --rm -it imagename:tag`                   	|
|                 Run a container with a file share ("volume")                	| `docker run -v /path/to/share:/path/in/container --rm -it imagename:tag` 	|
| Run a container and map port 8000 on the host to port 4444 in the container 	|             `docker run -p 8000:4444 --rm -it imagename:tag`             	|