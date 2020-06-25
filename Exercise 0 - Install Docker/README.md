# Exercise 0 - Install Docker on your machine

## Instructions

Note: if you have the choice, Docker will likely perform better on Linux-based machines such as Ubuntu.

- [Instructions for Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [Instructions for Mac](https://docs.docker.com/docker-for-mac/install/)
- [Instructions for Windows](https://docs.docker.com/docker-for-windows/install/)

## (Linux only) Adding your user to the 'docker' group

By default, you need to use `sudo` before running any Docker command. To make it more convenient, you can add yourself to the `docker` group by running:

```
sudo groupadd docker
sudo usermod -aG docker $USER
```

And close/re-open your terminal.

## Verifying Docker is correctly installed

```
docker run -it hello-world
```

Should output something similar to:

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```