from flask import Flask
import os
import sys

app = Flask(__name__)


@app.route('/')
def hello():
    return "Congrats!"

if __name__ == '__main__':
  if 'PORT' not in os.environ:
    print("You forgot to specify a port!", file=sys.stderr)
    exit(1)

  app.run(host='0.0.0.0', port=os.environ['PORT'])