# Exercise 2 - Another Dockerfile

Your mission: build and run a Docker image for the Python application in `src/`. This application expects an environment variable `PORT` to know on which port it should listen. We will use port 6666.

When the application runs, use your browser to go to http://127.0.0.1:6666 - you should see: `Congrats!`.

## Hints and solution

<details>
  <summary>Hint #1</summary>


  The Dockerfile is very similar to the one of Exercise 1
</details>


<details>
  <summary>Hint #2</summary>


  Once you have your Docker image built, how do you specify an environment variable when running a container?
</details>

<details>
  <summary>Hint #3</summary>


  Don't forget to expose the container's port! Otherwise you won't be able to reach it.
</details>

<details>
  <summary>Solution</summary>


  Dockerfile:

  ```
  FROM python:3.7
COPY src /
RUN pip install -r /requirements.txt
ENTRYPOINT python /main.py
```

  Build the image: 

  ```
docker build . -t exercise2
  ```

  Run it:

  ```
docker run --rm -it -e PORT=6666 -p 6666:6666 exercise2
  ```

  You can now access the application on `127.0.0.1:6666`. Note that we could specify another host port (e.g. `-p 1111:6666`), and we would be able to access the application on `127.0.0.1:1111`.
</details>