# Exercise 1 - Basic Dockerfile

Your mission is to write a Dockerfile for the application contained in `src/`. This is a simple  Python 3 application using the `requests` library and the [wttr.in](https://github.com/chubin/wttr.in) API to print the weather in Lausanne every 5 seconds.

## Step-by-step

### Step 1: Choose your base image

Knowing that the application is a Pythono 3 application, which base image would you use?

<details>
  <summary>Hint</summary>

  This is a Python-based application. What Python images are available in the Docker hub?
</details>

<details>
  <summary>Solution</summary>


  You can use `python:3.7`. This will go in the "FROM" section of your Dockerfile.
</details>

### Step 2: Determine which files you need to copy in the image

Which source code file(s) do you need to be able to run this application?

<details>
  <summary>Solution</summary>


  You will need `src/app.py` and `src/requirements.txt`, which you will `COPY` inside your image.
</details>

### Step 3: What commands do you need to run to install dependencies?

<details>
  <summary>Hint</summary>

  Dependencies of Python applications often need to be installed using `pip`.
</details>

<details>
  <summary>Solution</summary>


  You need to `RUN` `pip install -r requirements.txt` to install the dependencies.
</details>

### Step 4: How do you start the application?

This will be your `ENTRYPOINT`.

<details>
  <summary>Solution</summary>


  To run the application, you can simply use `python app.py`
</details>

## Assemble your Dockerfile!

Using the answers above, try to assemble your Dockerfile. Once you get it right, you should have the following output when you try to build it and run a container from it:

```
$ docker build . -t exercise1
Step 1/4 : FROM python:3.7
 ---> e4e55e98f1e0
Step 2/4 : COPY src /
 ---> Using cache
 ---> 63ab40fd7b02
Step 3/4 : RUN pip install -r /requirements.txt
 ---> Running in 7d9d69df53e7
Collecting requests==2.24.0
  Downloading requests-2.24.0-py2.py3-none-any.whl (61 kB)
Collecting chardet<4,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2020.6.20-py2.py3-none-any.whl (156 kB)
Collecting idna<3,>=2.5
  Downloading idna-2.9-py2.py3-none-any.whl (58 kB)
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Downloading urllib3-1.25.9-py2.py3-none-any.whl (126 kB)
Installing collected packages: chardet, certifi, idna, urllib3, requests
Successfully installed certifi-2020.6.20 chardet-3.0.4 idna-2.9 requests-2.24.0 urllib3-1.25.9
Removing intermediate container 7d9d69df53e7
 ---> f1349ffcd218
Step 4/4 : ENTRYPOINT python /app.py
 ---> Running in d9d93f7fd7bf
Removing intermediate container d9d93f7fd7bf
 ---> 18341f77a7ac
Successfully built 18341f77a7ac
Successfully tagged exercise1:latest

$ docker run --rm -it exercise1
Alias tip: d run --rm -it exercise1
lausanne: ⛅️  +15°C
```

## Solution

We highly encourage you give it a try before looking at the solution!

<details>
  <summary>Solution</summary>


  ```
  FROM python:3.7
COPY src /
RUN pip install -r /requirements.txt
ENTRYPOINT python /app.py
```
</details>

## More advanced (optional)

If you use `docker image ls`, you'll see that your image weights approximately 927MB. This is quite a lot, and is because Python images are based from a Debian base image which is quite heavy. To make it (much) lighter, you can use the alternative `python:3.7-alpine` image instead!