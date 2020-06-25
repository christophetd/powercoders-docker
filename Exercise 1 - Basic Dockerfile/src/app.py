import time
import requests

while True:
  weather = requests.get("https://wttr.in/lausanne?format=3").text
  print(weather)
  print("")
  time.sleep(5)
