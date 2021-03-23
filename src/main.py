import pandas as pd
from flask import Flask
app = Flask(__name__)

# esto es un comentario
def suma(a,b):
  return a+b

# este es el endpoint
@app.route("/")
def hello():
    res = suma(4,2)
    return "Hello World! %s" % (res)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
